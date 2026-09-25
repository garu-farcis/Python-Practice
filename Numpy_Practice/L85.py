"""1. Load weather_stations.npy.
   Create a new derived feature called "heat_index" using the formula:
   heat_index = temp_c + 0.33*humidity_pct - 0.70*wind_speed_ms - 4.0
   Then find all days where heat_index > 25 AND rainfall_mm < 1.
   Return the mean pressure of those days and the number of such days."""

# file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"

import numpy as np
data=np.load(file_path)
temp_c=data[:,0]
humidity_pct=data[:,1]
wind_speed_ms=data[:,3]
rainfall_mm=data[:,4]
heat_index=data[:,np.newaxis]
heat_index=temp_c + 0.33*humidity_pct - 0.70*wind_speed_ms - 4.0
# print(data)
mask=(heat_index > 25) & (rainfall_mm < 1)
res=data[mask]
res_mean=np.mean(res[:,2])
res_count=np.sum(mask)
# print(res)
print(res_mean)
print(res_count)
