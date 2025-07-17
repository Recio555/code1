# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 12:54:24 2025

@author: usuario
"""

from functools import reduce

def paso1(x): return x + 2
def paso2(x): return x * 3
def paso3(x): return x - 1

funciones = [paso1, paso2, paso3]

# Aplicar secuencialmente
resultado = reduce(lambda acc, f: f(acc), funciones, 5)
print(resultado)  # (((5 + 2) * 3) - 1) = 20
