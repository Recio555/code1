# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:46:37 2024

@author: usuario
"""

def trapezoidal(f, a, b, n): 
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result