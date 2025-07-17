import numpy as np
import matplotlib.pyplot as plt

def plot_hyperbola(c_values, x_range=(-5, 5), points=500):
    """
    Grafica la familia de hipérbolas x^2 - y^2 = c para diferentes valores de c.

    Parameters:
        c_values (list): Lista de valores de c para las hipérbolas.
        x_range (tuple): Rango de valores para x (xmin, xmax).
        points (int): Número de puntos en el rango de x.
    """
    x = np.linspace(x_range[0], x_range[1], points)

    plt.figure(figsize=(10, 8))

    for c in c_values:
        # Calcular las ramas de la hipérbola donde x^2 - c >= 0
        valid_mask = x**2 >= c
        x_valid = x[valid_mask]
        y_positive = np.sqrt(x_valid**2 - c)
        y_negative = -y_positive

        # Graficar las ramas de la hipérbola
        plt.plot(x_valid, y_positive, label=f'$c = {c}$', linewidth=2)
        plt.plot(x_valid, y_negative, linewidth=2)

    # Añadir ejes y detalles al gráfico
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.7)
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.7)
    plt.title('Familia de hipérbolas $x^2 - y^2 = c$', fontsize=14)
    plt.xlabel('$x$', fontsize=12)
    plt.ylabel('$y$', fontsize=12)
    plt.grid(alpha=0.4)
    plt.legend(fontsize=10)
    plt.axis('equal')  # Igualar proporciones de los ejes

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

# Lista de valores de c para graficar
c_values = [-4, -2, 0, 2, 4]
plot_hyperbola(c_values)

