import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear una cuadrícula de valores para x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calcular z = x^2 - y^2
Z = X**2 - Y**2

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Añadir etiquetas y título
ax.set_title('Gráfico de $z = x^2 - y^2$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Añadir una barra de color
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Mostrar el gráfico
plt.show()
