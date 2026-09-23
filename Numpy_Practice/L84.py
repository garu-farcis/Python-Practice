# 10. Load both datasets. Randomly select 40 row indices from weather_stations and 40 row indices from sensor_signals (independent sampling).
# Extract the first column of each selected subset and compute the Pearson correlation between the two extracted 1D series.

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
file_path1="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"

import numpy as np
data=np.load(file_path)
data1=np.load(file_path1)
sensor_indices = np.random.choice(data.shape[0], size=40, replace=False)
weather_indices = np.random.choice(data1.shape[0], size=40, replace=False)
frst_col_sensor=data[:,0]
frst_col_weather=data1[:,0]
pearson_coef=np.corrcoef(frst_col_sensor[sensor_indices],frst_col_weather[weather_indices])[0,1]