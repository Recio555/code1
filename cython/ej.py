# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:24:06 2024

@author: usuario
"""

def Generar(n):
    for k in range(1,n+1):
        if n%k ==0:
            yield k
        

for p in Generar(100):
    print(p)