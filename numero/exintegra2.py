# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:36:28 2024

@author: usuario
"""

import sympy as sp
 
x = sp.Symbol('x') 
y= (x**2 - 4)**(0.5)
a = sp.integrate(y,(x,2,3))
print(a)