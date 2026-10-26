"""7. Load weather_stations.npy.
   Replace every rainfall value that is an outlier (more than 2.5 standard deviations above the mean) with the median rainfall.
   After replacement, recompute the correlation between rainfall and humidity.
   Report both the number of outliers replaced and the new correlation value."""
import numpy as np

from Numpy_Practice.L76 import rainfall

filepath="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
data=np.load(filepath)
rainfall=data[:,4]
mean_rain=np.mean(rainfall)
std_rain=np.std(rainfall)
median_rain=np.median(rainfall)
mask=rainfall> (2.5*std_rain+mean_rain)
new_rainfall=np.where(mask,median_rain,data[:,4])
print(new_rainfall)
humidity=data[:,1]
corelation=np.corrcoef(new_rainfall,humidity)[0,1]
no_outliers=np.sum(mask)

print(corelation,no_outliers)

