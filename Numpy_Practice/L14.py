"""1. Array Creation
Create a 1D array arr from the list [10, 20, 30, 40, 50]. Then create:

A 3x3 array of all zeros
A 2x4 array of all ones
A 5x5 identity matrix

Print their shapes and data types."""
import numpy as np
from numpy.linalg import inv,qr
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.intersect1d(values, [2, 3, 6]))
X = np.random.default_rng().standard_normal((5, 5))
mat = X.T @ X
print(inv(mat),mat @ inv(mat))

L=[10, 20, 30, 40, 50]
my_arr=np.array(L)
print(np.zeros((3,3)))
print(np.ones((2,4)))
print(np.eye(5))

"""2. Basic Attributes & Properties
Given arr = np.arange(12).reshape(3, 4), print:

Number of dimensions (ndim)
Shape
Total elements (size)
Data type (dtype)
Item size in bytes

3. Indexing & Slicing
Using arr = np.arange(1, 13).reshape(3, 4):

Extract the element at row 1, column 2
Extract the first two rows
Extract the last column
Extract the sub-array [[5,6], [9,10]]"""
arr = np.arange(12).reshape(3, 4)
print(arr.ndim,arr.shape,arr.size,arr.dtype)

arr1 = np.arange(1, 13).reshape(3, 4)
print(arr1)
print(arr1[1,2])
print(arr1[1],arr1[0])
print(arr1[:2])
print(arr1[:,-1])
mask = np.isin(arr1, [5, 6, 9, 10])
print(arr1[mask])

"""4. Arithmetic Operations
Create two arrays:
Pythona = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
Perform element-wise addition, subtraction, multiplication, and division. Also compute a ** 2 and np.sqrt(a).
5. Aggregation Functions
For arr = np.random.randint(1, 100, size=(4, 5)):

Compute sum, mean, median, min, max of the entire array
Compute sum along axis=0 (column-wise) and axis=1 (row-wise)"""

