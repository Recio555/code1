# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:07:38 2024

@author: usuario
"""

class ListaLogger(list):
    def append(self, x): 
        print ("Añadiendo", x, "a la lista (¡ahora s´ı!)" )
        super(ListaLogger, self).append(x) 
        
numeros = ListaLogger([3,4]) 
a = input('Introduce el numero: ')
numeros.append(a)
print (numeros)