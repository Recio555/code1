# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:22:17 2024

@author: usuario
"""

from matplotlib import pyplot as plt
import math

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
        result *= h
    return result

from math import exp
v = lambda t: 3*(t**2)*exp(t**3)
n = 4
numerical = trapezoidal(v, 0, 1, n)
print(numerical)