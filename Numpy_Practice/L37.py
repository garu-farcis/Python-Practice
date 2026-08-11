"""2. Load temperatures.npy (shape 30×12). Calculate the average temperature per month and the average temperature per day.
Find the day that has the highest temperature range (max − min across the 12 months)."""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/temperatures.npy"
data=np.load(file_path)
print(data.shape)
avg_month=np.average(data,axis=0)
avg_day=np.average(data,axis=1)
daily_range=np.max(data,axis=1)-np.min(data,axis=1)
max_temp=np.argmax(daily_range)
print(f"highest temp is {max_temp}")
