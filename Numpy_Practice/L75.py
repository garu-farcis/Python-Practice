"""1. Load weather_stations.npy. Compute the mean and standard deviation of each column.
Then create a standardized version of the entire array (zero mean, unit variance per column)."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
import numpy as np
data=np.load(file_path)
data_mean=np.mean(data,axis=0)
data_std=np.std(data,axis=0)
unit_variance=np.var(data,axis=0)
# Standardization means:
# standardized data=
# data−mean/standard deviation
standard_ver=data-data_mean/data_std
print(standard_ver)