# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:00:08 2024

@author: usuario
"""

from numpy import linspace
import matplotlib.pyplot as plt
v0 =5
g = 9.81
t = linspace(0, 1, 1001)
y = v0*t- 0.5*g*t**2
plt.plot(t, y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()
