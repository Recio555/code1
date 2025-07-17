# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:21:09 2024

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
ax.plot_surface(X, Y, Z, alpha = 0.7,
                linewidth = 0.3, edgecolor = 'black')

# plt.show()