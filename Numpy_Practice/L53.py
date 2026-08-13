"""3. Load students.npy. Using boolean indexing, create a new array that contains
only the rows where age is between 20 and 22 (inclusive) AND score > 65. Report the shape of the resulting filtered array."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
data=np.load(file_path)
val=[20,22]
age_data=data[:,0]
score_data=data[:,2]
print(age_data)
mask=((age_data<=22) & (age_data>=20) & (score_data>65))
filt=data[mask]
print(filt,filt.shape)

