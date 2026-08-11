"""8. Load students.npy.columns: age, score, gender
 Split the array into two groups based on the gender column (0 and 1).
 Compute the mean score for each gender group without using loops."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
data=np.load(file_path)
gender_col=data[:,2]
score_data=data[:,1]
group1=score_data[gender_col==0]
group2=score_data[gender_col==1]
group1_mean=np.mean(group1)
group2_mean=np.mean(group2)
print(group1_mean,group2_mean)
# score_data=data[:,1] 
