"""6. Load sensor_readings.npy. Create a boolean mask for values that
 are local minima (smaller than both immediate neighbors).
Return the indices of all local minima and the corresponding values."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
data=np.load(file_path)
print(data.shape)
mask=((data[1:-1]<data[:-2]) & (data[1:-1]<data[2:]))
local_min=data[1:-1][mask]
print(local_min)
ind=np.where(mask)[0]+1
print(ind)
