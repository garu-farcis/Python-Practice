"""11. Load temperatures.npy. Compute the correlation matrix between the 12 months (shape 12×12).
Extract the upper triangle (excluding the diagonal) and find the pair of months with the highest absolute correlation."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
arr=np.load(file_path)
corr_matrix=np.corrcoef(arr,rowvar=False)
print(corr_matrix)
print(corr_matrix.shape)
# upp_tri=np.tri(12,12,k=0)
upp_tri=np.triu(corr_matrix,k=1)
print(upp_tri)
high_pair=np.argmax(np.abs(corr_matrix))
print(high_pair,corr_matrix[high_pair])
