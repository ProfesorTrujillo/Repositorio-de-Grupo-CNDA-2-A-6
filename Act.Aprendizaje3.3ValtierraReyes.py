
#
videojuegos = []

for i in range(3):
    nombre = input("Ingresa un videojuego: ")
    videojuegos.append(nombre)

print("Lista:", videojuegos)

opcion = 0
while opcion != 5:
    print("\n1.Agregar  2.Mostrar  3.Buscar  4.Eliminar  5.Salir")
    opcion = int(input("Elige: "))

    if opcion == 1:
        videojuegos.append(input("Nombre: "))

    elif opcion == 2:
        print(videojuegos if videojuegos else "Lista vacía")

    elif opcion == 3:
        nombre = input("Buscar: ")
        print("Sí está" if nombre in videojuegos else "No está")

    elif opcion == 4:
        nombre = input("Eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
        else:
            print("No existe")

    elif opcion == 5:
        print("Fin")
