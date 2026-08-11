"""7. Load temperatures.npy. Replace all values below 20 with the value 20 and
 all values above 30 with the value 30 (clipping).
Then count how many values were originally outside the [20, 30] range."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
data=np.load(file_path)
outside_range = (data < 20) | (data > 30)
count_num=np.sum(outside_range)
data[data<20]=20
data[data>30]=30
print(data)
range_num=[20,30]
print(count_num)