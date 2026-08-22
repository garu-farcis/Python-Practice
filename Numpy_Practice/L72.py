"""9. Load timeseries.npy. Generate a second array
of the same length containing a sine wave (frequency = 3 cycles over the
whole length). Add this sine wave to the original series and then recover an
 approximation of the original series by subtracting a
 fitted sine of the same frequency (you may use a simple least-squares approach with np.linalg).
"""

import numpy as np

file_path = "/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
data = np.load(file_path)
print(data.shape)
x = np.linspace(0, 2 * np.pi * 3, len(data))
second_arr = np.sin(x)
modified = data + second_arr
X = np.column_stack([np.sin(x), np.cos(x)])
coefficients, _, _, _ = np.linalg.lstsq(X, modified - data.mean(), rcond=None)
A, B = coefficients
fitted_sine = A * np.sin(x) + B * np.cos(x)
recovered = modified - fitted_sine
print("Original:", data)
print("Modified:", modified)
print("Recovered:", recovered)