juegos = []

videojuegos = []

opcion = 0

while opcion != 5:

    print("----- MENU -----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion < 1 or opcion > 5:
        print("Opcion invalida")

    elif opcion == 1:
        nombre = input("Escribe el nombre del videojuego: ")
        videojuegos.append(nombre)
        print("se agrego nuevo videojuego")

    elif opcion == 2:
        if videojuegos == []:
            print("Aun no se registran videojuegos")
        else:
            for x in videojuegos:
                print(x)

    elif opcion == 3:
        nombre = input("Que videojuego quieres encontrar: ")
        if nombre in videojuegos:
            print("Videojuego encontrado")
        else:
            print("No esta en la lista loco")

    elif opcion == 4:
        nombre = input("Escribe el videojuego a eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado")
        else:
            print("No esta en la lista loco")

    elif opcion == 5:
        print("Programa finalizado")
