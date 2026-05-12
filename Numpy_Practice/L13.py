import matplotlib.pyplot as plt
import numpy as np
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])
plt.colorbar()
plt.title(f"Image plot of $\sqrt{x**2 + y**2}$ for a grid of values")