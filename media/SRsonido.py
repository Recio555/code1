# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 18:19:55 2025

@author: usuario
"""

import wave
import ctypes
import threading
import time
import os

class ReproductorWaveOut:
    def __init__(self, archivo):
        if not os.path.exists(archivo):
            raise FileNotFoundError(f"Archivo no encontrado: {archivo}")

        self.archivo = archivo
        self.audio = wave.open(self.archivo, 'rb')
        
        if self.audio.getcomptype() != 'NONE':
            raise ValueError("Solo se admite audio PCM sin comprimir.")

        self.h_wave_out = ctypes.c_void_p()
        self.thread = None
        self.is_playing = False

        # Eventos para pausar y detener
        self._pausado = threading.Event()
        self._pausado.set()  # No pausado al inicio
        self._detenido = threading.Event()

        self.wave_format = self._crear_wave_format()
        self.buffer_size = 40096
        self._abrir_dispositivo()

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
        formato.wFormatTag = 1  # PCM
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

        try:
            while not (header.dwFlags & 0x00000001):  # WHDR_DONE
                if self._detenido.is_set():
                    break
                time.sleep(0.001)
        finally:
            ctypes.windll.winmm.waveOutUnprepareHeader(self.h_wave_out, ctypes.byref(header), ctypes.sizeof(header))

    def reproducir(self):
        if not self.is_playing:
            self.is_playing = True
            self._detenido.clear()
            self._pausado.set()
            self.thread = threading.Thread(target=self._reproducir_audio)
            self.thread.daemon = True
            self.thread.start()

    def _reproducir_audio(self):
        self.audio.rewind()
        while self.is_playing and not self._detenido.is_set():
            self._pausado.wait()  # Espera si está en pausa

            data = self.audio.readframes(self.buffer_size)
            if not data:
                break

            self._enviar_buffer(data)

        self.is_playing = False

    def pausar(self):
        if self.is_playing and self._pausado.is_set():
            self._pausado.clear()
            print("Reproducción pausada.")

    def reanudar(self):
        if self.is_playing and not self._pausado.is_set():
            self._pausado.set()
            print("Reanudando reproducción.")

    def detener(self):
        if self.is_playing:
            self._detenido.set()
            self._pausado.set()
            if self.thread and self.thread.is_alive():
                self.thread.join()
            self.is_playing = False
            print("Reproducción detenida.")

    def cerrar(self):
        self.detener()
        ctypes.windll.winmm.waveOutClose(self.h_wave_out)
        self.audio.close()
        print("Dispositivo de audio cerrado.")

# Ejemplo de uso
if __name__ == "__main__":
    archivo_audio = "Sonido.wav"  # Reemplazá con la ruta real
    reproductor = ReproductorWaveOut(archivo_audio)

    print("Iniciando reproducción...")
    reproductor.reproducir()
    time.sleep(7)

    print("Pausando...")
    reproductor.pausar()
    time.sleep(3)

    print("Reanudando...")
    reproductor.reanudar()
    time.sleep(5)

    print("Deteniendo...")
    reproductor.detener()

    reproductor.cerrar()
