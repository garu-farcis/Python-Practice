"""1. Load weather_stations.npy. Compute the mean and standard deviation of each column.
Then create a standardized version of the entire array (zero mean, unit variance per column)."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
import numpy as np
data=np.load(file_path)
print(data)