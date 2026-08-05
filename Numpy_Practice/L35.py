"""You have a 1-D sensor reading array of length 200 with some
    extreme outliers. Replace every value that is more than
    3 standard deviations away from the mean by the median
    of the whole array. Keep the original dtype.
    Sample: after cleaning, max(abs(data - mean)) <= 3*std"""

import numpy as np

arr= np.random.rand(200)
arr_mean=np.mean(arr)
arr_std=np.std(arr)
arr_median=np.median(arr)
mask= max(abs(arr - arr_mean)) <= 3*arr_std
arr[mask]=arr_median

print(f"array is {arr} ")

"""A grayscale image arrived as a flat 1-D array of 10 000
    pixels. Reshape it into a 100x100 image, flip it upside-down,
    then crop the central 60x60 region. Return the cropped array.
    Expected final shape: (60, 60)"""


grayscale=np.random.rand(10000)
new_res=np.reshape(grayscale,(100,100))
x= np.flipud(new_res)
mask=x[20:80,20:80]
print(f"mask is {mask}",mask.shape)

"""You have integer class labels in the range 0..4
    (length 150). Create a one-hot encoded matrix of shape
    (150, 5) using only NumPy (no sklearn). Each row must
    contain a single 1 and the rest 0s."""

