# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:58:26 2024

@author: usuario
"""

import numpy as np
import sympy as sp
 
x = sp.Symbol('x') 

b = 20*(x-24)
a = (x-25)**2+ x-24

f = b/a
p = sp.diff(f)

print(p)

z = sp.solve(p, x)

print(z)
print('\n')
t = np.linspace(23, 25,2)
print(t)
for n in t:
    a = (20*(n-24))/((n-25)**2 + n -24)
    print(a)
