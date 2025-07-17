# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:25:36 2025

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0, 2 * np.pi, 100)
Y = np.sin(X)
plt.plot(X, Y)
plt.show()