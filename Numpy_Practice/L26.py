import numpy as np

a = np.array([10, 20, 30, 40])

x= np.take(a, [0, 2, 3])
print(x)