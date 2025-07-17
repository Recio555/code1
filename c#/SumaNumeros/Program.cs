using System;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            Console.WriteLine("Ingrese el primer número:");
            int numero1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Ingrese el segundo número:");
            int numero2 = int.Parse(Console.ReadLine());

            int suma = numero1 + numero2;
            Console.WriteLine($"La suma de {numero1} y {numero2} es {suma}");

            Console.WriteLine("¿Desea realizar otra operación? (s/n)");
            string respuesta = Console.ReadLine();
            if (respuesta.ToLower() != "s")
            {
                Console.WriteLine("Saliendo del programa...");
                break;
            }
        }
    }
}

