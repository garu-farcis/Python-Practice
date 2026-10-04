"""Load weather_stations.npy.
   Bin the temperature column into 4 quantile-based bins (use np.quantile).
   For each temperature bin, compute the mean rainfall and mean wind speed.
   Return a (4, 2) array with these statistics"""
import numpy as np

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
data=np.load(file_path)
temp_c=data[:,0]
bins=np.quantile(temp_c,q=np.linspace(0,1,5))
print(bins)
rain=data[:,4]
wind=data[:,3]
bin_index=np.digitize(temp_c,bins[1:-1])
mean_rainfall=np.array([np.mean(rain[bin_index==i]) for i in range(4)])
mean_wind=np.array([np.mean(wind[bin_index==i]) for i in range(4)])

#     mean_rainfall=np.mean(data[:,4])
#     mean_wind=np.mean()
# x=np.concat([mean_rainfall,mean_wind])
# print(x)