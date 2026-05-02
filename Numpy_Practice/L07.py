"""Clean and Normalize Sensor Data
Given a NumPy array of shape (n_rows, n_features) with possible NaN values:

Remove rows that contain any NaN
Normalize each column to have mean = 0 and std = 1
Return the cleaned and normalized array. Do it efficiently (avoid loops)."""
import numpy as np

arr = np.array([
    [1.0, 2.0, np.nan],
    [4.0, np.nan, 6.0],
    [7.0, 8.0, 9.0],
    [np.nan, 5.0, 3.0]
])

arr_clean=np.nanmean(arr,axis=1)
print(arr_clean)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(arr_clean, inds[1])
print(arr)