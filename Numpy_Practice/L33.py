"""Create a 7x7 matrix with values 0..48 in column-major order
    (use order='F'). Extract the main diagonal and the two
    adjacent diagonals (super- and sub-diagonal) into three
    separate 1-D arrays without using np.diag in a loop.
    Sample main diagonal length: 7"""

import numpy as np
# arr= np.random.default_rng().integers(0,48,(7,7))
a = np.arange(49).reshape(7, 7, order='F')
print(a)
maind=np.diag(a)
adj1=np.diag(a,k=1)
adj2=np.diag(a,k=-1)
print(maind,adj1,adj2)

"""Given a = np.arange(24).reshape(2, 3, 4)
    Use np.transpose / np.moveaxis to rearrange axes so the
    shape becomes (4, 2, 3). Then verify that a.flatten() and
    the rearranged array.flatten() produce identical values
    (same linear order)."""

a = np.arange(24).reshape(2, 3, 4)
x=np.transpose(a,(2,0,1))
print(np.array_equal(a.flatten(), x.flatten()))

"""Generate two arrays of length 12:
    x = np.random.uniform(0, 10, 12)
    y = np.random.uniform(0, 10, 12)
    Compute the pairwise Euclidean distances between every
    point in x and every point in y using broadcasting only
    (result shape must be 12x12). No Python loops or
    scipy.spatial."""

x = np.random.uniform(0, 10, 12)
y = np.random.uniform(0, 10, 12)
dist = np.sqrt((x[:, np.newaxis] - y[np.newaxis, :]) ** 2)
print(f"Euclidean distances are {dist}")


"""Create a 1-D array of 50 random integers in [1, 20].
    Using np.bincount (and possibly np.unique), return:
    - the mode (most frequent value)
    - how many times it appears
    If several modes exist, return the smallest one."""

d1=np.random.default_rng().integers(0,20,50)
mode=np.bincount(d1)
print(f"mode is {mode}")
counts=np.argmax(mode)
freq=mode[counts]
print(f"freq is {freq}")

"""20.Given a 5x5 array of random floats, replace all elements
    that are strictly greater than their 4-neighbors
    (up/down/left/right) by the average of those neighbors.
    Edge elements keep their original values. Use only
    slicing and arithmetic (no loops)."""


a = np.random.rand(5, 5)
result = a.copy()

c = a[1:-1, 1:-1]
u = a[:-2, 1:-1]
d = a[2:, 1:-1]
l = a[1:-1, :-2]
r = a[1:-1, 2:]

avg = (u + d + l + r) / 4

mask = (c > u) & (c > d) & (c > l) & (c > r)

result[1:-1, 1:-1] = np.where(mask, avg, c)
