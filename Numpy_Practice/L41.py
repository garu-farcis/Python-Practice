"""6. Load sensor_readings.npy. Reshape it into a 2D array of shape (20, 10).
Compute the row-wise sum and the column-wise mean.
 Create a new array that subtracts the column mean from every element (centering)."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
data=np.load(file_path)
new_data=data.reshape(20,10)
print(new_data)
row_wise=np.sum(new_data,axis=1)
col_wise=np.average(new_data,axis=0)
print(row_wise,col_wise)
print(col_wise.shape)
sub_arr=np.subtract(new_data,col_wise)
print(sub_arr)