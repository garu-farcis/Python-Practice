"""14. Load timeseries.npy. Detect all peaks (local maxima) where the value is higher than
both neighbors and also higher than the global 75th percentile. Return the indices of those strong peaks."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
data=np.load(file_path)
print(data.shape)
global_perc=np.percentile(data,75)
local_maxima=(data[1:-1]>data[:-2])&(data[1:-1]>data[2:])
maxima=data[1:-1][local_maxima]
print(maxima)
result=maxima[maxima>global_perc]
maxima_indices = np.where(local_maxima)[0] + 1
res_indices = maxima_indices[maxima > global_perc]
print(res_indices)