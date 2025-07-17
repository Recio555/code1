import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)

Z = X**2 -Y**2

fig = plt.figure(figsize=(10,80))
ax = fig.add_subplot(111, projection='3d')

supr = ax.plot_surface(X,Y,Z, cmap = 'viridis', edgecolor='none')
ax.set_title('z = $x^2-Y^2$')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()

