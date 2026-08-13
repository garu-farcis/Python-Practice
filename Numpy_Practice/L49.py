"""14. Load timeseries.npy. Generate a second array of the same length filled with linear trend values (from 0 to 10).
Subtract this trend from the original series (detrending) and compute the variance of the residual."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
arr=np.load(file_path)
print(arr.shape)
second_arr=np.linspace(0,10,100)
print(second_arr.shape)
sub_trend=arr-second_arr
print(sub_trend)
var=np.var(sub_trend)
print(f"variance is {var}")