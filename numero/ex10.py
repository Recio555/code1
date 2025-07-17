# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:23:13 2024

@author: usuario
"""

class Persona(object): 
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.__edad = edad
        
        

p = Persona("Juan Pedro", 23)
print ("Nombre:", p.nombre)
print ("Edad:", p._Persona__edad)