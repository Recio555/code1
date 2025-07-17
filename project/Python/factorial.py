# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 21:31:35 2024

@author: usuario
"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))