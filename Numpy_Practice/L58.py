"""8. Load students.npy. Create a 2D array of shape (2, 3) that stores:
for each gender (0 and 1) the min, mean, and max of the score column.
Use advanced indexing or boolean masks, no explicit loops."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
data=np.load(file_path)
print(data.shape)
gender_data=data[:,2]
print(gender_data)
gender_0=gender_data==0
gender_1=gender_data==1
score_data=data[:,1]
print(score_data)

twod = np.array([
    [
        np.min(score_data[gender_0]),
        np.mean(score_data[gender_0]),
        np.max(score_data[gender_0])
    ],
    [
        np.min(score_data[gender_1]),
        np.mean(score_data[gender_1]),
        np.max(score_data[gender_1])
    ]
])
print(twod.reshape(2,3))