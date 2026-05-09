# Trabajando con Arreglos

videojuegos = []

opcion = ""
while opcion != "5":
    print("\n----- MENÚ -----")
    print("1. Agregar videojuego")
    print("2. Mostrar la lista")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")
    
    opcion = input("Elige un número: ")

    if opcion == "1":
        juego = input("Ingresa el nombre del videojuego: ")
        videojuegos.append(juego)
        print("Videojuego agregado.")

    elif opcion == "2":
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("\nLista de videojuegos:")
            for idx, nombre in enumerate(videojuegos, start=1):
                print(f"{idx}. {nombre}")

    elif opcion == "3":
        nombre = input("Ingresa el nombre del videojuego a buscar: ")
        if nombre in videojuegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")

    elif opcion == "4":
        nombre = input("Ingresa el nombre del videojuego a eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado.")
        else:
            print("No está en la lista.")

    elif opcion == "5":
        print("Programa finalizado.")

    else:
        print("Opción inválida. Intenta de nuevo.")