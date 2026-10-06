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
mean=np.apply_along_axis(lambda x:np.convolve(x,kernel,mode='valid'),axis=0,arr=data[:,0])
# tot_kernel=np.sum(np.ones(window)/window)
tot=np.apply_along_axis(lambda x:np.convolve(x,np.ones(window),mode='valid'),axis=0,arr=data[:,1])
# max_kernel=np.max(np.ones(window)/window)
max_ = np.array([np.max(data[i:i + window, 2])for i in range(len(data) - window + 1)])
one_stack=np.column_stack([mean,tot,max_])
