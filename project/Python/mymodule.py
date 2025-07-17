# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:57:12 2024

@author: usuario
"""


def Suma(a, b):
    for n in (a,b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
        return a+b


