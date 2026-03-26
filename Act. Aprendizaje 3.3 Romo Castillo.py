# Crear lista vacía
videojuegos = []

# Pedir 3 nombres
for i in range(3):
    nombre = input(f"Ingresa el nombre del videojuego {i+1}: ")
    videojuegos.append(nombre)

# Mostrar la lista completa
print("\nLista de videojuegos:")
print(videojuegos)
