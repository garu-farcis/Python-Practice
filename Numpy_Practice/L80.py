"""6. Load sensor_signals.npy. Detect peaks in channel 0 (local maxima higher than both neighbors).
Return the time indices of those peaks and the corresponding values."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
import numpy as np
data=np.load(file_path)
channel_0=data[:,0]
mask=(channel_0[1:-1]>channel_0[:-2])&(channel_0[1:-1]>channel_0[2:])
peak_indices=np.where(mask)[0]+1
corr_vals=channel_0[peak_indices]
print(peak_indices)
print(corr_vals)