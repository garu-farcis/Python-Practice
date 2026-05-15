import numpy as np
x = np.array([[[0], [1], [2]]])
print(x.shape)
X=np.squeeze(x).shape
print(X,x)
print(np.squeeze(x))
x = np.arange(9.0)
# split an array with the number of indices you like
print(np.split(x, 3))
# Construct an array by repeating A the number of times given by reps.
print(np.tile(x,3).reshape((9,3)))
# Pad an array.
