# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:35:53 2024

@author: usuario
"""

class Calculadora(object): 
    def __init__(self, nombre): 
        self.nombre = nombre 
        
    def modelo(self): 
        return self.nombre 
    
    @staticmethod
    def suma(x, y): 
        return x + y
    
c = Calculadora("Multivac")
print (c.modelo())
print (c.suma(4, 8))
print ( Calculadora.suma(4, 8))