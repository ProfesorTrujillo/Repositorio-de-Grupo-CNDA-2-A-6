Videojuego = []

#creacion del menu
while True:
    print("--Menu--")
    print("1. Agregar un videojuego")
    print("2. Eliminar un videojuego")
    print("3. Mostrar la lista de videojuegos")
    print("4. Buscar un videojuego")
    print("5. Salir")

    #Eleccion del usuario
    opcion = int(input("Ingrese el numero de la opcion que desea realizar: "))  
    if opcion == 1:
        nuevo_videojuego = input("Ingrese el nombre del nuevo videojuego: ")
        Videojuego.append(nuevo_videojuego)
        print("Videojuego agregado exitosamente.")
    elif opcion == 2:
        if Videojuego:
            print("Lista de Videojuegos:")
            for i, v in enumerate(Videojuego, 1):
                print(f"{i}. {v}")
            try:
                indice = int(input("Ingrese el número del videojuego que desea eliminar: "))
                if 1 <= indice <= len(Videojuego):
                    eliminado = Videojuego.pop(indice - 1)
                    print(f"Videojuego '{eliminado}' eliminado exitosamente.")
                else:
                    print("Número no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print("La lista está vacía.")
    elif opcion == 3:
        if Videojuego:
            print("Lista de Videojuegos:")
            for i, v in enumerate(Videojuego, 1):
                print(f"{i}. {v}")
        else:
            print("La lista está vacía.")
    elif opcion == 4:
        if Videojuego:
            print("Lista de Videojuegos:")
            for i, v in enumerate(Videojuego, 1):
                print(f"{i}. {v}")
            try:
                indice = int(input("Ingrese el número del videojuego que desea buscar: "))
                if 1 <= indice <= len(Videojuego):
                    print(f"El videojuego en la posición {indice} es: '{Videojuego[indice - 1]}'")
                else:
                    print("Número no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print("La lista está vacía.")
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
        
