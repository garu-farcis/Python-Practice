"""13. Load students.npy. Create a new column (as a separate array) that is 1 if score ≥ 70 else 0.
Then use np.bincount or unique + counts to get the class distribution of this binary label."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
arr=np.load(file_path)
print(arr.shape)
# new_col=arr[]
score_data=arr[:,1]
print(score_data)
new_col=(score_data>=70).astype(int)
# for i in range(len(score_data)):
#     if score_data[i]>=70:
#         score_data[i]=1
#     else:
#         score_data[i]=0
print(new_col)

# print(arr)
# np.ravel(score_data)
class_dist=np.bincount(new_col)
print(class_dist)