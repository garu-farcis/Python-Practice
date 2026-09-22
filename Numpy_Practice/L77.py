# 3. Load weather_stations.npy.
# Find the day (row index) with the highest “discomfort index” defined as: temp_c + 0.1 * humidity_pct - 0.05 * wind_speed_ms.
# Return the full row of that day.

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
import numpy as np
data=np.load(file_path)
temp_c=data[:,0]
humidity_pct=data[:,1]
wind_speed_ms=data[:,3]
discomfort_index=temp_c + 0.1 * humidity_pct - 0.05 * wind_speed_ms
max_index=np.argsort(discomfort_index)[-1]
print(max_index)
full_day=data[max_index,:]
print(full_day)

