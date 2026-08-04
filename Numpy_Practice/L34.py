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
arr=np.random.default_rng().standard_normal(200)
rolling_standd=np.lib.stride_tricks.sliding_window_view(arr,window_shape=10)
print(rolling_standd.shape)


"""Given a square matrix A of shape (n, n) with n = 5
    filled with random floats, compute its inverse with
    np.linalg.inv and its determinant with np.linalg.det.
    Verify that A @ A_inv is close to the identity
    (use np.allclose with a reasonable tolerance)."""


squarematrix=np.random.rand(5,5)
print(squarematrix)
inv=np.linalg.inv(squarematrix)
deter=np.linalg.det(squarematrix)
print(f"inverse is {inv} and determinant is {deter}")
print(np.allclose(squarematrix,squarematrix.T))

"""Build a 10x10 lower-triangular matrix of ones
    (including the diagonal) using only np.tri or
    broadcasting with np.arange. No loops, no np.tril
    of a full ones matrix if you can avoid it."""

x=np.ones((10,10))
print(x)
tri_matrix=np.tri(10,10,dtype=int,k=0)
print(tri_matrix)

"""Given temperatures = np.array([22.1, 23.5, 19.8, 25.0, 21.3, 24.7, 18.9])
    Convert the array to a structured array with a single
    field 'temp' of dtype float64, then add a second field
    'is_hot' that is True wherever temp > 22."""

temperatures = np.array([22.1, 23.5, 19.8, 25.0, 21.3, 24.7, 18.9])
dtype=[
    ("temp","f8"),
    ("is_hot","bool")
]
struct=np.empty(temperatures.shape,dtype=dtype)
struct["temp"]=temperatures
struct["is_hot"]=struct["temp"]>22
print(struct)

"""Create a 3-D array of shape (4, 5, 6) filled with
    consecutive integers starting at 0. Using advanced
    indexing, extract the sub-array corresponding to
    indices [0, 2] on axis 0, [1, 3] on axis 1 and
    all of axis 2. Expected shape: (2, 2, 6)"""


myarr=np.arange(120).reshape(4,5,6)
res=myarr[np.ix_([0,2],[1,3],np.arange(6))]
print(res.shape)

"""Simulate 1000 independent fair coin flips
    (0 = tails, 1 = heads) with np.random.randint.
    Compute the length of the longest consecutive run
    of heads using only vectorized operations
    (hint: np.diff + np.where or group-length tricks)."""

fairarr=np.random.randint(0,2,1000)

# Add zeros at both ends
padded = np.concatenate(([0], fairarr, [0]))

# Find changes
changes = np.diff(padded)

# Heads start where change = +1
starts = np.where(changes == 1)[0]

# Heads end where change = -1
ends = np.where(changes == -1)[0]

# Lengths of head runs
lengths = ends - starts

# Longest run
longest = lengths.max()

print(longest)