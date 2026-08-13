"""1. Load sensor_readings.npy. Compute a 5-bin histogram of the values.
Return both the counts and the bin edges. Then calculate the percentage of values that fall into the middle bin."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
data=np.load(file_path)
print(data.shape)
counts,bin_edges=np.histogram(data,5)
print(f"histogram 5 bins is {bin_edges}")
print(f"histo counts is {counts}")
mid_index=len(counts)//2
mid_vals=counts[mid_index]
perc=(mid_vals/(len(data)))*100
print(f"percentage is {perc}%")