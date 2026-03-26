# Crear la lista vacía
videojuegos = []
opcion = 0

# ciclo while 
while opcion != 5:
    # 2. Mostrar el menú
    print("\n----- MENÚ -----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    # Solicitar la opción
    opcion = int(input("Elige una opción: "))

    # opciones con if-elif-else
    if opcion == 1:
        # Agregar
        nombre = input("Nombre del videojuego: ")
        videojuegos.append(nombre)
        print("Videojuego agregado.")

    elif opcion == 2:
        # Mostrar
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            for v in videojuegos:
                print(v)

    elif opcion == 3:
        # Buscar
        nombre = input("Nombre a buscar: ")
        if nombre in videojuegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")

    elif opcion == 4:
        # Eliminar
        nombre = input("Nombre a eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado.")
        else:
            print("No está en la lista.")

    elif opcion == 5:
        # Salir
        print("Programa finalizado.")

    else:
        # Opción fuera de rango
        print("Opción inválida.")
