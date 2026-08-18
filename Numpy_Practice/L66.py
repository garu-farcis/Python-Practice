"""Load students.npy. Using boolean masks, count how many students satisfy
each of the following conditions simultaneously:
   - age ≥ 21
   - score between 60 and 85 (inclusive)
   - gender == 1
   Return only the final count."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
data=np.load(file_path)
print(data.shape)
age=data[:,0]
score=data[:,1]
gender=data[:,2]
mask=((age>=21) & ((score>=60)& (score<=85))&(gender==1))
final_count=np.sum(mask)
print(final_count)