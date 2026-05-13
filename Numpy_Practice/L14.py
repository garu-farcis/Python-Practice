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
Python a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
Perform element-wise addition, subtraction, multiplication, and division. Also compute a ** 2 and np.sqrt(a).
5. Aggregation Functions
For arr = np.random.randint(1, 100, size=(4, 5)):

Compute sum, mean, median, min, max of the entire array
Compute sum along axis=0 (column-wise) and axis=1 (row-wise)"""

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a+b)
arr = np.random.randint(1, 100, size=(4, 5))
print(arr.mean(),arr.max(),np.median(arr))
print(arr.sum(axis=0),arr.sum(axis=1))

"""6. Boolean Indexing
Create arr = np.array([10, 15, 20, 25, 30, 35, 40]).
Extract all elements that are greater than 20 and even.
7. Reshaping & Transposing
Create a 1D array of 20 elements using np.arange.
Reshape it to (4, 5), then to (2, 2, 5). Finally, transpose the (4, 5) version.
8. Concatenation & Stacking
Create a = np.zeros((3, 4)) and b = np.ones((3, 4)).

Stack them vertically (vstack)
Stack them horizontally (hstack)
Concatenate along axis=0 and axis=1"""
arr = np.array([10, 15, 20, 25, 30, 35, 40])
x=(((arr>20) & (arr%2==0)).any())
print(x)
filtered = arr[(arr > 20) & (arr % 2 == 0)]
print(filtered)

one_d=np.arange(20)
print(one_d.reshape(4,5),one_d.reshape(2,2,5),one_d.transpose())
x=one_d.reshape(4,5)
print(x)
print(np.transpose(x))

"""9. Broadcasting
Create a 4x3 array A and a 1D array b of length 3.
Add b to every row of A without using loops. Explain how broadcasting works here.
10. Fancy Indexing & Advanced Slicing
Create a 5x5 array of random integers.

Select rows 0, 2, and 4
Select elements at positions (0,1), (2,3), (4,0) using fancy indexing
Replace all values greater than 50 with 0"""

a=np.random.default_rng().integers(0,100,size=(4,3))
b=np.arange(3)
print(a+b)
a=np.random.default_rng().integers(0,100,size=(5,5))
selected=a[[0,2,4]]
print(selected)
print(np.where(selected>50,0,selected))
selct_1=a[[(0,1), (2,3), (4,0)]]
print('list of tuples ', selct_1)
print(np.where(selct_1>50,0,selct_1))
selct_1 = a[[0,2,4], [1,3,0]]
print(selct_1)

"""11. Universal Functions (ufuncs)
Given angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2]), compute sin, cos, and exp of these values.
Also demonstrate np.add, np.maximum, and np.divide on two arrays.
12. Sorting & Searching
Create a 2D array (5x4) of random numbers.

Sort each row
Sort each column
Find the indices that would sort the flattened array (argsort)
Find positions where values > mean of the array"""

angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
print(np.add(angles,angles[::-1]))
print(np.sin(angles),np.cos(angles),np.exp(angles))
print(np.maximum(angles,angles[::-1]))
# print(np.divide(angles,angles[::-1]))
a=np.random.default_rng().integers(0,100,size=(5,4))
row_sorted = np.sort(a, axis=1)
col_sorted = np.sort(a, axis=0)
print(row_sorted,col_sorted)
flat_arr=a.ravel()
print(flat_arr)
print(np.argsort(flat_arr))
my_mean=flat_arr.mean()
sorted_flat = np.sort(flat_arr)
print(np.searchsorted(sorted_flat,my_mean))
positions = np.where(flat_arr > my_mean)[0]
print("\nPositions where values > mean:")
print(positions)
positionss = np.nonzero(flat_arr)[0]
print(positionss)


"""3. Linear Algebra Basics
Create two 3x3 matrices A and B.

Compute matrix multiplication (@ or np.dot)
Compute inverse of A (if invertible)
Compute determinant of A
Solve the system Ax = b where b is a vector of ones"""
A=np.random.default_rng().integers(0,100,size=(3,3))
print(A)
B=np.random.default_rng().integers(0,100,size=(3,3))
print(B)
print(A@B)
print(A.__invert__())
print(np.linalg.inv(A))
print(np.linalg.det(A))
b=np.ones((3,3))
res=np.linalg.solve(A,b)
print(res)

"""14. Random Number Generation & Statistics
Set seed to 42. Generate:

1000 samples from standard normal distribution
A 10x10 array from uniform distribution [0, 1)
Compute mean, std, and correlation matrix of a 100x5 random normal dataset

15. Real-world Mini Project: Image-like Processing
Create a 100x100 grayscale "image" (array) with a bright square in the center.

Add Gaussian noise
Clip values between 0 and 255
Compute row-wise and column-wise means
Apply a simple threshold to create a binary mask"""

rng = np.random.default_rng(42)
myarr=rng.standard_normal(1000)
uni_matrx=rng.random((10,10))
data = rng.standard_normal((100, 5))
mean_values = data.mean(axis=0)
print("Mean:\n", mean_values)
std_values = data.std(axis=0)
print("Std Dev:\n", std_values)
corr_matrix = np.corrcoef(data, rowvar=False)
print("Correlation Matrix:\n", corr_matrix)
A = np.ones((2, 2))

B = np.eye(2, 2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))
print(A,'\n      ',B,'\n      ',C,'\n      ',D)
E=np.block([[A, B], [C, D]])
print(np.block([[A, B], [C, D]]))
