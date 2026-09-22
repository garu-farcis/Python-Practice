"""5. Load sensor_signals.npy.
For each channel, compute a rolling mean with window size 5.
Pad the result so the output has the same shape as the original array (use 'edge' padding or NaNs at the beginning)."""
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sensor_signals.npy"
import numpy as np
data=np.load(file_path)
window=5
kernel = np.ones(window) / window
rolling_mean = np.apply_along_axis(
    lambda x: np.convolve(x, kernel, mode="valid"),
    axis=0,
    arr=data
)

result = np.pad(
    rolling_mean,
    ((window - 1, 0), (0, 0)),
    mode="edge"
)

print(result)
print(result.shape)