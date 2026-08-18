"""6. Load sensor_readings.npy. Create a boolean mask for values that
 are local minima (smaller than both immediate neighbors).
Return the indices of all local minima and the corresponding values."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
data=np.load(file_path)
print(data.shape)