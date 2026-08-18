"""5. Load image_rgb.npy. Flip the image both vertically and horizontally (i.e.,
 rotate 180 degrees) using only slicing. Then extract the central 4×4×3 crop from the flipped image."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/image_rgb.npy"
data=np.load(file_path)
print(data.shape)
vert=np.flip(data,axis=(0,1))
print(vert.shape)
small_image=vert[3:7, 3:7, :]
print(small_image)


