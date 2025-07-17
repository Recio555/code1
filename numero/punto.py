# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:44:56 2024

@author: usuario
"""

import math
2
3 class Punto(object):
4 def __init__(self, x, y):
5 self.x = x
6 self.y = y
7
8 def distancia(self, otro):
9 x_delta = self.x - otro.x
10 y_delta = self.y - otro.y
11 return math.sqrt(x_delta ** 2 + y_delta ** 2)
12
13 c1 = Punto(4, 1.5)
14 c2 = Punto(3, 3.1)
15 print c1.distancia(c2) == Punto.distancia(c1, c2)
