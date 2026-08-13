"""2. Load temperatures.npy. For each day (row), find the month that had the maximum temperature.
 Return a 1D array of length 30 containing those month indices (0-based)."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
data=np.load(file_path)
temp=np.max(data,axis=0)
max_tem=np.argmax(temp)
# max_month=temp[max_tem]
# print(max_month)
month=np.unravel_index(max_tem,temp.shape)
print(month)