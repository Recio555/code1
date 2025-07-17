# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:37:13 2024

@author: usuario
"""
class Perro:
    trucos = []
    def __init__(self, nombre):
        self.nombre = nombre
        
    def agregar(self, truco):
        self.trucos.append(truco)
        
        
        
d = Perro('Fido')
e = Perro('Buddy')    
d.agregar('GIRAR')
e.agregar('hacer el muerto')

print(d.trucos)