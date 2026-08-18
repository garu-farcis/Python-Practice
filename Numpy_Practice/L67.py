"""4. Load timeseries.npy. Construct a 2D array of shape (len(ts)-4, 5)
where each row is a sliding window of 5 consecutive values.
 Then compute the variance of every window and return the window with the highest variance."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
data=np.load(file_path)
print(data.shape)
window=5
row=len(data)-4
print(row)
rolling_win = np.array([
    data[i:i + window]
    for i in range(len(data) - window + 1)
])

print(rolling_win)
print(rolling_win.shape)
# arr=rolling_win.reshape(row,5)
windows_var=np.var(rolling_win,axis=1)
high_var=np.argmax(windows_var)