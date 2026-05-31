"""numpy questions1: """
import numpy as np

rng = np.random.default_rng(42)
normal_samples = rng.standard_normal(1000)

print(normal_samples.shape)
print(normal_samples[:5])
uniform_matrix = rng.random((10, 10))

print(uniform_matrix)
data = rng.standard_normal((100, 5))
corr_matrix = np.corrcoef(data, rowvar=False)
print("Correlation Matrix:\n", corr_matrix)