"""Array attributes"""

import numpy as np
L= [23,34,22,55,142,533,533,53556,23,45553,536,667,786,8788,86]
L1=[76,54,8567,36,65,74,93,74,65,92]
my_arr= np.array(L)
print(my_arr)
# dimension
print(my_arr.ndim)
# shape
print(my_arr.shape)
# size
print(my_arr.size)
# data type
print(my_arr.dtype)
print('reshape  ',my_arr.reshape(3,5))

"""How to create a basic array
 np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()
"""
zero_arr=np.zeros(10)
print(zero_arr)
print(np.ones(10))
print(np.arange(10))

print(np.linspace(0,10,num=9))

# generate 2d array
# Random values
print(np.random.seed(42)   )                 # for reproducibility
arr5 = np.random.rand(3, 4)           # 3x4 array with random floats (0 to 1)
arr6 = np.random.randint(1, 100, size=(5, 3))  # random integers
print(arr5)
print(arr6)
# Sequential numbers
arr7 = np.arange(12).reshape(3, 4)    # Very useful!
print(arr7)

# Evenly spaced values
arr8 = np.linspace(0, 10, 6).reshape(2, 3)
print(arr8)

# 1. Empty 2D array (recommended way)
matrix = np.zeros((5, 5))
print(matrix)

# 2. Identity matrix
identity = np.eye(4)                  # 4x4 identity matrix
print(identity)

# 3. From existing 1D array
a = np.array([1, 2, 3, 4, 5, 6])
matrix = a.reshape(2, 3)

print(matrix)

"""Adding, removing, and sorting elements
np.sort(), np.concatenate()
argsort, which is an indirect sort along a specified axis,

lexsort, which is an indirect stable sort on multiple keys,

searchsorted, which will find elements in a sorted array, and

partition, which is a partial sort.
"""
print(np.sort(my_arr,axis=0,kind='Q'))
print(np.concatenate((L,L1),axis=0, out=None))
print(np.argsort(L,axis=0,kind='M',order= None))
print(matrix)
print(np.lexsort(matrix,axis=0))
# numpy.searchsorted(a, v, side='left', sorter=None)
print(np.searchsorted(L1,L,side='right'))
print(np.partition(L,7))
# np.where (if condition, result, else this result)
print(np.where(my_arr%2==0,my_arr,my_arr*1000))
# np.extract(condition to extract, the array from where you extract)
print(np.extract(my_arr%2!=0,my_arr))

import numpy as np
arr = np.arange(12).reshape((3, 4))
condition = np.mod(arr, 3)==0
print(condition)
print(np.extract(condition, arr))

print(np.nonzero(np.ravel(arr7))[0])
print(np.flatnonzero(arr6))
x=arr6
print(x.ravel()[np.flatnonzero(x)])
print(np.argwhere(my_arr),np.argwhere(arr8))
x = np.arange(6).reshape(2,3)
print(x)
print('        ',np.argwhere(x>1))



"""How to convert a 1D array into a 2D array (how to add a new axis to an array)"""
L= [23,34,22,55,142,533,533,53556,23,45553,536,667,786,8788,86]
print(len(L))
my_arr=np.array(L)
print(my_arr.shape)
L1=[76,54,8567,36,65,74,93,74,65,92]
my_d=my_arr[np.newaxis, :]
print(my_d.shape)
my_d=my_arr[:, np.newaxis]
print(my_d.shape)
# my_d.reshape(3,5)
# using expand dims axis =1 for cols and 0 for rows

my_d=np.expand_dims(my_arr,axis=1)
print(my_d.shape)
my_d=np.expand_dims(my_arr,axis=0)
print(my_d.shape)

"""Indexing and slicing"""

L= [23,34,22,55,142,533,533,53556,23,45553,536,667,786,8788,86]
print(len(L))
my_arr=np.array(L)
print(my_arr[my_arr%2==0])
print(my_arr[my_arr>1909])
print(my_arr[(my_arr>500) & (my_arr<1000)])
#  add condition on top of nonzero conditions directly
print(np.nonzero(my_arr<1000))

"""How to create an array from existing data"""
a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = a[3:8]
print(arr1)
a1 = np.array([[1, 1],
               [2, 2]])
a2 = np.array([[3, 3],
               [4, 4]])
print(np.vstack((a1, a2)))
print(np.hstack((a1,a2)))
print(np.hsplit(a1,2))
print(np.vsplit(a1,2))

print(np.random.rand(3,3))
print(np.random.randint(4))
# create any random number numpy array
rng = np.random.default_rng()
print(rng.random(4))
print(rng.integers(2,10,size=(3,5)))
# removes dups
print(np.unique(my_arr))
uni_val, indexes,my_counts=np.unique(my_arr, return_index=True,return_counts=True)
print(uni_val,indexes,my_counts)


"""Transposing and reshaping a matrix"""
rng=np.random.default_rng()
# myarr= rng.random(6)
myarr=rng.integers(0,100,size=(5,6))
print(myarr)
print(myarr.reshape(3,10))
print(myarr.ravel())
print(myarr.transpose())
# flip is to reverse a array
print(np.flip(myarr,axis=0))
myarr[1]=np.flip(myarr[1],axis=0)
print(myarr)
print(myarr.flatten())
arr9=np.array(myarr.flatten())
print(arr9.reshape(6,5))
x=arr9.reshape(6,5)
np.save('testfile',arr9.reshape(6,5))
val= np.load('testfile.npy')
print('my val:......',val)
np.savetxt('mycsv.csv',x,delimiter=',')
print('my csv:.................',np.loadtxt('mycsv.csv', delimiter=','))

from io import StringIO

s = StringIO("1,1.3,abcde")
data = np.genfromtxt(s, dtype=[('myint','i8'),('myfloat','f8'),
('mystring','S5')], delimiter=",")
print(data)
print(np.ndarray.tolist(x))
print(np.array2string(x))


import pandas as pd
txt=pd.read_csv('mycsv.csv',header = None)
print(txt)
df =pd.DataFrame(txt)
print(df)
df.to_csv('mycsv_pandas.csv')

import matplotlib.pyplot as plt
# matplotlib inline
plt.plot(x)
plt.show()
#  x and y must have same dimensions , num should be equal 
x1=np.linspace(0,100,20)
y1=np.linspace(1,38,20)
plt.plot(x1,y1,'purple')
plt.show()