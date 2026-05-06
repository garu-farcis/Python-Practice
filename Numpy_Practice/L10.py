"""1. Array Creation & Basic Properties
Create a NumPy array from the list [10, 20, 30, 40, 50]. Then print its shape, dtype, and number of dimensions.
2. Element-wise Operations
Given a NumPy array arr = np.array([1, 2, 3, 4, 5]), create a new array where each element is squared
and then add 10 to every element. Do it in a single line using vectorization."""
import numpy as np

lst=[10, 20, 30, 40, 50]
arr=np.array(lst)
print(np.array(lst))
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5])
print((arr*10)+10)

"""3. Boolean Masking & Filtering
Create a NumPy array of 20 random integers between 0 and 100. Use boolean indexing to extract all values greater than 50.
4. Statistical Computations
Given a 1D array of 100 random floats, compute and print: mean, median, standard deviation, minimum, and maximum."""

arr=np.random.default_rng().integers(0,100,size=(3,5))
print(arr)
print(arr[arr>50])

one_d=np.random.rand(100)
print(one_d)
print(one_d.dtype)
print('max',one_d.max())
print('min',one_d.min())
print('mean',one_d.mean())
print('median',np.median(one_d,axis=0))
print('standard deviation', np.std(one_d,axis=0))


"""
5. 2D Array Operations
Create a 2D NumPy array of shape (5, 4) filled with random integers (10 to 99).

Compute the sum of each row
Compute the sum of each column

6. Reshaping & Flattening
Create a 1D array with 12 elements. Reshape it into (3, 4) and then flatten it back to 1D using two different methods (flatten() and ravel()). Explain the difference."""



two_d=np.random.default_rng().integers(10,99,size=(5,4))
print(two_d)
print('col sum',two_d.sum(axis=0))
print('row sum',two_d.sum(axis=1))

my_oned=np.arange(12)
print(my_oned)
x= my_oned.reshape(3,4)
print(x)
y= my_oned.ravel()
print(y)

"""7. Array Concatenation
Create two arrays: A = np.arange(5) and B = np.arange(5, 10).
Concatenate them both horizontally and vertically.
8. Indexing & Slicing
Given a 2D array of shape (6, 6) filled with numbers 0 to 35, extract:
start = n//2 - 1
end   = n//2 + 2 
for center 
The center 3x3 subarray
Every second element of the last row"""


A = np.arange(5)
B = np.arange(5, 10)
print(np.hstack((A,B)))
print(np.vstack((A,B)))


two_d=np.random.default_rng().integers(0,35,size=(6,6))
print(two_d)
print(two_d[5,0:5])
center = two_d[2:5, 2:5]
print(center)

"""9. Replacing Values with Conditions
Create a 1D array of 15 random integers (0-50). Replace all values less than 20 with 0 and all values greater than 40 with 99 — in a vectorized way.
10. Broadcasting
Create a 2D array of shape (4, 5) and a 1D array of shape (5,). Add the 1D array to each row of the 2D array using broadcasting. Show the result."""


oned=np.random.default_rng().integers(0,50,size=(15,))
print(oned)
oned=[0 if i<20  else i for i in oned ]
print(oned)
oned=[99 if i>40  else i for i in oned]
print(oned)

oned_d=np.arange(5)
twod=np.random.default_rng().integers(0,10,size=(4,5))

print(twod+oned_d)

"""11. Sorting & Argsort
Given a 1D array, sort it in descending order. Also return the original indices of the sorted values (use argsort).
12. Handling Missing Values
Create a 1D array with some np.nan values.

Count how many NaNs are present
Replace all NaNs with the mean of the non-NaN values"""

L=np.random.rand(7)
print(L)
print(np.argsort(L,axis=0,kind='Q'))

arr =np.empty(20)
arr[:]=np.nan
print(arr)

x = np.array([1, 2, np.nan, 4])
print(np.isnan(x).sum())
mean_val=np.nanmean(x)
x[np.isnan(x)]=mean_val
print(x)
# uniques,counts=np.unique(x,return_counts=True)
# print(uniques,counts)
# for each in x:
#     if np.isnan(each):
#         each=0
# print(x)

"""13. Matrix Multiplication
Create two 2D arrays: one (3, 4) and another (4, 2). Perform matrix multiplication using the appropriate operator.

14. Percentiles & Quantiles
Generate 1000 random numbers from a normal distribution. Find the 25th, 50th (median), and 75th percentiles.

15. Data Normalization
Given a 2D array of shape (100, 5) with random values, normalize each column so that it has:

Mean = 0
Standard deviation = 1
(Use vectorized operations only)"""

one=np.random.default_rng().integers(0,100,size=(3,4))
two=np.random.default_rng().integers(0,100,size=(4,2))
print(one)
print(two)
print(np.dot(one,two))

import numpy as np

# 1. Generate 1000 random numbers from a normal distribution
data = np.random.randn(1000)  # mean=0, std=1

# 2. Compute percentiles
p25 = np.percentile(data, 25)
p50 = np.percentile(data, 50)  # median
p75 = np.percentile(data, 75)

print("25th percentile:", p25)
print("50th percentile (median):", p50)
print("75th percentile:", p75)


# create data
X = np.random.rand(100, 5)

# compute column-wise mean and std
mean = X.mean(axis=0)
std = X.std(axis=0)

# normalize
X_norm = (X - mean) / std
print(X_norm)