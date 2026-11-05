"""4. Create a boolean mask for rows where temperature > 25 AND humidity < 50.
   Use this mask (boolean indexing) to extract those rows. Then apply the ufunc np.sqrt
   to the vibration column of the filtered data."""

import numpy as np
data=np.load("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_log.npy")
mask=(data[:,1]>25) and (data[:,1]<50)
extract=data[mask]