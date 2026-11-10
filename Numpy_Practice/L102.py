"""5. Using broadcasting, divide every column by its own maximum value (scale each column
   to the range [0, 1]). After scaling, compute the sum of each row with aggregation.
"""

import numpy as np
data=np.load("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_log.npy")
# temp=data[:,0]
# temp_max=max(data[:,0])
# print(temp_max)
# humidity=data[:,1]
# humi_max=max(data[:,1])
# press=data[:,2]
# press_max=max(data[:,2])
# wind_sp=data[:,3]
# wind_sp_max=max(data[:,3])
# voltage=data[:,4]
# volt_max=max(data[:,4])
# curr=data[:,5]
# curr_max=max(data[:,5])

x_normed = data / np.max(data,axis=0)
print(x_normed)
