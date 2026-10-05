"""Load sensor_signals.npy.
   Normalize each channel to the range [0, 1] independently.
   Then compute the pairwise Euclidean distances between all 8 channels (treating each channel as a 60-dimensional vector).
   Return the (8, 8) distance matrix and the indices of the two most similar channels."""
import numpy as np

file="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
a=np.load(file)
normalizeed=(a - a.min()) / (a.max() - a.min())
print(a)
distance = np.linalg.norm(a_norm - b_norm)
