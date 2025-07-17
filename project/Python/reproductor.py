# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import wave
import ctypes
import threading
import time
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ReproductorWaveOut:
    def __init__(self, archivo):
        self.archivo = archivo
        self.audio = wave.open(self.archivo, 'rb')

        if self.audio.getcomptype() != 'NONE':
            raise ValueError("Solo se admite audio PCM sin comprimir.")

        self.h_wave_out = ctypes.c_void_p()
        self.wave_format = self._crear_wave_format()
        self.buffer_size = 40096

        self._pausado = threading.Event()
        self._pausado.set()
        self._detenido = threading.Event()

        self.duracion = self.audio.getnframes() / float(self.audio.getframerate())
        self._abrir_dispositivo()

        self.is_playing = False
        self.thread = None
        self.posicion = 0

    def _crear_wave_format(self):
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

        formato = WAVEFORMATEX()
        formato.wFormatTag = 1
        formato.nChannels = self.audio.getnchannels()
        formato.nSamplesPerSec = self.audio.getframerate()
        formato.wBitsPerSample = self.audio.getsampwidth() * 8
        formato.nBlockAlign = (formato.nChannels * formato.wBitsPerSample) // 8
        formato.nAvgBytesPerSec = formato.nSamplesPerSec * formato.nBlockAlign
        formato.cbSize = 0
        return formato

    def _abrir_dispositivo(self):
        result = ctypes.windll.winmm.waveOutOpen(
            ctypes.byref(self.h_wave_out),
            -1,
            ctypes.byref(self.wave_format),
            0,
            0,
            0
        )
        if result != 0:
            raise RuntimeError(f"Error al abrir el dispositivo de audio: {result}")

    def _enviar_buffer(self, data):
        class WAVEHDR(ctypes.Structure):
            _fields_ = [
                ("lpData", ctypes.c_char_p),
                ("dwBufferLength", ctypes.c_uint),
                ("dwBytesRecorded", ctypes.c_uint),
                ("dwUser", ctypes.c_void_p),
                ("dwFlags", ctypes.c_uint),
                ("dwLoops", ctypes.c_uint),
                ("lpNext", ctypes.c_void_p),
                ("reserved", ctypes.c_void_p),
            ]

        buffer = ctypes.create_string_buffer(data)
        header = WAVEHDR()
        header.lpData = ctypes.cast(buffer, ctypes.c_char_p)
        header.dwBufferLength = len(data)
        header.dwFlags = 0

        ctypes.windll.winmm.waveOutPrepareHeader(self.h_wave_out, ctypes.byref(header), ctypes.sizeof(header))
        ctypes.windll.winmm.waveOutWrite(self.h_wave_out, ctypes.byref(header), ctypes.sizeof(header))

        while not (header.dwFlags & 0x00000001):
            if self._detenido.is_set():
                break
            time.sleep(0.001)

        ctypes.windll.winmm.waveOutUnprepareHeader(self.h_wave_out, ctypes.byref(header), ctypes.sizeof(header))

    def reproducir(self, desde_segundos=0):
        if not self.is_playing:
            self.is_playing = True
            self._detenido.clear()
            self._pausado.set()
            self.posicion = desde_segundos
            self.audio.setpos(int(desde_segundos * self.audio.getframerate()))
            self.thread = threading.Thread(target=self._reproducir_audio)
            self.thread.daemon = True
            self.thread.start()

    def _reproducir_audio(self):
        while self.is_playing and not self._detenido.is_set():
            self._pausado.wait()
            data = self.audio.readframes(self.buffer_size)
            if not data:
                break
            self._enviar_buffer(data)
            self.posicion += self.buffer_size / self.audio.getframerate()
        self.is_playing = False

    def pausar(self):
        if self.is_playing:
            self._pausado.clear()

    def reanudar(self):
        if self.is_playing:
            self._pausado.set()

    def detener(self):
        if self.is_playing:
            self._detenido.set()
            self._pausado.set()
            self.thread.join()
            self.is_playing = False

    def cerrar(self):
        self.detener()
        ctypes.windll.winmm.waveOutClose(self.h_wave_out)
        self.audio.close()

class ReproductorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor WAV")
        self.reproductor = None

        self.boton_cargar = ttk.Button(root, text="Cargar WAV", command=self.cargar_audio)
        self.boton_cargar.pack(pady=5)

        self.boton_play = ttk.Button(root, text="Reproducir", command=self.reproducir)
        self.boton_play.pack(pady=5)

        self.boton_pausa = ttk.Button(root, text="Pausar", command=self.pausar)
        self.boton_pausa.pack(pady=5)

        self.boton_reanudar = ttk.Button(root, text="Reanudar", command=self.reanudar)
        self.boton_reanudar.pack(pady=5)

        self.boton_detener = ttk.Button(root, text="Detener", command=self.detener)
        self.boton_detener.pack(pady=5)

        self.slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=self.saltar)
        self.slider.pack(fill='x', padx=10, pady=10)
        self.slider.set(0)

        self.label_tiempo = ttk.Label(root, text="0.00 / 0.00")
        self.label_tiempo.pack()

        self.actualizar_slider()

    def cargar_audio(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if ruta:
            if self.reproductor:
                self.reproductor.cerrar()
            self.reproductor = ReproductorWaveOut(ruta)
            self.slider.config(to=self.reproductor.duracion)
            self.slider.set(0)

    def reproducir(self):
        if self.reproductor:
            self.reproductor.reproducir(self.slider.get())

    def pausar(self):
        if self.reproductor:
            self.reproductor.pausar()

    def reanudar(self):
        if self.reproductor:
            self.reproductor.reanudar()

    def detener(self):
        if self.reproductor:
            self.reproductor.detener()

    def saltar(self, val):
        if self.reproductor and not self.reproductor.is_playing:
            self.slider.set(float(val))

    def actualizar_slider(self):
        if self.reproductor and self.reproductor.is_playing:
            self.slider.set(self.reproductor.posicion)
            self.label_tiempo.config(text=f"{self.reproductor.posicion:.2f} / {self.reproductor.duracion:.2f} s")
        self.root.after(200, self.actualizar_slider)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReproductorGUI(root)
    root.mainloop()
