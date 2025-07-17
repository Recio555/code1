# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:42:54 2025

@author: usuario
"""

import numpy as np
from scipy.integrate import simps
from scipy.special import erf

def integral_erf(a):
    # Definir la función
    f = lambda x: np.exp(-x**2)
    
    # Crear puntos de evaluación
    x = np.linspace(0, a, 1000)
    
    # Evaluar la función en esos puntos
    y = f(x)
    print(y)