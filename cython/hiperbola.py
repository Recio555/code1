# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:35:32 2024

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros de la hipérbola
a = 1
b = 1

# Crear un rango de valores para x
x = np.linspace(-5, 5, 400)
y1 = np.sqrt((x**2 / a**2 - 1) * b**2)
y2 = -np.sqrt((x**2 / a**2 - 1) * b**2)

# Graficar la hipérbola
plt.plot(x, y1, 'b', label='y = sqrt((x^2 / a^2 - 1) * b^2)')
plt.plot(x, y2, 'b')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Gráfica de una Hipérbola')
plt.xlabel('x')
plt.ylabel('y')
plt.show()