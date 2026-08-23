"""2. Load temperatures.npy. Create a new array of the same shape where every value is replaced by its rank within its
own row (1 = lowest, 12 = highest). Handle ties by assigning the average rank."""

import numpy as np
from scipy.stats import rankdata

file_path = "/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
data = np.load(file_path)
print(data.shape)
ranks = np.apply_along_axis(rankdata, 1, data)
# rank=np.argsort(np.argsort(data,axis=1),axis=1)+1
print(ranks)
# print(data[rank].shape)
newar=np.full_like(data,ranks,dtype=float)
print(newar)