"""1. Sliding Window Aggregations (Memory-Efficient Strides)
Scenario: You process high-frequency sensor data (millions of rows). You need rolling statistics without copying data.
Problem: Implement a function using as_strided to compute rolling mean + std (window=60)
on a 1D float64 array of length N. Return a (N-window+1, 2) array of [mean, std]. Must be O(N) time and near-zero extra memory.
Sample Input:
Pythondata = np.random.randn(100000).astype(np.float64)
result = rolling_stats(data, window=60)
Expected: result.shape == (99941, 2), very low memory footprint.
2. Vectorized Grouped Operations (No Pandas)
Scenario: Log data with user_id (int) and value (float). Compute per-user mean and count in pure NumPy, faster than np.unique + loops.
Problem: Given user_ids (int32) and values (float64), same length, return two arrays:
 unique user_ids (sorted) and their means. Bonus: also return counts.
Sample Input:
Pythonuser_ids = np.array([1, 2, 1, 3, 2, 1])
values = np.array([10., 20., 30., 40., 50., 60.])
Expected Output: unique = [1,2,3], means ≈ [33.333, 35., 40.], counts = [3,2,1]
3. Advanced Broadcasting for Imbalanced Time-Series Alignment
Scenario: Align sparse event data with dense time grid.
Problem: Given dense_time (shape T), event_times (shape E), event_values (shape E), create output (T, K)
where each row broadcasts the last K events before that timestamp (use searchsorted + advanced indexing).
4. Memory-Mapped Large Array Transformation
Scenario: You have a 50GB float32 array on disk (memory-mapped). Apply a complex transformation: (x - mean) / std per column,
then clip to [-5,5], then multiply by a sparse mask.
Problem: Write code that minimizes RAM usage (< 4GB peak) while being fast. Explain np.memmap strategy and when to use out= parameter.
5. Efficient Top-K per Row with Column Indices
Scenario: Recommendation system scoring matrix (millions of users × thousands of items).
Problem: For a (M, N) score matrix, return (M, K) indices of top-K items per row and their scores,
using np.argpartition. Handle ties deterministically.
6. Vectorized Levenshtein / Edit Distance Matrix (Broadcasting Trick)
Scenario: Deduplicate millions of short strings (product names) using edit distance.
Problem: Given two arrays of strings A (len M) and B (len N), both short, compute
distance matrix efficiently using NumPy vectorization (character level broadcasting + cumsum). Avoid pure Python loops.
7. Custom ufunc for Piecewise Complex Function
Scenario: Feature engineering with different formulas per data regime.
Problem: Create a ufunc (or simulated via np.select / np.piecewise) that computes:

x**2 if |x| < 1
log(|x|) + sign(x) if 1 <= |x| < 10
sqrt(|x|) otherwise
Apply to a large array with multiple conditions.

8. Stride Tricks for Image-like Patch Extraction (No skimage)
Scenario: 1D signal treated as multi-channel "image" for CNN-style feature extraction in pipeline.
Problem: Given (N, C) time-series, extract overlapping patches of length W with stride S using as_strided.
Return view of shape (num_patches, W, C).
9. Outlier-Resistant Normalization with Quantiles
Scenario: Robust scaling for production pipeline with heavy-tailed data.
Problem: Implement robust_scale using np.nanquantile (5th/95th percentile) to compute center/scale, then clip.
Must handle NaNs and very large arrays efficiently.
10. Kronecker Product for Feature Interactions (Memory Optimized)
Scenario: Polynomial feature expansion for sparse high-cardinality categorical data.
Problem: Efficiently compute interaction features using np.kron or manual broadcasting for
 two arrays A (N, D1) and B (N, D2) → (N, D1*D2) without full materialization if possible.
11. Boolean Indexing + Reduction Performance Trap
Scenario: Filtering massive clickstream data.
Problem: Compare performance (and explain why) of:

data[data > threshold].mean()
vs using np.mean(data, where=data > threshold)
vs boolean mask reuse.
Ask candidate to choose best for N=100M.

12. Multi-dimensional Histogram with Custom Bins
Scenario: Joint distribution analysis of 5 numerical features.
Problem: Compute 5D histogram with irregular bin edges using np.digitize + np.bincount on raveled multi-index.
Return sparse representation if possible.
13. Reproducible Reservoir Sampling with NumPy
Scenario: Streaming data where you can only keep K samples in memory.
Problem: Implement reservoir sampling using np.random with fixed seed that works on chunks.
Return exactly K unique samples with correct probabilities.
14. Advanced Indexing for Graph Adjacency Matrix Construction
Scenario: Building sparse-like adjacency from edge list (source, target, weight).
Problem: Given edges as (E, 2) int array and weights, construct dense adjacency matrix (N x N) efficiently.
Then compute degree + Laplacian (L = D - A) in few lines.
15. Chunked SVD / PCA on Large Matrix (Streaming Style)
Scenario: Dimensionality reduction on TB-scale data.
Problem: Implement incremental mean/variance calculation across chunks,
then approximate PCA using randomized SVD (np.linalg.svd on sketch). Discuss power iteration or Halko method tradeoffs."""



import numpy as np
from numpy.lib.stride_tricks import as_strided




def rolling_stats(data: np.ndarray, window: int = 60):
    if len(data) < window:
        return np.empty((0, 2), dtype=np.float64)

    # Create strided view - zero extra memory
    shape = (len(data) - window + 1, window)
    strides = (data.strides[0], data.strides[0])
    windowed = as_strided(data, shape=shape, strides=strides)

    means = np.mean(windowed, axis=1)
    stds = np.std(windowed, axis=1, ddof=0)  # or ddof=1
    return np.column_stack((means, stds))




