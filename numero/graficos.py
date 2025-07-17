# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:13:53 2024

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros del elipsoide
a = 5
b = 3
c = 2

# Generar puntos en la superficie del elipsoide
x = np.linspace(-a, a, 100)
y = np.linspace(-b, b, 100)
X, Y = np.meshgrid(x, y)

# Calcular la coordenada Z para cada punto
Z = np.sqrt(1 - ((X**2) / a**2) - ((Y**2) / b**2))

# Graficar la superficie del elipsoide
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.3, color='red')
ax.plot_surface(X, Y, -Z, alpha=0.3, color='green')

# Mostrar la gráfica
plt.show()