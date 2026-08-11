"""4. Load timeseries.npy.
Create a rolling window of size 7 and compute the rolling mean.
Store the result as a new array of the same length (pad the beginning with NaN or use valid mode)."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
data=np.load(file_path)
window=7
rolling_mean=np.convolve(data,np.ones(window)/window,mode="valid")
print(rolling_mean)

val_mean=np.full(len(data),np.nan)
val_mean[window-1:]=rolling_mean
print(val_mean)