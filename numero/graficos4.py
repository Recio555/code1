# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:06:56 2024

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

# Superficie 3D en verde claro
ax.plot_surface(X, Y, Z, color = 'lightgreen')

# plt.show()