"""Load weather_stations.npy.
   Create a new derived feature called "heat_index" using the formula:
   heat_index = temp_c + 0.33*humidity_pct - 0.70*wind_speed_ms - 4.0
   Then find all days where heat_index > 25 AND rainfall_mm < 1.
   Return the mean pressure of those days and the number of such days"""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
data=np.load(file_path)
temp_c=data[:,0]
humidity_pct=data[:,1]
wind_speed_ms=data[:,3]
rainfall_mm=data[:,4]
heat_index=data[:,np.newaxis]
heat_index=temp_c + 0.33*humidity_pct - 0.70*wind_speed_ms - 4.0
mask=(heat_index>25)&(rainfall_mm < 1)
filt_data=data[mask]
mean_pressure=np.mean(filt_data[:,2])
num_of_days=len(filt_data)
print(mean_pressure,num_of_days)