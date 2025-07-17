# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:02:15 2024

@author: usuario
"""

import os
import os.path

class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def Crear(self): 
        if os.path.exists(self.nombre): 
            os.chdir(self.nombre) 
            print(os.getcwd())
        else: 
            os.system('mkdir'+' '+ self.nombre) 
            os.chdir(self.nombre)
            print(os.getcwd())

class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def crear_archivo(self):
        try: 
            with open(self.nombre, "x") as f:
                pass
                
        except FileExistsError:
            #print('el archivo existe')
            pass
    
    def Editar(self, texto):
       self.texto = texto
       with open(self.nombre, 'a') as f:
           f.write(self.texto)
           
    def Leer(self): 
        with open(self.nombre, 'r') as f: 
            tex = f.read() 
            print(tex)
            f.close()
            
    def CrearEscribir(self):
        with open(self.nombre, 'w') as f: 
            self.texto = input("Ecribe el texto a guardar : ")
            f.write(self.texto)
            
    def Guardar(self):
        self.nombre = input("Escriba el nombre del archivo :")
        if os.path.exists(self.nombre):
            p = input("Deseas sobre escribir el archivo? si o no :")
            if p == 'si':
               a.CrearEscribir()
            else:
                a.Guardar()
        else: 
            a.CrearEscribir()
              
       
        
if __name__ =="__main__":
    carpeta = input("Introduce el nombre de la carpeta sin espacios \n:")
    archivo = input("Introduce el nombre del achivo \n :")
    tex = input("Introduce el texto que deseas guardar \n :")
    c = Carpeta(carpeta)
    c.Crear()
    a = Archivo(archivo)
    a.Editar(tex)
    a.crear_archivo()
    a.Leer()
    a.Guardar()
    
