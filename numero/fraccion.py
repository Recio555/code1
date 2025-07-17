# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:26:48 2024

@author: usuario
"""

from fractions import Fraction
def add(a, b):
    print('Result of Addition: {0}'.format(a+b))
if __name__ == '__main__': 
     a = Fraction(input('Enter first fraction: '))
     b = Fraction(input('Enter second fraction: '))
     op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
     if op == 'Add':
        add(a,b)