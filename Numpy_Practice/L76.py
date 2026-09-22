# 2. Load weather_stations.npy.
# Create a boolean mask for “rainy & windy” days (rainfall_mm > 5 and wind_speed_ms > 6).
# Count how many such days exist and extract the temperature values of those days.


file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
import numpy as np
data=np.load(file_path)
print(data.shape)
rainfall=data[:,4]
wind_speed=data[:,3]
mask= (rainfall>5 ) & (wind_speed>6)
filter_data=data[mask]
such_days=np.sum(mask)
temp_vals=filter_data[:,0]
print(such_days,temp_vals)