# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:12:13 2024

@author: usuario
"""

import wave
import winsound
import time
import threading

class ReproductorDesdeCero:
    def __init__(self, archivo):
        self.archivo = archivo
        self.audio = wave.open(self.archivo, 'rb')
        self.pausado = False
        self.posicion_actual = 0
        self.hilo_reproduccion = None
        self.terminado = False

    def reproducir(self):
        """Inicia la reproducción en un hilo."""
        if not self.hilo_reproduccion or not self.hilo_reproduccion.is_alive():
            self.terminado = False
            self.hilo_reproduccion = threading.Thread(target=self._reproducir_audio)
            self.hilo_reproduccion.daemon = True
            self.hilo_reproduccion.start()

    def _reproducir_audio(self):
        """Lógica interna para manejar la reproducción."""
        while not self.terminado:
            if not self.pausado:
                data = self.audio.readframes(1024)
                if not data:
                    break
                #winsound.PlaySound(self.archivo, winsound.SND_FILENAME)
                winsound.PlaySound(data, winsound.SND_MEMORY)
                self.posicion_actual = self.audio.tell()
            else:
                time.sleep(0.1)
        if not self.terminado:
            self.detener()

    def pausar(self):
        """Pausar la reproducción."""
        if not self.pausado:
            self.pausado = True
            print("Reproducción pausada.")

    def reanudar(self):
        """Reanudar la reproducción."""
        if self.pausado:
            self.pausado = False
            print("Reanudando reproducción.")

    def detener(self):
        """Detener la reproducción."""
        self.terminado = True
        print("Reproducción detenida.")
        self.posicion_actual = 0

# Uso del reproductor
if __name__ == "__main__":
    archivo_audio = "Sonido.wav"
    reproductor = ReproductorDesdeCero(archivo_audio)

    print("Iniciando reproducción...")
    reproductor.reproducir()
    time.sleep(20)

    print("Pausando...")
    reproductor.pausar()
    time.sleep(20)

    print("Reanudando...")
    reproductor.reanudar()
    time.sleep(50)

    print("Deteniendo...")
    reproductor.detener()
