import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-3, 2, 200)
Y = X ** 2 - 2 * X + 1.
plt.plot(X, Y)
plt.show()