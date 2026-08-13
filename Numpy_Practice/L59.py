"""9. Load timeseries.npy. Generate a random walk of the same length and add it
 as noise (scaled by 0.3) to the original series.
 Then apply a simple exponential moving average with alpha=0.2 and return the smoothed series."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
data=np.load(file_path)
print(data.shape)
rand_walk_noise=np.random.randn(len(data))*0.3
print(rand_walk_noise)
rand_walk=rand_walk_noise+data
alpha = 0.2

smoothed = np.empty_like(rand_walk, dtype=float)


smoothed[0] = rand_walk[0]


for i in range(1, len(rand_walk)):
    smoothed[i] = (
        alpha * rand_walk[i]
        + (1 - alpha) * smoothed[i - 1]
    )

print(smoothed)