"""1. Load sensor_readings.npy. Divide the array into 4 equal-length segments.
 For each segment compute the mean and standard deviation, then return a (4, 2) array containing these statistics."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
data=np.load(file_path)
print(data.shape)
seg=np.split(data,4)
print(seg)
arr_mean=np.average(seg,axis=1)
print(arr_mean)
arr_std=np.std(seg,axis=1)
print(arr_std)
res=np.column_stack((arr_std,arr_mean))
print(res.shape)