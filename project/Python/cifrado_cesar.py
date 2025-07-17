# -*- coding: utf-8 -*-
"""
Created on Mon May  5 18:37:17 2025

@author: usuario
"""

def cifrado_cesar(texto, desplazamiento):
    resultado = ''
    for char in texto:
        if char.isupper():
            # Para letras mayúsculas
            resultado += chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
        elif char.islower():
            # Para letras minúsculas
            resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            # Otros caracteres no se modifican
            resultado += char
    return resultado

# Uso del cifrado
text = 'Hello World'
shift = 3

texto_cifrado = cifrado_cesar(text, shift)
print("Texto original: ", text)
print("Texto cifrado:  ", texto_cifrado)