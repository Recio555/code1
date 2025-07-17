# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:40:34 2024

@author: usuario
"""

import wave
import ctypes
import threading
import time

class ReproductorWaveOut:
    def __init__(self, archivo):
        self.archivo = archivo
        self.audio = wave.open(self.archivo, 'rb')
        self.h_wave_out = ctypes.c_void_p()
        self.is_playing = False
        self.is_paused = False
        self.thread = None

        # Configuración del formato de audio
        self.wave_format = self._crear_wave_format()

        # Tamaño del bloque de datos a enviar
        self.buffer_size = 40096  # Ajustar según la calidad deseada

        # Iniciar el dispositivo de audio
        self._abrir_dispositivo()

    def _crear_wave_format(self):
        """Crea la estructura de formato WAVEFORMATEX necesaria."""
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
        """Abre el dispositivo de audio."""
        result = ctypes.windll.winmm.waveOutOpen(
            ctypes.byref(self.h_wave_out),
            -1,  # Dispositivo por defecto
            ctypes.byref(self.wave_format),
            0,
            0,
            0
        )
        if result != 0:
            raise RuntimeError(f"Error al abrir el dispositivo de audio: {result}")

    def _enviar_buffer(self, data):
        """Envía datos de audio al dispositivo usando WAVEHDR."""
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

        # Preparar el encabezado
        ctypes.windll.winmm.waveOutPrepareHeader(self.h_wave_out, ctypes.byref(header), ctypes.sizeof(header))

        # Escribir el buffer al dispositivo
        ctypes.windll.winmm.waveOutWrite(self.h_wave_out, ctypes.byref(header), ctypes.sizeof(header))

        # Esperar a que termine la reproducción del bloque
        while not (header.dwFlags & 0x00000001):  # WHDR_DONE
            time.sleep(0.001)

        # Liberar el encabezado
        ctypes.windll.winmm.waveOutUnprepareHeader(self.h_wave_out, ctypes.byref(header), ctypes.sizeof(header))

    def reproducir(self):
        """Inicia la reproducción en un hilo."""
        if not self.is_playing:
            self.is_playing = True
            self.is_paused = False
            self.thread = threading.Thread(target=self._reproducir_audio)
            self.thread.daemon = True
            self.thread.start()

    def _reproducir_audio(self):
        """Lógica de reproducción."""
        self.audio.rewind()
        while self.is_playing:
            if self.is_paused:
                time.sleep(0.01)
                continue

            data = self.audio.readframes(self.buffer_size)
            if not data:
                break
            self._enviar_buffer(data)

        self.is_playing = False

    def pausar(self):
        """Pausa la reproducción."""
        if self.is_playing:
            self.is_paused = True
            print("Reproducción pausada.")

    def reanudar(self):
        """Reanuda la reproducción."""
        if self.is_paused:
            self.is_paused = False
            print("Reanudando reproducción.")

    def detener(self):
        """Detiene la reproducción."""
        self.is_playing = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
        print("Reproducción detenida.")

    def cerrar(self):
        """Cierra el dispositivo de audio y libera recursos."""
        self.detener()
        ctypes.windll.winmm.waveOutClose(self.h_wave_out)
        self.audio.close()
        print("Dispositivo de audio cerrado.")

# Uso del reproductor
if __name__ == "__main__":
    archivo_audio = "Sonido.wav"  # Reemplaza con la ruta real
    #reproductor = ReproductorWaveOut(archivo_audio)

    #print("Iniciando reproducción...")
    #reproductor.reproducir()
    #time.sleep(5)

    #print("Pausando...")
    #reproductor.pausar()
    #time.sleep(3)

    #print("Reanudando...")
    #reproductor.reanudar()
    #time.sleep(5)

    #print("Deteniendo...")
    #reproductor.detener()

    #reproductor.cerrar()
