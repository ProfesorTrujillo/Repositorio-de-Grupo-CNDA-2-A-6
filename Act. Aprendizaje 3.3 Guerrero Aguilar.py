# Crear una lista vacía para almacenar los videojuegos
lista_juegos = []

print("Lista de Videojuegos Favoritos")

# Ciclo para pedir al usuario 4 videojuegos
for i in range(3):
    juego = input(f"Escribe el nombre del videojuego {i+1}: ")

    # Guardar el videojuego dentro de la lista
    lista_juegos.append(juego)

# Mostrar los videojuegos que se registraron
print("\nLos videojuegos que ingresaste son:")

# Mostrar la lista de los videojuegos uno por uno
for juego in lista_juegos:
    print("-", juego)