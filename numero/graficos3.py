# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:28:48 2024

@author: usuario
"""
import numpy as np
x = np.array([-1, 0, 1])
y = np.array([-2, 0, 2])
X, Y = np.meshgrid(x, y)

op = np.ogrid[0:4,0:4]

print(op)

print(X)
print()
print(Y)
print('la funcion Z')
Z = (X + Y) ** 2
print(Z)