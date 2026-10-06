"""Load weather_stations.npy.
   Create a sliding window of 5 consecutive days.
   For each window compute:
   - mean temperature
   - total rainfall
   - max wind speed
   Stack these three statistics into a new array of shape (96, 3)"""
import numpy as np

file="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/weather_stations.npy"
data=np.load(file)
window=5
kernel=np.ones(window)/window
mean=np.apply_along_axis(lambda x:np.convolve(x,kernel,mode='valid'),axis=1,arr=data)
tot_kernel=np.sum(np.ones(window)/window)
tot=np.apply_along_axis(lambda x:np.convolve(x,tot_kernel,mode='valid'),axis=1,arr=data)
max_kernel=np.max(np.ones(window)/window)
max_=np.apply_along_axis(lambda x:np.convolve(x,max_kernel,mode='valid'),axis=1,arr=data)

one_stack=np.hstack([mean,tot,max_])
