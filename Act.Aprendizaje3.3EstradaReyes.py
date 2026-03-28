# Lista vacía para guardar videojuegos
videojuegos = []

# Variable para controlar el menú
opcion = 0

# Ciclo que se repite hasta que el usuario elija salir
while opcion != 5:

    # Mostrar menú
    print("----- MENÚ -----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    # Pedir opción al usuario
    opcion = int(input("Elige una opción: "))

    # Opción 1: Agregar videojuego
    if opcion == 1:
        nombre = input("Escribe un videojuego: ")
        videojuegos.append(nombre)  # Agrega a la lista
        print("Videojuego agregado")

    # Opción 2: Mostrar lista
    elif opcion == 2:
        if len(videojuegos) == 0:  # Verifica si está vacía
            print("No hay videojuegos")
        else:
            for juego in videojuegos:  # Recorre la lista
                print(juego)

    # Opción 3: Buscar videojuego
    elif opcion == 3:
        nombre = input("Buscar videojuego: ")
        if nombre in videojuegos:  # Verifica si existe
            print("Videojuego encontrado")
        else:
            print("No está en la lista")

    # Opción 4: Eliminar videojuego
    elif opcion == 4:
        nombre = input("Eliminar videojuego: ")
        if nombre in videojuegos:  # Verifica antes de eliminar
            videojuegos.remove(nombre)  # Elimina
            print("Eliminado")
        else:
            print("No está en la lista")

    # Opción 5: Salir
    elif opcion == 5:
        print("Programa finalizado")

    # Si la opción no es válida
    else:
        print("Opción inválida")
