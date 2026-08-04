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

"""Build a Vandermonde matrix of order 5 for the points
    x = np.array([1., 2., 3., 4., 5.]) using only broadcasting
    and power operations (do not call np.vander).
    Sample first row: [1. 1. 1. 1. 1.]"""

x = np.array([1., 2., 3., 4., 5.])
powers=np.arange(5)
vand=x[:,None]**powers
print(vand)

"""Given a = np.random.randn(1000)
    Compute the 5 %, 25 %, 50 %, 75 % and 95 % quantiles
    in a single call to np.percentile. Then create a boolean
    mask that is True only for values lying between the
    25 % and 75 % quantiles (IQR)."""

a = np.random.randn(1000)
perc1=np.percentile(a,5)
perc2=np.percentile(a,25)
perc3=np.percentile(a,50)
perc4=np.percentile(a,75)
perc5=np.percentile(a,95)
mask=(a>=perc2) & (a<=perc4)
print(mask)

"""Create a sparse-like representation of a 6x6 identity
    matrix using only the three arrays of a COO format:
    row indices, column indices and data values.
    Reconstruct the dense matrix with these three arrays
    and verify it equals np.eye(6)."""

rowind=np.arange(6)
colind=np.arange(6)
vals=np.ones(6,dtype=int)
dense=np.zeros((6,6),dtype=int)
dense[rowind,colind]=vals
print(dense)

# Verify it equals the identity matrix
print(np.array_equal(dense, np.eye(6, dtype=int)))


"""Given two 1-D arrays of different lengths:
    a = np.array([3, 1, 4, 1, 5, 9])
    b = np.array([2, 7, 1, 8])
    Pad the shorter array with zeros on the right, then
    compute their element-wise product and the sum of that
    product (dot product of the padded vectors)."""

a = np.array([3, 1, 4, 1, 5, 9])
b = np.array([2, 7, 1, 8])
print(a.shape,b.shape)
padded=np.pad(b,(0,2),mode="constant")
print(padded)
elewise=a*padded
sumelewise= sum(elewise)
print(f"their element-wise product {elewise} and the sum of that product {sumelewise}")

"""Generate a 4x5 matrix of random integers in [0, 9].
    For each column compute the cumulative sum from top
    to bottom, then replace the original matrix by these
    cumulative sums (in-place if possible). Sample shape
    remains (4, 5)."""
randarr=np.random.default_rng().integers(0,9,(4,5))
cusum=np.cumsum(randarr,axis=0)
print(cusum.shape,randarr.shape)
print(cusum)
randarr[:,]=cusum
print(randarr)

"""Create a 1-D array t = np.linspace(0, 2*np.pi, 200).
    Using only vectorized NumPy, evaluate the function
    f(t) = sin(t) * cos(2*t) + exp(-t/3).
    Then find the index of the global maximum of f
    and the corresponding t value"""
t = np.linspace(0, 2*np.pi, 200)
funct=np.sin(t) * np.cos(2*t) + np.exp(-t/3)
globmax=np.argmax(funct)
print(t[globmax])

"""Given a = np.arange(16).reshape(4, 4)
    Extract the upper-triangular part (including diagonal)
    into a 1-D array in row-major order using boolean
    masking with np.tri / np.triu. Sample length: 10"""
