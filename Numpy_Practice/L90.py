"""Load sensor_signals.npy.
   Normalize each channel to the range [0, 1] independently.
   Then compute the pairwise Euclidean distances between all 8 channels (treating each channel as a 60-dimensional vector).
   Return the (8, 8) distance matrix and the indices of the two most similar channels."""
import numpy as np

file="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
a=np.load(file)
normalizeed=(a - a.min()) / (a.max() - a.min())
print(a)
diff = normalizeed[:, np.newaxis, :] - normalizeed[np.newaxis, :, :]
distance = np.linalg.norm(diff,axis=2)
i, j = np.unravel_index(
    np.argmin(np.where(np.eye(8, dtype=bool), np.inf, distance)),
    distance.shape
)
