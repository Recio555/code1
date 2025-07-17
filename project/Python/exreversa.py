# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:11:20 2024

@author: usuario
"""

class Reversa:
    '''recore una secuencia marcha a tras'''
    def __init__(self, datos):
        self.datos = datos
        self.indice = len(datos)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice == 0:
            raise StopIteration
        self.indice = self.indice - 1
        return self.datos[self.indice]
    
rev = Reversa('spam')
iter(rev)
for char in rev:
    print(char)

