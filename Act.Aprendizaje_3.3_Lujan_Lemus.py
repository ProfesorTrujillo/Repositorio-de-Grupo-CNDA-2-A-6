# Crear una lista vacía
videojuegos = []

# Pedir 3 nombres de videojuegos
for i in range(3):
    nombre = input(f"Ingrese el nombre del videojuego {i+1}: ")
    videojuegos.append(nombre)

# Mostrar el arreglo
print("Lista de videojuegos:")
print(videojuegos)