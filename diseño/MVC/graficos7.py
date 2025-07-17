# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:25:42 2024

@author: usuario
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos de muestra
X, Y = np.meshgrid(np.linspace(-8, 8), 
                   np.linspace(-8, 8))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R) / R

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

# Superficie 3D
ax.plot_surface(X, Y, Z, cmap = 'viridis')

# Contour
ax.contour(X, Y, Z, lw = 3, cmap = 'viridis', offset = -1)

# Límites del eje Z
ax.set(zlim = (-1, 0.8))

# plt.show()