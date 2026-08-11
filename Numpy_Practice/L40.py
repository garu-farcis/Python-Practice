"""5. Load image_rgb.npy (shape 8×8×3). Convert the RGB image to grayscale
using the formula 0.299*R + 0.587*G + 0.114*B.
Then normalize the grayscale values to the range [0, 1]."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/image_rgb.npy"
data=np.load(file_path)
print(data.shape)
R=data[:,:,0]
G=data[:,:,1]
B=data[:,:,2]

func=0.299*R + 0.587*G + 0.114*B
print(func)
normallise_grayscale=(func-np.min(func))/(np.max(func)-np.min(func))
print(normallise_grayscale)
# covert_rgb=np.poly
# val((0.299*R + 0.587*G + 0.114*B),data)
