

# 1. Crear la lista vacía
videojuegos = []

# 2. Variable para el menú
opcion = 0

# 3. Ciclo principal
while opcion != 5:

    # Mostrar menú
    print("\n MENÚ ")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    # Pedir opción
    opcion = int(input("Elige una opción: "))

    # Opción 1: Agregar 
    if opcion == 1:
        nombre = input("Escribe el nombre del videojuego: ")
        videojuegos.append(nombre)
        print("Videojuego agregado.")

    # Opción 2: Mostrar 
    elif opcion == 2:
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("\nLista de videojuegos:")
            for juego in videojuegos:
                print("-", juego)

    # Opción 3: Buscar 
    elif opcion == 3:
        nombre = input("Escribe el nombre a buscar: ")
        if nombre in videojuegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")

    #Opción 4: Eliminar 
    elif opcion == 4:
        nombre = input("Escribe el nombre a eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado.")
        else:
            print("No está en la lista.")

    # Opción 5: Salir 
    elif opcion == 5:
        print("Programa finalizado.")

    # Opción inválida 
    else:
        print("Opción inválida.")
