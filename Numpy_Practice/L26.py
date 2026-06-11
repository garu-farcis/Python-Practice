import numpy as np

a = np.array([10, 20, 30, 40])

x= np.take(a, [0, 2, 3])
print(x)

x = np.arange(10)
x[2:7] = 1
print(x)
z = np.arange(81).reshape(3, 3, 3, 3)
print(z)
indicezz=(1,1,1,1)
print(z[indicezz])
indics = (1, 1, 1, slice(0, 2))  # same as [1, 1, 1, 0:2]

print(z[indics])