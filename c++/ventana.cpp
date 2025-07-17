#include <windows.h>

// Declaración de la función de ventana (Window Procedure)
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    // Nombre de la clase de ventana
    const char CLASS_NAME[] = "VentanaEjemplo";

    // Estructura de la clase de ventana
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc; // Procedimiento de ventana
    wc.hInstance = hInstance;   // Identificador de la aplicación
    wc.lpszClassName = CLASS_NAME; // Nombre de la clase

    // Registrar la clase de ventana
    RegisterClass(&wc);

    // Crear la ventana
    HWND hwnd = CreateWindowEx(
        0,                          // Estilo extendido
        CLASS_NAME,                 // Nombre de la clase de ventana
        "Mi primera ventana",       // Título de la ventana
        WS_OVERLAPPEDWINDOW,        // Estilo de la ventana
        CW_USEDEFAULT, CW_USEDEFAULT, 800, 600, // Posición y tamaño
        NULL,                       // Sin ventana padre
        NULL,                       // Sin menú
        hInstance,                  // Identificador de la aplicación
        NULL                        // Sin parámetros adicionales
    );

    // Verificar si la ventana fue creada correctamente
    if (hwnd == NULL) {
        return 0;
    }

    // Mostrar la ventana
    ShowWindow(hwnd, nCmdShow);

    // Bucle de mensajes
    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

// Definición de la función de ventana
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
    case WM_DESTROY: // Cuando la ventana se cierra
        PostQuitMessage(0);
        return 0;

    case WM_PAINT: { // Cuando se necesita repintar la ventana
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);
        FillRect(hdc, &ps.rcPaint, (HBRUSH)(COLOR_WINDOW + 1));
        EndPaint(hwnd, &ps);
    } return 0;
    }

    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
