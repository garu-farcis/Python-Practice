"""Load sensor_signals.npy.
   For each channel, compute both the rolling mean (window=7) and rolling standard deviation (window=7).
   Create a new 3D array of shape (60, 8, 2) that stores [rolling_mean, rolling_std] for every time step and channel.
   Handle the edges with NaN padding."""
from Numpy_Practice.L79 import rolling_mean

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"

import numpy as np
data=np.load(file_path)
window=7
kernel=np.ones(window)/window
rolling_mean=np.apply_along_axis(func1d= (lambda x:np.convolve(x,kernel,mode='same')),axis=0,arr=data)
rolling_std = np.apply_along_axis(
    lambda x: np.array([
        np.std(x[max(0, i-window//2):min(len(x), i+window//2+1)])
        if i >= window//2 and i < len(x)-window//2
        else np.nan
        for i in range(len(x))
    ]),
    axis=0,
    arr=data
)
new_arr = np.full((60, 8, 2), np.nan)
new_arr[:, :, 0] = rolling_mean
new_arr[:, :, 1] = rolling_std

print(new_arr.shape)
print(new_arr)