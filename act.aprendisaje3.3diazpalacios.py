videojuegos = []
opcion = 0

def mostrar_menu():
    print("\n1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

while opcion != 5:
    mostrar_menu()
    opcion = int(input("Elige una opción (1-5): "))

    if opcion == 1:
        titulo_nuevo = input("Ingresa el nombre del videojuego: ")
        videojuegos.append(titulo_nuevo)
        print("Videojuego agregado")
        
    elif opcion == 2:
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("Lista de juegos:")
            for item in videojuegos:
                print(item)
                
    elif opcion == 3:
        busqueda = input("Nombre del videojuego a buscar: ")
        if busqueda in videojuegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")
            
    elif opcion == 4:
        item_a_borrar = input("Nombre del videojuego a eliminar: ")
        if item_a_borrar in videojuegos:
            videojuegos.remove(item_a_borrar)
            print("Videojuego eliminado.")
        else:
            print("No está en la lista.")
            
    elif opcion == 5:
        print("Programa finalizado.")
        
    else:
        print("Opción inválida.")
