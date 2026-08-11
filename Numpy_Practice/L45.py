"""10. Load sensor_readings.npy. Sort the array in ascending order.
Using binary search (np.searchsorted), find the insertion points for the values 20, 25 and 30."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
arr=np.load(file_path)
print(arr.shape)
sorted_arr=np.sort(arr)
print(sorted_arr)
vals=[20,25,30]
search=np.searchsorted(sorted_arr,vals)
print(search)