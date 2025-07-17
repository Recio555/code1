# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:33:33 2024

@author: usuario
"""

def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for z in x:
  print(z)