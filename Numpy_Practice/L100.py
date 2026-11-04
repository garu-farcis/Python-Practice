"""3. Using slicing, create a view of every 5th row starting from index 10 up to index 600.
   On this sliced view, compute the row-wise sum and the column-wise mean using aggregation."""

import numpy as np
data=np.load("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_log.npy")
my_view=data[5,::5]
print(my_view)