data = np.random.randn(100000).astype(np.float64)
result = rolling_stats(data, 60)
print(result.shape)  # (99941, 2)




def groupby_mean_count(user_ids: np.ndarray, values: np.ndarray):
    # Sort for stability + efficiency
    idx = np.argsort(user_ids)
    user_ids = user_ids[idx]
    values = values[idx]

    # Find group boundaries
    diff = np.diff(user_ids, prepend=user_ids[0] - 1)
    boundaries = np.where(diff != 0)[0]

    unique_ids = user_ids[boundaries]
    counts = np.diff(np.append(boundaries, len(user_ids)))

    # Group sums using ufunc.reduceat
    sums = np.add.reduceat(values, boundaries)
    means = sums / counts

    return unique_ids, means, counts




def align_events(dense_time, event_times, event_values, K=5):
    # Last K events before each dense_time point
    idx = np.searchsorted(event_times, dense_time, side='right') - 1
    valid = idx >= 0

    # Pad for advanced indexing
    padded_events = np.pad(event_values, (K, 0), constant_values=np.nan)
    padded_idx = np.clip(idx[:, None] - np.arange(K), 0, len(event_values) - 1)

    result = padded_events[padded_idx]
    result[~valid] = np.nan
    return result  # shape (T, K)



def robust_transform_large(memmap_path, shape, dtype=np.float32, chunk_size=10_000_000):
    arr = np.memmap(memmap_path, dtype=dtype, mode='r+', shape=shape)
    # Process column-wise or in chunks
    for col in range(arr.shape[1]):
        data = arr[:, col]
        # Use running stats or chunked quantiles for very large data
        mean = np.mean(data)
        std = np.std(data)
        data[:] = np.clip((data - mean) / std, -5, 5)  # in-place
    arr.flush()




def top_k_per_row(scores: np.ndarray, K: int):
    # Negative for descending
    idx = np.argpartition(-scores, K, axis=1)[:, :K]
    # Sort within top-K
    row_idx = np.arange(scores.shape[0])[:, None]
    top_scores = scores[row_idx, idx]
    sort_idx = np.argsort(-top_scores, axis=1)
    return idx[row_idx, sort_idx], top_scores[row_idx, sort_idx]



def edit_distance_matrix(A, B):
    # Simple Levenshtein via dynamic programming vectorized (for short strings)
    A = np.array([list(s) for s in A])
    B = np.array([list(s) for s in B])
    # Full matrix is heavy; often better to use numba or cdist with custom metric
    # For interview: show understanding of broadcasting for DP table
    pass  # Production: use numba.jit or sklearn




def piecewise_transform(x: np.ndarray):
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)

    mask1 = np.abs(x) < 1
    mask2 = (np.abs(x) >= 1) & (np.abs(x) < 10)

    result[mask1] = x[mask1] ** 2
    result[mask2] = np.log(np.abs(x[mask2])) + np.sign(x[mask2])
    result[~mask1 & ~mask2] = np.sqrt(np.abs(x[~mask1 & ~mask2]))
    return result



def extract_patches(data: np.ndarray, W: int, S: int = 1):
    N, C = data.shape
    num_patches = (N - W) // S + 1
    shape = (num_patches, W, C)
    strides = (data.strides[0] * S, data.strides[0], data.strides[1])
    return as_strided(data, shape=shape, strides=strides, writeable=False)





def robust_scale(X: np.ndarray, quantile_range=(0.05, 0.95)):
    X = np.asarray(X, dtype=np.float64)
    q_low, q_high = np.nanquantile(X, quantile_range, axis=0)
    scale = q_high - q_low
    scale[scale == 0] = 1.0
    center = np.nanmedian(X, axis=0)
    return np.clip((X - center) / scale, -5, 5)





def interaction_features(A: np.ndarray, B: np.ndarray):
    # A (N, D1), B (N, D2) -> (N, D1*D2)
    return (A[:, :, None] * B[:, None, :]).reshape(A.shape[0], -1)



#
# mask = data > threshold
# mean_val = np.mean(data, where=mask) if hasattr(np.mean, 'where') else data[mask].mean()




def multi_hist_nd(data: np.ndarray, bins):
    # data (N, D)
    digitized = np.stack([np.digitize(data[:, i], bins[i]) for i in range(data.shape[1])], axis=1)
    flat_idx = np.ravel_multi_index(digitized.T, [len(b) + 1 for b in bins])
    hist = np.bincount(flat_idx, minlength=np.prod([len(b) + 1 for b in bins]))
    return hist.reshape([len(b) + 1 for b in bins])




def reservoir_sample(stream, K: int, seed=42):
    rng = np.random.default_rng(seed)
    reservoir = np.empty(K, dtype=object)
    for i, item in enumerate(stream):
        if i < K:
            reservoir[i] = item
        else:
            j = rng.integers(0, i + 1)
            if j < K:
                reservoir[j] = item
    return reservoir




def build_adjacency(edges: np.ndarray, weights: np.ndarray, N: int):
    A = np.zeros((N, N), dtype=float)
    A[edges[:, 0], edges[:, 1]] = weights
    # Optional: A += A.T if undirected
    degrees = A.sum(axis=1)
    D = np.diag(degrees)
    L = D - A
    return A, L





def incremental_pca(chunks, n_components=50):
    # Chunked mean/variance
    mean = np.zeros(chunks[0].shape[1])
    M2 = np.zeros_like(mean)
    n = 0
    for chunk in chunks:
        chunk = chunk - mean
        n += len(chunk)
        mean += chunk.mean(axis=0) * (len(chunk) / n)  # Welford style
        # ... full implementation uses randomized SVD on sketch
    # Final step: use np.linalg.svd on column-sampled matrix
    pass  # Production: use sklearn IncrementalPCA or fbpca


