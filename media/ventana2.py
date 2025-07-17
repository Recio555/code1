# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:30:48 2024

@author: usuario
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time
import Rsonido

# Función que realiza una tarea larga en un hilo secundario
def tarea_larga(label):
    def trabajo():
        a = Rsonido.Media()
        a.Player()
        

    # Inicia el hilo secundario
    hilo = threading.Thread(target=trabajo)
    hilo.start()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hilos en Tkinter")
ventana.geometry("300x150")

# Etiqueta para mostrar el progreso
label = tk.Label(ventana, text="Esperando...")
label.pack(pady=20)

# Botón para iniciar la tarea larga
boton = tk.Button(ventana, text="Iniciar Tarea", command=lambda: tarea_larga(label))
boton.pack(pady=10)

ventana.mainloop()