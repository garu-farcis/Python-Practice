"""15. Load sensor_readings.npy and temperatures.npy. Create a random integer index array of length 50 (with replacement).
Use advanced indexing to extract the corresponding values from both arrays and then compute the Pearson correlation between the two extracted series."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
file_path1="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"

arr=np.load(file_path)
arr1=np.load(file_path1)
print(arr1.shape)
print(arr.shape)
# new_arr=np.arange(0,50,1)
max_index = min(len(arr), len(arr1))
new_arr = np.random.randint(0, 45, size=50)
print(new_arr)

sensor_data=arr[new_arr]
temp_data=arr1[new_arr]
print(sensor_data)
print(temp_data)

