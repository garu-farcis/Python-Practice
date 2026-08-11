"""9. Load timeseries.npy. Create a new array that contains the first differences (arr[i] − arr[i-1]).
Then find the index of the largest positive jump and the largest negative jump."""


import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
arr=np.load(file_path)
print(arr.shape)
new_arr=np.diff(arr)
high_index=np.argmax(new_arr)
neg_index=np.argmin(new_arr)
print(high_index,neg_index)

