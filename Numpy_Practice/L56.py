"""6. Load sensor_readings.npy. Reshape it into shape (10, 20).
Apply a row-wise z-score normalization (subtract row mean and divide by row std).
Handle any row that has zero standard deviation by leaving it unchanged."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_readings.npy"
data=np.load(file_path)
print(data.shape)
arr=data.reshape(10,20)
print(arr)
row_mean=np.mean(arr,axis=1,keepdims=True)
row_std=np.std(arr,axis=1,keepdims=True)
score=row_std-row_mean
z_score=arr.copy()
valid_rows = row_std != 0
# z_score[valid_rows[:,0]]=(arr[valid_rows[:,0]]-row_mean[valid_rows[:,0]])/row_std[valid_rows[:,0]]
z_score[valid_rows[:, 0]] = (
    arr[valid_rows[:, 0]] - row_mean[valid_rows[:, 0]]
) / row_std[valid_rows[:, 0]]
print(f"z score is {z_score}")
