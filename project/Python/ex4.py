# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:00:32 2024

@author: usuario
"""

def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError( parameter must be an iterable type )
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError( elements must be numeric )
        total = total+ v
    return total

sum((4,5,9,8))