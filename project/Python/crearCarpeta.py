# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:32:01 2024

@author: usuario
"""

import os
import os.path

def crearCarpeta(carpeta , archivo, tex): 
    if os.path.exists(carpeta): 
        os.chdir(carpeta) 
    else: 
        os.system('mkdir'+' '+ carpeta) 
        os.chdir(carpeta)
        print(os.getcwd())
    
    with open(archivo,'w') as f: 
        f.write(tex)
        f.close()
        
    tex 
    f.write(tex)
    f.close()
    with open(archivo) as f: 
        tex = f.read() 
        print(tex)
        f.close()
        
if __name__ =="__main__":
    carpeta = 'Faborita'
    archivo = 'Persona.txt'
    tex = 'hola'
    crearCarpeta(carpeta, archivo, tex)
