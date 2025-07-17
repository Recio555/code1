# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:19:09 2025

@author: usuario
"""

import math
import matplotlib.pyplot as plt

T = range(100)
X = [(2*math.pi*t)/len(T) for t in T]
Y = [math.sin(value) for value in X]

plt.plot(X,Y)
plt.show()