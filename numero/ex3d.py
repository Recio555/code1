# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:02:59 2024

@author: usuario
"""

# Importamos los modulos necesarios
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
 
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

# Definimos los datos
x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [5,6,7,8,2,5,6,3,7,2]
z3 = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

# utilizamos el método bar3d para graficar las barras
ax1.bar3d(x3, y3, z3, dx, dy, dz)

# Mostramos el gráfico
plt.show()
