# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:21:42 2024

@author: usuario
"""

def factors(n):
    for k in range(1,n+1):
        if n%k==0:
            yield k
    

x = factors(100)

for z in x:
  print(z)