# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:31:10 2024

@author: usuario
"""

import numpy as np
import sympy as sp
 
x = sp.Symbol('x') 



f = 999.87 - 0.06426*x + 0.0085043*x**2 - 0.0000679*x**3
p = sp.diff(f)

print(p)

z = sp.solve(p, x)

print(z)
print('\n')
t = np.linspace(3.97, 79.5,2)
print(t)
for x in t:
    a = 999.87 - 0.06426*x + 0.0085043*x**2 - 0.0000679*x**3
    print(a)