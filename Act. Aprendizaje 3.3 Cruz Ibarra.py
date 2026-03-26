opcion = 0
videojuegos = []

while opcion != 5:
    print("\n----- MENÚ -----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")
    opcion = int(input("Elige una opción: "))
    
if opcion == 1:
        nombre=input("Dame el nombre del videojuego: ")
        videojuegos.append(nombre)
        print("Agregado")
        
elif opcion == 2:
    if videojuegos == []:
      print("lista vacia")
    else:
        for x in videojuegos:
            print(x)
elif opcion == 3:
    buscar=input("Buscar: ")
    if buscar in videojuegos:
        print("Si esta")
    else:
        print("No esta")
        
elif opcion == 4:
        eliminar = input("Eliminar: ")
        if eliminar in videojuegos:
            videojuegos.remove(eliminar)
            print("Eliminado")
        else:
            print("No está")
elif opcion == 5:
        print("Fin")
        
