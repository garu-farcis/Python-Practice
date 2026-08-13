"""5. Load image_rgb.npy. Compute the mean intensity of each color channel separately.
Then create a new image where every pixel is replaced by the average
RGB color of the whole image (constant color image)."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/image_rgb.npy"
data=np.load(file_path)
print(data.shape)
r_data=data[:,:,0]
g_data=data[:,:,1]
b_data=data[:,:,2]
r_mean=np.mean(r_data)
g_mean=np.mean(g_data)
b_mean=np.mean(b_data)
mean_rgb = np.array([r_mean, g_mean, b_mean])
new_image=np.full_like(data,mean_rgb)
# r_col=np.full_like(r_data,r_mean)
# g_col=np.full_like(g_data,g_mean)
# b_col=np.full_like(b_data,b_mean)
# new_image=np.concatenate([r_col,g_col,b_col],axis=0)
print(new_image)