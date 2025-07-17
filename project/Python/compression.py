# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:46:26 2024

@author: usuario
"""

import zlib
s = b'hola que tal  jkhjlkljjlkjl  kkllk  kkk lll llll'
print(len(s))

t = zlib.compress(s)
print(len(t))