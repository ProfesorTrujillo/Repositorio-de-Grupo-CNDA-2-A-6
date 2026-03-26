videojuegos = []

def menu():
    print("---- Menu de Videojuegos ----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista de videojuegos")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

opcion = 0

while opcion != 5:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        videojuego = input("Ingrese el nombre del videojuego: ")
        videojuegos.append(videojuego)

    elif opcion == 2:
        print("Lista de videojuegos:")
        for videojuego in videojuegos:
            print(videojuego)

    elif opcion == 3:
        buscar = input("Ingrese el nombre del videojuego a buscar: ")
        if buscar in videojuegos:
            print("El videojuego se encuentra en la lista.")
        else:
            print("El videojuego no se encuentra en la lista.")

    elif opcion == 4:
        eliminar = input("Ingrese el nombre del videojuego a eliminar: ")
        if eliminar in videojuegos:
            videojuegos.remove(eliminar)
            print("El videojuego ha sido eliminado.")
        else:
            print("El videojuego no se encuentra en la lista.")

    elif opcion == 5:
        print("Saliendo del programa...")

    else:
        print("Opcion no valida. Por favor, ingrese una opcion del 1 al 5.")
