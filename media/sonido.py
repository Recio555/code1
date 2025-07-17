# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:50:42 2024

@author: usuario
"""
import ctypes
from ctypes import wintypes as w

import wave
import time
import os

# Cargar la biblioteca winmm.dll
lib = ctypes.windll.winmm

# Definir la estructura WAVEHDR para el encabezado de los datos de audio
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

# Función para leer un archivo WAV y obtener su formato y datos
def read_wav(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)
        return params, frames


lib.PlaySoundW.argtypes = w.LPCWSTR,w.HMODULE,w.DWORD
lib.PlaySoundW.restype = w.BOOL

SND_FILENAME = 0x20000

# Call it with a Unicode string and it works.
lib.PlaySoundW('sound.wav',None,SND_FILENAME)

# Call it with a byte string and get an error since `.argtypes` is defined.
#dll.PlaySoundW(b'Sonido.wav',None,SND_FILENAME)
lib.PlaySound(b"Sonido.wav", None, 0x20000)