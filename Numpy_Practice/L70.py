"""7. Load temperatures.npy. Normalize each column independently to the range [0, 1]
using min-max scaling.
 Then compute the Euclidean distance between every pair of days (rows) and find the two most similar days."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
data=np.load(file_path)
print(data.shape)
normalized_d=(data-np.min(data,axis=0))/(np.max(data,axis=0)-np.min(data,axis=0))
distances = np.linalg.norm(
    normalized_d[:, None, :] - normalized_d[None, :, :],
    axis=2)
np.fill_diagonal(distances, np.inf)
day1, day2 = np.unravel_index(
    np.argmin(distances),
    distances.shape
)
print("Most similar days:", day1, day2)
print("Distance:", distances[day1, day2])

