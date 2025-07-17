# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:14:51 2025

@author: usuario
"""

import matplotlib.pyplot as plt
import cmath
import numpy as np
X =  np.linspace(-1, 1, 200)
Y = [cmath.sqrt(1- value ** 2) for value in X] 
f = [-cmath.sqrt(1- value ** 2) for value in X]
plt.plot(X, Y)
plt.plot(X, f)
plt.title('{x,y)\sqt(x**2+y**2<1')
plt.show()