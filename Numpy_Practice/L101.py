"""4. Create a boolean mask for rows where temperature > 25 AND humidity < 50.
   Use this mask (boolean indexing) to extract those rows. Then apply the ufunc np.sqrt
   to the vibration column of the filtered data."""

import numpy as np
data=np.load("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_log.npy")
temp=data[:,1]
humi=data[:,2]
mask=(temp>25) and (humi<50)
extract=data[mask]
res=np.sqrt(extract[:,7])
print(res)