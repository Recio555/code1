# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:34:01 2024

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt
def plot_slope(X, Y):
    X =  np.linspace(0,0, 100)
    plt.plot(X,Y, color = 'k')
    
def plot_H(X, Y):
    Y  =  np.linspace(0,0, 100)
    plt.plot(X,Y, color = 'k')
  
X = np.linspace(-3, 3, 100)
Y = X
plt.plot(X, Y)
plot_slope(X, Y)
plot_H(X, Y)
plt.show()