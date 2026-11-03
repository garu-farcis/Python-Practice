"""1. Load the array. Using broadcasting, subtract the column-wise mean from every row
   (center the data). Then compute the new column-wise standard deviation.
"""

import numpy as np
data=np.load("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_log.npy")
col_wise_mean=np.mean(data,axis=0)
data=col_wise_mean-data
print(data)
col_wise_std=np.std(data,axis=0)