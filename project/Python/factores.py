# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:08:46 2024

@author: usuario
"""

def factors(n):
     results = [ ]
     for k in range(1,n+1):
         if n%k==0:
             results.append(k)
     return results

print(factors(100))