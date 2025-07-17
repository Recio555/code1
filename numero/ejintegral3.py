# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:06:21 2024

@author: usuario
"""

import math
import sympy as sp
a, b, x, y = sp.symbols("a, b, x, y")
i = sp.integrate(sp.exp(-x**2), (x, 0, math.inf))
print(i)

print('\n')

a, b, c = sp.symbols("a, b, c", positive=True)
b = sp.integrate(a * sp.exp(-((x-b)/c)**2), (x, -math.inf, math.inf))
print(b)
print('\n')

a, b, x, y = sp.symbols("a, b, x, y")
f = sp.integrate((x**2-4)**0.5, (x, 2, 3))

print(f)
print('\n')
print(sp.Matrix([1, 2]))
input()