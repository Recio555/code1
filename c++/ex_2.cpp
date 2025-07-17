#include <iostream>
#include <list>
using namespace std;

// Definición de una función que suma dos números
int suma(int a, int b) {
    return a + b;
}

void log(string mensaje){
     cout << "Hola, " << mensaje << "!" << endl;
}
void log2(string mensaje){
     cout << "Hola, " << mensaje << "!" << endl;
}

int main() {
    
    log("hola mundo") ;
    list<string> primero;
    //primero ={"se puede haceder dede una lista", log("HOLA"),log2};
    system("pause");
    return 0;
}

