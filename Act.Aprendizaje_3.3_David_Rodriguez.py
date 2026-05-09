#Crear lista vacía de videojuegos
videojuegos = []

#Pedir 3 videojuegos al mendigo usuario (es comeia profe)
print("Ingresa 3 videojuegos:")
for i in range(3):
    nombre = input(f"Videojuego {i+1}: ")
    videojuegos.append(nombre)

#Mostrar arreglo completo
print("Lista inicial de videojuegos:")
for juego in videojuegos:
    print(juego)

#Agregar el menu a la pantalla
opcion = 0
while opcion != 5:
    
    print("----- MENÚ -----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")
    
#Aqui se le pide al usuario que elija una opción del menu
    try:
        opcion = int(input("Elige una opción: "))
    except:
        print("Opción inválida")
        continue
    
#Esto es por si el usuario elije un numero mayor a las opciónes disponibles
    if opcion < 1 or opcion > 5:
        print("Opción inválida")
    
#Aqui vamos a dividir las opciónes del menu 
#Agregar
    elif opcion == 1:
        nombre = input("Ingresa el nombre del videojuego: ")
        videojuegos.append(nombre)
        print("Videojuego agregado")
    
#Mostrar lista completa
    elif opcion == 2:
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados")
        else:
            print("\nLista de videojuegos:")
            for juego in videojuegos:
                print(juego)
    
#Buscar el pishi videojuego
    elif opcion == 3:
        nombre = input("Ingresa el videojuego a buscar: ")
        if nombre in videojuegos:
            print("Videojuego encontrado")
        else:
            print("No se encuentra en la lista")
    
#Eliminar el videojuego jeje
    elif opcion == 4:
        nombre = input("Ingresa el videojuego a eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado")
        else:
            print("No está en la lista")
    
#Salir del programa o no se XD
    elif opcion == 5:
        print("Programa finalizado")