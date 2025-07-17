# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:06:25 2024

@author: usuario
"""

import os
import os.path
carpeta = 'Hola'
if os.path.exists(carpeta): 
    os.chdir(carpeta)
    
else: 
    os.system('mkdir carpeta') 
    os.chdir(carpeta)
    
    
print(os.getcwd())


with open('holamundo.txt','w') as f: 
    f.write('\n' + 'Hola Mundo') 
    f.close()
    
   
with open("holamundo.txt") as f:
    tex = f.read()
    print(tex)
    f.close()
    