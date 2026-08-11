"""3. Load students.npy (columns: age, score, gender).
Create a boolean mask for students with score > 75.
Using fancy indexing, extract only the ages of those high-scoring students and compute their mean age."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
data=np.load(file_path)
mask=data[:,1]>75
print(mask)
ages=data[mask,0]
mean_age=np.mean(ages)
print(f"mean age is {mean_age}")