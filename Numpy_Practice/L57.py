"""7. Load temperatures.npy. Create a mask of all values that are local
maxima along the month axis (axis=1). A value is a local maximum if it is greater than both its left and right
neighbors (handle edges carefully). Count how many local maxima exist."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
data=np.load(file_path)
local_max=((data[:, 1:-1] > data[:, :-2]) & (data[:, 1:-1] > data[:, 2:]))
indices=np.where(local_max)
print(indices)
print(np.sum(indices))

