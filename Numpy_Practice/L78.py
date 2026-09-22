# 4. Load sensor_signals.npy. Compute the correlation matrix between the 8 channels (shape 8×8).
# Extract the upper triangle (excluding diagonal) and find the pair of channels with the strongest absolute correlation.

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
import numpy as np
data=np.load(file_path)
print(data.shape)
correlation_mat=np.corrcoef(data,rowvar=False)
print(correlation_mat)
upper=np.triu(correlation_mat,k=1)
print(upper)