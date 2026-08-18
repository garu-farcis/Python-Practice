"""13. Load students.npy. Create a one-hot encoded version of the gender column (shape (50, 2))
 Then horizontally stack the original age and
score columns with this one-hot matrix to obtain a final feature matrix of shape (50, 4)."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
data=np.load(file_path)
print(data.shape)
gender_d=data[:,2]
print(gender_d)
one_hot=np.eye(2)[gender_d.astype(int)]
print(one_hot)
og_age=data[:,0]
scores=data[:,1]
new_stack=np.column_stack((og_age.astype(int),scores.astype(float)))
res=np.hstack((new_stack,one_hot))
print(res)
