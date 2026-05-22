"""1. Sliding Window Aggregations (Memory-Efficient Strides)

Scenario: You process high-frequency sensor data (millions of rows).
You need rolling statistics without copying data.
Problem: Implement a function using as_strided to compute rolling mean + std (window=60) on a 1D float64 array of length N.
Return a (N-window+1, 2) array of [mean, std].
Must be O(N) time and near-zero extra memory.

Sample Input:
Python
data = np.random.randn(100000).astype(np.float64)
result = rolling_stats(data, window=60)

Expected: result.shape == (99941, 2), very low memory footprint."""

# import numpy as np
# data = np.random.randn(100000).astype(np.float64)
# window=60
# rolling_mean=np.convolve(data,np.ones(window)/window,mode='valid')
# rolling_std=np.convolve(data,np.std(data),mode='valid')
# ans=np.concatenate((rolling_std,rolling_mean))
# # print(np.concatenate((rolling_std,rolling_mean)).reshape(len(ans)-window+1,2))
#
# from numpy.lib.stride_tricks import as_strided
# def rolling_stats(data, window=60):
#     n=data.shape
#     my_shape=(n-window+1,window)
#     strides = (data.strides[0], data.strides[0])
#     windows = as_strided(
#         data,
#         shape=my_shape,
#         strides=strides
#     )
#
#     means = windows.mean(axis=1)
#
#     stds = windows.std(axis=1)
#
#     result = np.column_stack((means, stds))
#
#     return result
#
#
# data = np.random.randn(100000).astype(np.float64)
#
# result = rolling_stats(data, window=60)
#
# print(result.shape)