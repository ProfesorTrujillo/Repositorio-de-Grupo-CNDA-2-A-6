videojuegos = []
for i in range(5):
      nombre = input("Ingrese un videojuego:")
      videojuegos.append(nombre)
      print("lista de videojuegos:", videojuegos)
  #creacion del menu
while True:
    print("Menu de opciones:")
    print("1. Agregar un videojuego")
    print("2. eliminar un videojuego")
    print("3. Mostrar la lista de videojuegos")
    print("4. buscar un videojuego")
    print("5. Salir")
    #solicitar opcion al usuario
    opcion = input("Ingrese una opcion:")
    if opcion == "1":
        nombre = input("Ingrese un videojuego:")
        videojuegos.append(nombre)
        print("lista de videojuegos:", videojuegos)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del videojuego a eliminar:")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("videojuego eliminado")
        else:
            print("videojuego no encontrado")
    elif opcion == "3":
        print("lista de videojuegos:", videojuegos)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del videojuego a buscar:")
        if nombre in videojuegos:
            print("videojuego encontrado")
        else:
            print("videojuego no encontrado")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intente de nuevo")
