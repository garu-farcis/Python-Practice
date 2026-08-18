"""15. Load sensor_readings.npy and temperatures.npy.
Randomly sample 40 indices (without replacement) from the length of sensor_readings.
 Use those indices to extract values from sensor_readings and also from the first column
 of temperatures (broadcast/truncate if needed). Compute the Spearman rank correlation
 between the two extracted series (you may use np.argsort to implement ranks manually)."""

import numpy as np

sensor_path = "/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
temp_path = "/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"

sensor = np.load(sensor_path)
temperatures = np.load(temp_path)

print(sensor.shape)
print(temperatures.shape)
n = min(len(sensor), len(temperatures))
indices = np.random.choice(n, size=40, replace=False)
sampled_sensor = sensor[indices]
sampled_temperatures = temperatures[:, 0][indices]

print("indices:", indices)
print("sensor:", sampled_sensor)
print("temperatures:", sampled_temperatures)