#include <windows.h>
#include <mmsystem.h>
#pragma comment(lib, "winmm.lib") // Vincular la biblioteca winmm.lib

int main() {
    // Comando para abrir el archivo MP3
    mciSendString("open \"example.mp3\" type mpegvideo alias myMusic", NULL, 0, NULL);

    // Comando para reproducir el archivo
    mciSendString("play myMusic", NULL, 0, NULL);

    // Mantener el programa en ejecución mientras la música se reproduce
    MessageBox(NULL, "Presiona OK para detener la música", "Reproduciendo Música", MB_OK);

    // Detener y cerrar el archivo
    mciSendString("stop myMusic", NULL, 0, NULL);
    mciSendString("close myMusic", NULL, 0, NULL);

    return 0;
}
