"""7. Load weather_stations.npy.
   Replace every rainfall value that is an outlier (more than 2.5 standard deviations above the mean) with the median rainfall.
   After replacement, recompute the correlation between rainfall and humidity.
   Report both the number of outliers replaced and the new correlation value."""
import numpy as np
filepath="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"


