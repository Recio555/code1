# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:53:55 2024

@author: usuario
"""

from fractions import Fraction
f = Fraction(3, 4) + 1
print(f) 

a = complex(2, 3)
b = 3 + 3j
print(a/b)

z = 4 + 3j

print(z.real)

print(z.imag)

print(abs(z))

print(z.conjugate())

try:
 a = float(input('Enter a number: '))
except ValueError:
 print('You entered an invalid number')