"""1. Load sensor_readings.npy. Compute the 10th, 50th and 90th percentiles.
Then create a boolean mask for values that are more than 1.5 standard deviations away from the mean and count how many outliers exist."""

import numpy as np
import pandas as pd
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
data= np.load(file_path)
print(data)
ten_perc=np.percentile(data,10)
fifty_perc=np.percentile(data,50)
ninty_perc=np.percentile(data,90)
std=np.std(data)
d_std=1.5*std
d_mean=np.mean(data)
mask = np.abs(data - d_mean) > (1.5 * std)
outlier_count = np.sum(mask)
print(outlier_count)

