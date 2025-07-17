# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:31:06 2025

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plt.title('gafico')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(X, Y, c = 'r')
plt.grid(True, lw = 2, ls = '--', c = '.75')
plt.show()