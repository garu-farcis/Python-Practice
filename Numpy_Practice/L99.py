"""2. Extract columns 0 (temp), 1 (humidity) and 4 (voltage) using advanced indexing.
   Create a new 2D array from these three columns. Then use a ufunc to compute
   the element-wise maximum between temperature and voltage (broadcast humidity if needed)."""

import numpy as np
data=np.load("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_log.npy")
temp=data[:,0]
humidity=data[:,1]
voltage=data[:,4]
new_data=np.concatenate([[temp,humidity,voltage]],axis=0)
print(new_data)
ele_wise_max=np.maximum(new_data[:,0], new_data[:,2])
print(ele_wise_max)