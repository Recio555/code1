# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 13:01:29 2025

@author: usuario
"""

import os

def leer_archivos(directorio):
    return [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith('.txt')]

def leer_contenido(archivo):
    with open(archivo, 'r') as f:
        return f.read()

def procesar_archivos(directorio):
    archivos = leer_archivos(directorio)
    for archivo in archivos:
        contenido = leer_contenido(archivo)
        print(f"[{archivo}]\n{contenido}\n---")

procesar_archivos("C:\project\python")  # reemplaza con tu ruta
