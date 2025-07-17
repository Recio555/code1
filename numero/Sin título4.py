# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:12:47 2024

@author: usuario
"""

import matplotlib.pyplot as plt
from numpy import arange,sin,cos
x = arange(0.0,6.2,0.2)
plt.subplot(2,1,1)
plt.plot(x,sin(x),'o-')
plt.xlabel('x');plt.ylabel('sin(x)')
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(x,cos(x),'^-')
plt.xlabel('eje x');plt.ylabel('cos(x)')
plt.grid(True)
plt.show()
input("\nPress return to exit")