# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:52:37 2024

@author: usuario
"""

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError(' x must be numeric' )
    elif x < 0:
        raise ValueError( 'x cannot be negative' )
sqrt(-6)