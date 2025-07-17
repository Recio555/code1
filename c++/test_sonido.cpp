#include <windows.h>
#include <mmsystem.h>
#include <iostream>
#include <fstream>

#pragma comment(lib, "winmm.lib")

int main() {
    const char* filename = "Sonido.wav";

    // Abrir el archivo WAV
    std::ifstream file(filename, std::ios::binary);
    if (!file) {
        std::cerr << "No se pudo abrir el archivo.\n";
        return 1;
    }

    // Leer encabezado WAV (simplificado)
    char riff[4];
    file.read(riff, 4);
    if (strncmp(riff, "RIFF", 4) != 0) {
        std::cerr << "Formato incorrecto: no es un archivo RIFF.\n";
        return 1;
    }

    file.ignore(4); // Tamaño
    char wave[4];
    file.read(wave, 4);
    if (strncmp(wave, "WAVE", 4) != 0) {
        std::cerr << "No es un archivo WAVE.\n";
        return 1;
    }

    // Buscar el subchunk 'fmt '
    char chunkId[4];
    uint32_t chunkSize;
    while (true) {
        file.read(chunkId, 4);
        file.read(reinterpret_cast<char*>(&chunkSize), 4);
        if (strncmp(chunkId, "fmt ", 4) == 0) break;
        file.ignore(chunkSize);
    }

    WAVEFORMATEX wfx;
    file.read(reinterpret_cast<char*>(&wfx), sizeof(WAVEFORMATEX));

    // Saltar posibles bytes extra
    if (chunkSize > sizeof(WAVEFORMATEX))
        file.ignore(chunkSize - sizeof(WAVEFORMATEX));

    // Buscar el subchunk 'data'
    while (true) {
        file.read(chunkId, 4);
        file.read(reinterpret_cast<char*>(&chunkSize), 4);
        if (strncmp(chunkId, "data", 4) == 0) break;
        file.ignore(chunkSize);
    }

    // Leer los datos de audio
    char* audioData = new char[chunkSize];
    file.read(audioData, chunkSize);
    file.close();

    // Preparar el dispositivo de salida
    HWAVEOUT hWaveOut;
    if (waveOutOpen(&hWaveOut, WAVE_MAPPER, &wfx, 0, 0, CALLBACK_NULL) != MMSYSERR_NOERROR) {
        std::cerr << "No se pudo abrir el dispositivo de audio.\n";
        delete[] audioData;
        return 1;
    }

    // Preparar el header
    WAVEHDR header = {};
    header.lpData = audioData;
    header.dwBufferLength = chunkSize;
    header.dwFlags = 0;

    waveOutPrepareHeader(hWaveOut, &header, sizeof(WAVEHDR));
    waveOutWrite(hWaveOut, &header, sizeof(WAVEHDR));

    // Esperar hasta que termine la reproducción
    while (!(header.dwFlags & WHDR_DONE)) {
        Sleep(100);
    }

    // Limpiar
    waveOutUnprepareHeader(hWaveOut, &header, sizeof(WAVEHDR));
    waveOutClose(hWaveOut);
    delete[] audioData;

    std::cout << "Reproducción finalizada.\n";
    return 0;
}
