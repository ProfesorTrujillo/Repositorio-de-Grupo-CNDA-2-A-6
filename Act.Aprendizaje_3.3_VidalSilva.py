
videojuegos = []

opcion = 0

while opcion != 5:

    print("\n----- MENÚ -----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    opcion = int(input("Elige una opción, por favor: "))

    if opcion < 1 or opcion > 5:
        print("Opción inválida")

    elif opcion == 1:
        nombre = input("Ingresa el nombre del videojuego: ")
        videojuegos.append(nombre)
        print("Videojuego agregado")

    elif opcion == 2:
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados")
        else:
            print("\nLista de videojuegos:")
            for juego in videojuegos:
                print(juego)

    elif opcion == 3:
        nombre = input("Ingresa el videojuego a buscar: ")
        if nombre in videojuegos:
            print("Videojuego encontrado")
        else:
            print("No se encuentra en la lista")

    elif opcion == 4:
        nombre = input("Ingresa el videojuego a eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado")
        else:
            print("No está en la lista")

    elif opcion == 5:
        print("Programa finalizado")

    elif opcion == 5:
        print("Programa finalizado")
