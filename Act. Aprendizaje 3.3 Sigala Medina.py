"""
Escribe un programa en Python que:
Pida al usuario 3 nombres de videojuegos.
Los guarde en una lista.
Muestre la lista completa

"""
# Crear una lista vacía para almacenar los nombres de los videojuegos
videojuegos = []    
# Pedir al usuario que ingrese 3 nombres de videojuegos
for i in range(3):
    nombre = input(f"Ingresa el nombre del videojuego {i+1}: ")
    videojuegos.append(nombre)  # Agregar el nombre a la lista
# Mostrar la lista completa de videojuegos
print("Los videojuegos que ingresaste son:")
for juego in videojuegos:
    print(juego)  