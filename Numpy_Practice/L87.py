"""Load weather_stations.npy.
   Standardize every column (zero mean, unit variance).
   Then compute the Euclidean distance of every day to the “average day” (the mean vector).
   Return the indices of the 5 most unusual days (largest distances) and their distance values."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"

import numpy as np
data=np.load(file_path)