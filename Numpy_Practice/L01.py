"""Array properties

Given an array:

arr = np.array([[1, 2, 3], [4, 5, 6]])

Find:

shape
number of dimensions
data type"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print('the dimensions ', np.ndim(arr))
b = arr[1:]
print(b)
print(arr)
print('shape', arr.shape)
print('size', arr.size)
print('data type', arr.dtype)
elements =[j for i in arr for j in i]
print(elements)

my_array= np.arange(20)
print(my_array)
my_view= my_array[2:6]
print(my_view)

print(np.zeros(2),'\n',np.ones(3),'\n',np.empty(3),'\n',np.arange(20))
arr = np.linspace(0, 10, 5)
print(arr)
h= np.argsort(arr,0)
# returns indices when we pass array
print('hello',h)

# sorts by keys and returns indices
h1 =np.lexsort(arr)
print(h1)


x = np.array([3, 1, 2])
print(np.argsort(x))