"""5. Using broadcasting, divide every column by its own maximum value (scale each column
   to the range [0, 1]). After scaling, compute the sum of each row with aggregation.
"""

import numpy as np
data=np.load("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_log.npy")
temp_max=max(data[:,0])
print(temp_max)

