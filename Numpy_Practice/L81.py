# 7. Load weather_stations.npy. Clip all temperature values to the range [5, 30]
# and all rainfall values to [0, 25]. Count how many values were changed by the clipping operation.

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
import numpy as np
data=np.load(file_path)
print(data.shape)
temp_vals=data[:,0]
rain_vals=data[:,4]
t_c=np.clip(temp_vals,5,30)
r_c=np.clip(rain_vals,0,25)
count_t = np.sum(temp_vals != t_c)
count_r = np.sum(rain_vals != r_c)
print(t_c,r_c,count_r,count_t)