#include <windows.h>
#include <mmsystem.h>
#include <iostream>
#include <fstream>

int main() {
    const char* filename = "Sonido.wav";

    // Verificar que el archivo existe
    std::ifstream f(filename);
    if (!f.good()) {
        std::cerr << "Archivo no encontrado: " << filename << std::endl;
        return 1;
    }

    // Intentar reproducirlo
    if (!PlaySoundA(filename, NULL, SND_FILENAME | SND_ASYNC)) {
        std::cerr << "PlaySound falló. ¿El archivo está en formato PCM?" << std::endl;
        return 1;
    }

    std::cout << "Reproduciendo " << filename << "..." << std::endl;
    Sleep(5000);
    PlaySound(NULL, NULL, 0);  // Detener

    return 0;
}

