'''Trabajando con Arreglos
Enunciado
Escribe un programa en Python que:
Pida al usuario 3 nombres de videojuegos.
Los guarde en un arreglo.
Muestre el arreglo completo.
 '''
videojuegos = []

while True:
    print("---Menú---")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    opcion = input("Escoja lo que desea hacer: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del videojuego: ")
        videojuegos.append(nombre)
        print("Se agregó exitosamente.")

    elif opcion == "2":
        print("Esta es la lista completa de videojuegos:")
        print(videojuegos)

    elif opcion == "3":
        nombre = input("Ingresa el videojuego que buscas: ")
        if nombre in videojuegos:
            print("Videojuego encontrado:", nombre)
        else:
            print("No está en la lista.")

    elif opcion == "4":
        nombre = input("Ingresa el videojuego que deseas eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado:", nombre)
        else:
            print("No está en la lista.")

    elif opcion == "5":
        print("Adiós, gracias por usar este programa.")
        break
