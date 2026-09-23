# 8. Load sensor_signals.npy. Reshape / treat the data as 60 samples.
# Create a new feature that is the mean of all 8 channels at each time step,
# then horizontally stack this new feature to the original array (final shape should be (60, 9)).

import  numpy as np
file_p="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
data=np.load(file_p)
print(data.shape)
new_feature=np.apply_along_axis(lambda x:np.mean(x),axis=1,arr=data)
new_stack=np.hstack([new_feature[:,np.newaxis],data])
