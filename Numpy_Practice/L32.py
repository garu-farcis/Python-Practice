"""Create a 5x5 array of random integers between 10 and 50 (inclusive).
   Then extract the border (first/last rows and columns) into a new 1-D array
   without using loops.
   Sample expected shape of border array: (16,)"""

import numpy as np
arr=np.random.default_rng().integers(10,50,(5,5))
print(arr)
border = np.concatenate((arr[0,:],arr[1:-1, -1],arr[-1, ::-1],arr[-2:0:-1, 0]))
print(f"border array is {border}")


"""Given a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
   Use broadcasting to subtract the mean of each column from every element
   of that column. Do not use np.mean(..., axis=...) inside a loop.
   Sample result:
   [[-3. -3. -3.]
    [ 0.  0.  0.]
    [ 3.  3.  3.]]"""

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
col_sum = np.sum(a, axis=0)
col_mean1 = col_sum / a.shape[0]
col_mean = np.mean(a, axis=0)
result = a - col_mean
result1 = a - col_mean1
print(f"broadcasted array is {result}")
print(f"broadcasted array is {result1}")


"""Create a 1-D array of 20 random integers in [0, 9].
   Using boolean indexing, replace every even number with -1 and every
   multiple of 3 with 0 (multiples of 6 become 0).
   Sample input:  [4 7 2 9 0 5 6 1 8 3 ...]
   Sample output: [-1 7 -1 0 0 5 0 1 -1 0 ...]"""


# oned=np.random.default_rng().integers(0,9)
oned=np.random.randint(0,10,20)
even = (oned % 2 == 0)
multiple3 = (oned % 3 == 0)

oned[even] = -1
oned[multiple3] = 0

print(oned)

"""Given two arrays of the same length:
   x = np.array([1, 3, 5, 7, 9])
   y = np.array([2, 4, 6, 8, 10])
   Build a 2-D array that interleaves them column-wise:
   [[1 2]
    [3 4]
    [5 6]
    [7 8]
    [9 10]]
   Use only stacking / reshaping – no Python loops."""
x = np.array([1, 3, 5, 7, 9])
y = np.array([2, 4, 6, 8, 10])
a=[]
z=[(i,j) for i in x for j in y]
print(z)
res = np.column_stack((x,y))
print(res)

"""Create a 6x6 matrix filled with the numbers 0..35 in row-major order.
   Extract every other element of every other row using advanced indexing
   (fancy indexing) so the result is a 3x3 array:
   [[ 0  2  4]
    [12 14 16]
    [24 26 28]]"""

arr= np.random.default_rng().integers(0,35,(6,6))
print(arr)
print(arr[:,(0,1,2)])
result = arr[[0, 2, 4]][:, [0, 2, 4]]
print(result)

import numpy as np

arr = np.arange(36).reshape(6, 6)

print(arr)

result = arr[[0, 2, 4]][:, [0, 2, 4]]

print(result)

"""Given a = np.random.randn(4, 5)
   Compute the Euclidean norm of each row and of each column without using
   np.linalg.norm.  Return two 1-D arrays (row_norms, col_norms)."""

import numpy as np

a = np.random.randn(4, 5)

# Euclidean norm of each row
row_norms = np.sqrt(np.sum(a**2, axis=1))

# Euclidean norm of each column
col_norms = np.sqrt(np.sum(a**2, axis=0))

print("Array:")
print(a)

print("\nRow norms:")
print(row_norms)

print("\nColumn norms:")
print(col_norms)

"""Generate a 1-D array of 1000 standard-normal samples.
   Using only vectorized operations, compute the proportion of values that
   lie inside the interval [-1.96, 1.96] (approx. 95 % of a normal distribution).
   Sample expected value ≈ 0.95"""

dd=np.random.randn(1000)
proportion = np.mean(np.abs(dd) <= 1.96)
proportion = np.mean((x >= -1.96) & (x <= 1.96))
print(f"Proportion inside [-1.96, 1.96]: {proportion:.4f}")


"""Given two matrices A (3x4) and B (4x2) filled with random integers,
   compute the matrix product A @ B two different ways:
   (a) using the @ operator
   (b) using np.einsum
   Verify they are identical."""

matr1=np.random.default_rng().integers(0,100,(3,4))
matr2=np.random.default_rng().integers(0,100,(4,2))
prod=matr1@matr2
sum=np.einsum('ij, jk ->', matr1, matr2)
print(f"product is {prod}")

"""Create a sorted array of 15 unique random integers in [1, 50].
   Insert the value 25 into the correct sorted position using only
   np.searchsorted and np.insert (no Python sorting)."""

matr1=np.random.default_rng().integers(0,100,15)
print(matr1)
matr1.sort()
r=np.searchsorted(matr1,25)
res=np.insert(matr1,r,25)
# res=np.searchsorted(matr1,side="left")
print(f"result is {res}")


"""Given a 2-D array of shape (8, 6) filled with random floats,
    replace every element that is greater than the 75-th percentile of
    its own column by NaN.  Use broadcasting and np.percentile"""

arr=np.random.randn(8,6)
print(arr)
perc=np.percentile(arr,75,axis=0)
arr[arr>perc]=np.nan
print(arr)

"""Build a 5x5 Hilbert matrix H where H[i,j] = 1 / (i + j + 1)
    (0-based indices).  Then compute its condition number with
    np.linalg.cond.  Sample H[0,0] = 1.0, H[4,4] = 0.1"""

n = 5
i = np.arange(n).reshape(-1, 1)   # Column indices
j = np.arange(n)                  # Row indices

H = 1 / (i + j + 1)

print("Hilbert Matrix:")
print(H)
cond= np.linalg.cond(H)
print(f"condition {cond}")

"""Given a 1-D array of daily temperatures (length 30),
    compute a 7-day moving average using only convolution
    (np.convolve) with a uniform kernel.  The result should have length 24."""


d1=np.arange(30)
kernel = np.ones(7) / 7
res=np.convolve(d1,kernel,mode="valid")
print(f"convolved is {res}")


"""Create two arrays:
    a = np.array([1, 2, 3, 2, 4, 1, 5])
    b = np.array([2, 4, 6, 8])
    Using set-like NumPy functions, return:
    - elements that appear in both a and b
    - elements that appear only in a
    - elements that appear in either a or b (union)"""

a = np.array([1, 2, 3, 2, 4, 1, 5])
b = np.array([2, 4, 6, 8])
either= np.union1d(a,b)
uni=np.intersect1d(a,b)
onlya= np.setdiff1d(a,b)
print(f"elements that appear in both a and b {uni}, elements that appear only in a {onlya},elements that appear in either a or b (union) {either} ")

"""Given a 3-D array of shape (2, 3, 4) filled with consecutive integers
    starting from 0, reshape / transpose it so that the axes become
    (4, 2, 3) while preserving the original data order
    (i.e., the linear memory order stays the same)."""

d3=np.random.default_rng().integers(0,100,(2,3,4))
print(f"original is  {d3}")
redone=d3.reshape(4,2,3)
print(f"redone is {redone}")

"""Create a 10x10 matrix of random integers in [0, 9].
    For every row, find the index of the first occurrence of the maximum
    value in that row.  Return a 1-D array of those 10 indices
    (use np.argmax with the correct axis, no Python loops).
"""

a=np.random.default_rng().integers(0,10,(10,10))
print(a)
res=np.argmax(a,axis=1)
print(f"the result is {res}")



