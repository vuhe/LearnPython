import numpy as np
import matplotlib.pyplot as plt

print(0.99 ** 365)
print(1.01 ** 365)

x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.show()
