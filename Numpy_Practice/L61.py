"""12. Load image_rgb.npy. Downsample the image by a factor of 2 using simple averaging of 2×2 blocks
(resulting shape should be 4×4×3). Do it without using external libraries (only NumPy slicing and mean)."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/image_rgb.npy"
data=np.load(file_path)
print(data.shape)
downsample=data.reshape(data.shape[0]//2,2,data.shape[1]//2,2,3).mean(axis=(1,3))
print(downsample,downsample.shape)