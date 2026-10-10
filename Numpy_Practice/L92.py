"""Load both datasets.
    From weather_stations take the temperature column.
    From sensor_signals take the mean across all 8 channels at each time step (producing a 60-length series).
    Resample / interpolate the longer series (temperature) down to length 60 using simple linear interpolation (you may use np.interp).
    Finally compute the Pearson correlation between the two resulting length-60 serie"""


import numpy as np

file="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
data_1=np.load(file)
data_2=np.load(file_path)
print(data_1.shape)
print(data_2.shape)
temp_c=data_1[:,0]
mean_across_time =