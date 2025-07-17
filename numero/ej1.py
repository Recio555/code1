# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:25:44 2024

@author: usuario
"""

import numpy as np
import sympy as sp
 
x = sp.Symbol('x') 

p = -x**2+40*x-379

print(p)

z = sp.solve(p, x)

print(z)