"""8. Load students.npy. Sort the entire array by the score column in descending order.
After sorting, extract the top 10 rows and compute the mean age of those top-scoring students."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.npy"
data=np.load(file_path)
print(data.shape)
sorted_indices = np.argsort(data[:, 1])[::-1]

soreted_col=data[sorted_indices]
print(soreted_col)
top_ten=soreted_col[:10]
print(top_ten)
mean_top=np.mean(top_ten)
print(mean_top)