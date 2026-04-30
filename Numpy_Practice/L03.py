"""Convert List to NumPy Array

Convert a Python list into a NumPy array and print its shape.

# Input: [1, 2, 3, 4, 5]
# Output: numpy array + shape (5,)"""

import numpy as np
from numpy import array
L=[1, 2, 3, 4, 5]
my_arr=np.array(L)
print(my_arr,my_arr.shape)

"""Tuple → NumPy Array

Given a tuple of numbers, convert it into a NumPy array and multiply each element by 2.

# Input: (10, 20, 30)
# Output: [20, 40, 60]"""
T=(10, 20, 30)
t_arr=np.array(T)
print(t_arr)
res=t_arr*2
print(res)
L=[]
for i in t_arr:
    L.append(i*2)
print(L)


"""Dictionary Values → Array

Extract values from a dictionary and convert them into a NumPy array.

# Input: {'a': 1, 'b': 2, 'c': 3}
# Output: array([1, 2, 3])"""

my_dict={'a': 1, 'b': 2, 'c': 3}
L=[i for i in my_dict.values()]
my_arr=np.array(L)
print(my_arr)

"""Remove Duplicates Using Set + NumPy

Convert a list with duplicates into a set, then back into a NumPy array.

# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: array([1,2,3,4,5]) (order not important)"""

L=[1, 2, 2, 3, 4, 4, 5]
s1=set(L)
print(s1)
print(np.array(list(s1)))

"""List of Lists → 2D NumPy Array

Convert a nested list into a 2D NumPy array and print its dimensions.

# Input: [[1,2,3], [4,5,6]]
# Output: shape (2,3)"""

L=[[1,2,3], [4,5,6]]
arr=np.array(L)
print(arr.shape)

"""Element-wise Operations

Given two lists, convert them into NumPy arrays and perform addition, subtraction, and multiplication.

# Input: [1,2,3], [4,5,6]
# Output: sum, diff, product arrays"""

l1=[1,2,3]
l2=[4,5,6]
arr1=np.array(l1)
arr2=np.array(l2)
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)

"""Filter Even Numbers (NumPy + List)

Convert a list into a NumPy array and extract only even numbers.

# Input: [1,2,3,4,5,6]
# Output: [2,4,6]"""
L=[1,2,3,4,5,6]
arr=np.array(L)
for i in arr:
    if i%2==0:
        print(i,end=' ')
print(arr[arr % 2 == 0])

"""Find Unique Elements (Set + NumPy)

Find unique elements in a NumPy array using a set.

# Input: array([1,1,2,3,3,4])
# Output: [1,2,3,4]"""

j=np.array([1,1,2,3,3,4])
print(np.unique(j))
s1=set(j)
print(list(s1))

"""Zip Lists into Dictionary then Convert

Given two lists, create a dictionary using zip, then extract values into a NumPy array.

# Input: keys = ['a','b','c'], values = [10,20,30]
# Output: array([10,20,30])
10. Flatten List of Tuples

Convert a list of tuples into a flat NumPy array.

# Input: [(1,2), (3,4), (5,6)]
# Output: array([1,2,3,4,5,6])"""
keys = ['a','b','c']
values = [10,20,30]
my_dict=dict(zip(keys,values))
print(my_dict)
my_arr=np.array(my_dict.values())
print(my_arr)

T=[(1,2), (3,4), (5,6)]
my_arr=np.array(T)
print(my_arr)
flat_arr=[j for i in my_arr for j in i]
print(np.array(flat_arr))





