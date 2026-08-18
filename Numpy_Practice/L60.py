"""11. Load temperatures.npy. Compute the cumulative sum along the day axis (axis=0).
Then normalize each column so that the
final cumulative value of every month becomes 1.0 (i.e., turn it into a cumulative distribution)."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
data=np.load(file_path)
print(data.shape)
c_sum=np.cumulative_sum(data,axis=0)
final_values = c_sum[-1, :]
normalized = c_sum / final_values
print(normalized)