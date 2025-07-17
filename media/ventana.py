# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:27:03 2024

@author: usuario
"""
import Msonido
import tkinter as tk

from tkinter import *
import threading

 
class GUI: 
    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk()
        self.create_button_frame()
        self.create_bottom_frame()
        self.root.mainloop()
     
    def create_button_frame(self):
        buttonframe= Frame(self.root)
        self.playbtn=Button(buttonframe, text ='play', command = self.play)
        self.playbtn.grid(row=3, column=3)
        buttonframe.grid(row=1, pady=4, padx=5)
     
       
    def create_bottom_frame(self):
        bottomframe = Frame(self.root)
        add_filebtn=Button(bottomframe,  text='pause', command = self.pausa)
        add_filebtn.grid(row=2, column=1)
        btn=Button(bottomframe,  text='Reanudar', command = self.reanudar)
        btn.grid(row=3, column=1)
        bottomframe.grid(row=2, sticky='w',pady=4, padx=5)
        
        
    def play(self):
        self.player.reproducir()
    def pausa(self):
        self.player.pausar()
    def reanudar(self):
        self.player.reanudar()
    
        

if __name__ == '__main__':
    archivo_audio = "Sonido.wav"
    obj = Msonido.ReproductorWaveOut(archivo_audio)
    app = GUI(obj)