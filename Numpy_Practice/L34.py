"""Create a 6x8 array of random integers in [0, 99].
    Extract all elements that are perfect squares using
    boolean masking and np.isin (or a vectorized square-root
    check). Return them sorted in ascending order.
    Sample possible values: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81"""


import numpy as np
arr=np.random.default_rng().integers(0,99,(6,8))
mask=np.isclose(np.sqrt(arr),np.round(np.sqrt(arr)))
x=arr[mask]
x.sort()
print(x)

"""Given a = np.arange(1, 13).reshape(3, 4)
    Use np.pad to add a border of zeros so the result is
    shape (5, 6). Then replace the inner 3x4 block by its
    element-wise reciprocal (1/a). Keep dtype float."""

a = np.arange(1, 13).reshape(3, 4)
padded= np.pad(a,((1,1), (1,1)),mode="constant")
# a[:,]=1/a
padded[1:-1,1:-1]= 1/a
print(padded)


"""Generate two rank-1 arrays:
    u = np.random.randn(5)
    v = np.random.randn(7)
    Form the outer product u[:, None] * v[None, :] using
    only broadcasting. Verify the result equals np.outer(u, v)."""

u = np.random.randn(5)
v = np.random.randn(7)
prod=u[:, None] * v[None, :]
print(np.array_equal(prod,np.outer(u,v)))

"""Create a 1-D array of 200 standard-normal samples.
    Compute a rolling standard deviation with window size 10
    using only np.lib.stride_tricks.sliding_window_view
    (or pure slicing + axis reduction). Result length = 191."""


