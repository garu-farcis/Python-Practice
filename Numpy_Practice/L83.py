# 9. Load weather_stations.npy.
# Sort the rows by rainfall_mm in descending order.
# After sorting, compute the mean temperature of the top 15 rainiest days.

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
import numpy as np
data=np.load(file_path)
rainfall=data[:,4]
sort_d_index=np.argsort(rainfall)
sorted_desc=sort_d_index[::-1]
temp=data[sorted_desc[:15],0]
print(temp.shape)
top_mean=np.mean(temp)
print(top_mean)
