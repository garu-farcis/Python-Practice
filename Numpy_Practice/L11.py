"""9. Broadcasting
Create a 4x3 array A and a 1D array b of length 3.
Add b to every row of A without using loops. Explain how broadcasting works here.

10. Fancy Indexing & Advanced Slicing
Create a 5x5 array of random integers.

Select rows 0, 2, and 4
Select elements at positions (0,1), (2,3), (4,0) using fancy indexing
Replace all values greater than 50 with 0"""
import numpy as np
L=np.random.rand(4,3)
L1=np.arange(3)
print(L+L1)

arr= np.random.default_rng().integers(0,100,size=(5,5))
print(arr)
print(arr[[0,2,4],[1,3,0]])

print(np.where(arr>50,0,arr))

"""11. Universal Functions (ufuncs)
Given angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2]), compute sin, cos, and exp of these values.
Also demonstrate np.add, np.maximum, and np.divide on two arrays.
y"""

angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
print(np.sin(angles),np.cos(angles),np.exp(angles))