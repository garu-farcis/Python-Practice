"""1. Sliding Window Aggregations (Memory-Efficient Strides)
Scenario: You process high-frequency sensor data (millions of rows). You need rolling statistics without copying data.
Problem: Implement a function using as_strided to compute rolling mean + std (window=60) on a 1D float64 array of length N.
Return a (N-window+1, 2) array of [mean, std]. Must be O(N) time and near-zero extra memory.
Sample Input:
Pythondata = np.random.randn(100000).astype(np.float64)
result = rolling_stats(data, window=60)
Expected: result.shape == (99941, 2), very low memory footprint."""


import numpy as np


data =np.random.default_rng().random(size=20)
print(data)
window=60
roll_mean=np.convolve(data,data.mean(),data=data/)