# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:44:35 2024

@author: usuario
"""

def trapezoid(f,a,b,Iold,k):
    if k == 1:
        Inew = (f(a) + f(b))*(b - a)/2.0
    else:
        n = 2**(k -2 ) # Number of new points
        h = (b - a)/n # Spacing of new points
        x = a + h/2.0
        sum = 0.0
        for i in range(n):
            sum = sum + f(x)
            x=x+h
            Inew = (Iold + h*sum)/2.0
    return Inew

import math

def f(x): return (3/2)*math.sqrt(x**2+4)**(0.5)




Iold = 0.0
for k in range(1,21):
    Inew = trapezoid(f,2,3,Iold,k)
    if (k > 1) and (abs(Inew - Iold)) < 1.0e-6:
        break 
        Iold = Inew
print("Integral =",Inew)
print("nPanels =",2**(k-1))
input("\nPress return to exit")