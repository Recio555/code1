# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:48:41 2024

@author: usuario
"""

from trapezoidal import trapezoidal

from math import exp
v = lambda x: (3/2)*(x**2-4)**0.5

n =4
numerical = trapezoidal(v, 0,1,n)

print(numerical)
 