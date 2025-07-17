# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:14:28 2024

@author: usuario
"""

with open("filename.log", "a") as log_file:
 log_file.write("Log message goes here.\n")
 
 
def log_message(msg):
 with open("filename.log", "a") as log_file:
     log_file.write("{0}\n".format(msg))
 
log_message("Hola que tal esto es un parrafo de prueba ")