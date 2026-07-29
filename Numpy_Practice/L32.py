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
