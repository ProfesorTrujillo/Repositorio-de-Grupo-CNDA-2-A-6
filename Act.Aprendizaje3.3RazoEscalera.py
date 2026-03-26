videojuegos = []
seleccion = 0

def menu():
    print("\n1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

while seleccion != 5:
    menu()
    seleccion = int(input("Elige una opción (1-5): "))

    if seleccion == 1:
        agregado = input("Ingresa el nombre del videojuego: ")
        videojuegos.append(agregado)
        print("Videojuego agregado")
        
    elif seleccion == 2:
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("Lista de juegos:")
            for juego in videojuegos:
                print(juego)
                
    elif seleccion == 3:
        nombre_buscar = input("Nombre del videojuego a buscar: ")
        if nombre_buscar in videojuegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")
            
    elif seleccion == 4:
        nombre_eliminar = input("Nombre del videojuego a eliminar: ")
        if nombre_eliminar in videojuegos:
            videojuegos.remove(nombre_eliminar)
            print("Videojuego eliminado.")
        else:
            print("No está en la lista.")
            
    elif seleccion == 5:
        print("Programa finalizado.")
        
    else:
        print("Opción inválida.")
