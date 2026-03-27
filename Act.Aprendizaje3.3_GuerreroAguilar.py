# Crear una lista vacía para almacenar los videojuegos
lista_juegos = []

print("Lista de Videojuegos Favoritos")

# Ciclo para pedir al usuario 4 videojuegos
for i in range(4):
    juego = input(f"Escribe el nombre del videojuego {i+1}: ")
    lista_juegos.append(juego)

# Mostrar los videojuegos que se registraron
print("\nLa lista inicial de videojuegos que ingresaste es:")
for juego in lista_juegos:
    print("-", juego)

# Iniciar el menú de opciones
opcion = 0
while opcion != 5:
    print("\n---- Menú de opciones ----")
    print("1. Agregar un videojuego")
    print("2. Mostrar lista completa de videojuegos")
    print("3. Buscar algún videojuego registrado")
    print("4. Eliminar videojuego de la lista")
    print("5. Salir del menú")

    # Pedir la opción del menú al usuario
    opcion = int(input("Elige una opción: "))

    # Opción 1: Agregar videojuego
    if opcion == 1:
        nuevo_juego = input("Escribe el nombre del videojuego que deseas agregar: ")
        lista_juegos.append(nuevo_juego)
        print("Videojuego agregado.")

    # Opción 2: Mostrar la lista de videojuegos
    elif opcion == 2:
        if len(lista_juegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("\nLista de videojuegos:")
            for juego in lista_juegos:
                print("-", juego)

    # Opción 3: Buscar videojuego en la lista
    elif opcion == 3:
        nombre = input("Escribe el videojuego a buscar: ")
        if nombre in lista_juegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")

    # Opción 4: Eliminar videojuego
    elif opcion == 4:
        eliminar_juego = input("Escribe el videojuego que quieres eliminar: ")
        if eliminar_juego in lista_juegos:
            lista_juegos.remove(eliminar_juego)
            print("Videojuego eliminado con éxito.")
        else:
            print("No está registrado en la lista.")

    # Opcion 5: Salir del programa
    elif opcion == 5:
        print("Programa finalizado,gracias! :)")

    else:
        print("Opcion inválida, ingresa una opción correcta.")
