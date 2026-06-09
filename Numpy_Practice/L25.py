"""1. Sliding Window Aggregations (Memory-Efficient Strides)
Scenario: You process high-frequency sensor data (millions of rows). You need rolling statistics without copying data.
Problem: Implement a function using as_strided to compute rolling mean + std (window=60) on a 1D float64 array of length N.
Return a (N-window+1, 2) array of [mean, std]. Must be O(N) time and near-zero extra memory.
Sample Input:
Pythondata = np.random.randn(100000).astype(np.float64)
result = rolling_stats(data, window=60)
Expected: result.shape == (99941, 2), very low memory footprint."""



import numpy as np
from numpy.lib.stride_tricks import as_strided


def rolling_stats(data: np.ndarray, window: int = 60) -> np.ndarray:
    """
    Compute rolling mean and standard deviation using as_strided.

    - Extremely memory efficient (only creates a lightweight view + output array)
    - O(N) time complexity
    - Returns shape (N - window + 1, 2) → [[mean, std], ...]
    """
    if not isinstance(data, np.ndarray) or data.ndim != 1 or data.dtype != np.float64:
        raise ValueError("Input must be a 1D float64 numpy array")

    N = len(data)
    if window < 1 or window > N:
        raise ValueError(f"window must be between 1 and {N}")

    # Create strided view of overlapping windows - NO data copying!
    shape = (N - window + 1, window)
    strides = (data.strides[0], data.strides[0])  # key for overlapping

    windows = as_strided(data, shape=shape, strides=strides)

    # Compute statistics along each window (axis=1)
    means = np.mean(windows, axis=1)
    stds = np.std(windows, axis=1, ddof=0)  # ddof=0 → population std (common for rolling)
    # Use ddof=1 if you want sample standard deviation

    # Combine into final (M, 2) result
    return np.column_stack((means, stds))