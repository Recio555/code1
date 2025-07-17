# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:12:39 2024

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (np.sqrt(1 - ((x**2)/2) - ((y**2)/2)))


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)


X, Y = np.meshgrid(x, y)

Z = f(X, Y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.3, color='green')
ax.plot_surface(X, Y, -Z, alpha=0.3, color='green')
plt.show()