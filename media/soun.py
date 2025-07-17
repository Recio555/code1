# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:42:33 2024

@author: usuario
"""

import ctypes
import wave
import time
import os
from ctypes import wintypes as w

# Cargar la biblioteca winmm.dll
winmm = ctypes.windll.winmm

# Definir la estructura WAVEFORMATEX para el formato del audio
class WAVEFORMATEX(ctypes.Structure):
    _fields_ = [
        ("wFormatTag", ctypes.c_ushort),
        ("nChannels", ctypes.c_ushort),
        ("nSamplesPerSec", ctypes.c_uint),
        ("nAvgBytesPerSec", ctypes.c_uint),
        ("nBlockAlign", ctypes.c_ushort),
        ("wBitsPerSample", ctypes.c_ushort),
        ("cbSize", ctypes.c_ushort),
    ]

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

# Función para reproducir el archivo WAV
def play_wav(file_path):
    if not os.path.isfile(file_path):
        print("El archivo no existe.")
        return

    # Leer los datos del archivo WAV
    params, audio_data = read_wav(file_path)

    # Crear el formato WAVEFORMATEX basado en el archivo WAV
    wave_format = WAVEFORMATEX(
        wFormatTag=1,  # PCM
        nChannels=params.nchannels,
        nSamplesPerSec=params.framerate,
        nAvgBytesPerSec=params.framerate * params.nchannels * params.sampwidth,
        nBlockAlign=params.nchannels * params.sampwidth,
        wBitsPerSample=params.sampwidth * 8,
        cbSize=0
    )

    # Abrir el dispositivo de salida de audio
    hWaveOut = ctypes.c_void_p()
    res = winmm.waveOutOpen(ctypes.byref(hWaveOut), 0, ctypes.byref(wave_format), 0, 0, 0)
    if res != 0:
        print("Error al abrir el dispositivo de salida de audio.")
        return

    # Preparar los datos de audio
    #buffer = ctypes.create_string_buffer(audio_data)
    #wave_header = WAVEHDR(ctypes.cast(buffer, ctypes.c_void_p), len(audio_data), 0, 0, 0, 0, 0, 0)

    # Preparar el encabezado del buffer para la reproducción
    #winmm.waveOutPrepareHeader(hWaveOut, ctypes.byref(wave_header), ctypes.sizeof(WAVEHDR))

    # Reproducir los datos de audio
    #winmm.waveOutWrite(hWaveOut, ctypes.byref(wave_header))

    # Esperar hasta que el audio termine de reproducirse
    #time.sleep(len(audio_data) / (params.framerate * params.sampwidth))

    # Limpiar el encabezado y cerrar el dispositivo de salida
    #winmm.waveOutUnprepareHeader(hWaveOut, ctypes.byref(wave_header), ctypes.sizeof(WAVEHDR))
    #winmm.waveOutClose(hWaveOut)
    winmm.PlaySoundW.argtypes = w.LPCWSTR,w.HMODULE,w.DWORD
    winmm.PlaySoundW.restype = w.BOOL

    SND_FILENAME = 0x20000
    winmm.PlaySound(b"Sonido.wav", None, 0x20000)
    print("Reproducción terminada.")

# Llamar a la función para reproducir el archivo WAV
file_path = "Sonido.wav"  # Sustituye con la ruta de tu archivo WAV
play_wav(file_path)



