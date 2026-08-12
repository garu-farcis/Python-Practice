"""12. Load image_rgb.npy. Extract only the red channel,
then create a new RGB image where the green and blue channels are set to zero (keeping only the red information)."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/image_rgb.npy"
arr=np.load(file_path)
print(arr)
red_channel=arr[:,:,0]
new_channel=np.zeros_like(arr)
new_channel[:,:,0]=red_channel

# arr[:,:,1]=0
# arr[:,:,2]=0
# green=arr[:,:,1]
# blue=arr[:,:,2]
# new_rgb=np.concatenate([red_channel,green,blue],axis=0)
print(f"result is {new_channel}")
# print(new_rgb.shape)