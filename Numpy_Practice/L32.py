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
