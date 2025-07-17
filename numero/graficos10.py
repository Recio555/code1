# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:27:06 2024

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
ax.plot_surface(X, Y, Z, cmap = 'Spectral_r', alpha = 0.9)

# Curvas de nivel coloreadas
ax.contour(X, Y, Z, lw = 2, colors = 'black', offset = -1)
ax.contourf(X, Y, Z, cmap = 'Spectral_r', offset = -1, alpha = 0.75)

# Límites del eje Z
ax.set(zlim = (-1, 0.8))

# plt.show()