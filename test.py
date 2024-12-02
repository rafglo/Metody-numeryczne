import numpy as np
x = - 1
for _ in range(1000):
    x = np.exp(x) - 1
print(x)