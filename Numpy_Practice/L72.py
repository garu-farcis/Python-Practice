"""9. Load timeseries.npy. Generate a second array
of the same length containing a sine wave (frequency = 3 cycles over the
whole length). Add this sine wave to the original series and then recover an
 approximation of the original series by subtracting a
 fitted sine of the same frequency (you may use a simple least-squares approach with np.linalg).
"""

import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
data=np.load(file_path)
print(data.shape)
second_arr=np.full_like(data,(np.sinc(3)),dtype=float)
print(second_arr)