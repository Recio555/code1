# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 00:15:02 2024

@author: usuario
"""
import ctypes
from ctypes import wintypes as w

import wave
import time
import os
import threading

class WAVEHDR(ctypes.Structure):
    _fields_ = [
        ("lpData", ctypes.c_void_p),
        ("dwBufferLength", ctypes.c_uint),
        ("dwBytesRecorded", ctypes.c_uint),
        ("dwUser", ctypes.c_ulong),
        ("dwFlags", ctypes.c_uint),
        ("dwLoops", ctypes.c_uint),
        ("lpNext", ctypes.c_void_p),
        ("reserved", ctypes.c_void_p),
    ]
    
def read_wav(self, file_path):
    with wave.open(file_path, 'rb') as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)
        return params, frames
    

from threading import Thread
class Media: 
   def __init__(self, **arg): 
       super().__init__(**arg)
       self.lib = ctypes.windll.winmm
       self.SND_FILENAME = 0x20000
       self.lib.PlaySoundW.argtypes = w.LPCWSTR,w.HMODULE,w.DWORD
       self.lib.PlaySoundW.restype = w.BOOL
       self.path = b"Sonido.wav"
        
        
   def time(self):
        path = "Sonido.wav"
        self.params, self.audio_data = read_wav(self, path)
        print(self.params)
        time.sleep(len(self.audio_data) / (self.params.framerate * self.params.sampwidth))
        
   #def Play(self): 
       # self.lib.PlaySound(self.path, None, 0x20000)
        
   def Play(self):
       def Player():
           self.lib.PlaySound(self.path, None, 0x20000)
       hilo_reproduccion = threading.Thread(target=Player)
       hilo_reproduccion.daemon = True  # Hacer el hilo  se cierre cuando la interfaz cierre
       hilo_reproduccion.start()
       
        
    

        
        
