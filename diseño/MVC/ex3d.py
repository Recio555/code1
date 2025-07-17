# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:39:22 2024

@author: usuario
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Definir el rango de valores para x y y
x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)

# Crear una cuadrícula de coordenadas para x y y
X, Y = np.meshgrid(x, y)

# Calcular los valores de f(x, y) en cada punto de la cuadrícula
#Z = 2 - X**2 - Y**2
Z = (X + Y) ** 2

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')

# Título del gráfico
#plt.title('Gráfico de f(x, y) = 2 - x^2 - y^2')
plt.title('Z = (X + Y) ** 2')

# Mostrar el gráfico
plt.show()