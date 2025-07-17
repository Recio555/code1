# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:29:54 2024

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt

# Datos
X, Y = np.meshgrid(np.linspace(-5, 10, 100),
                   np.linspace(-5, 10, 100))
Z = np.sqrt(X ** 2 + Y ** 2)

# Contour
fig, ax = plt.subplots()
cnt = ax.contour(X, Y, Z)
ax.clabel(cnt, cnt.levels, inline = True, fontsize = 10)

# plt.show() 
 
