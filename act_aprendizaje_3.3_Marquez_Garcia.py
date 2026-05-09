# menu con 3 videojuegos y opciones para agregar, eliminar, mutabilidad y mostrar el inventario
juegos = []
juegos.append(input("nombre del videojuego: "))
juegos.append(input("nombre del videojuego: "))
juegos.append(input("nombre del videojuego: "))
#crear menu para videojuegos
while True:
    print("\n MENÚ DE VIDEOJUEGOS")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Modificar")
    print("4. Mostrar")
    print("5. Salir")
#definir las opciones a elegir
    opcion = input("Elige opción: ")

    if opcion == "1":
        juegos.append(input("Nombre del videojuego: "))

    elif opcion == "2":
        print(juegos)
        try:
            i = int(input("Posición a eliminar: "))
            eliminado = juegos.pop(i)
            print("Se eliminó:", eliminado)
        except (IndexError, ValueError):
            print("Índice inválido")

    elif opcion == "3":
        print(juegos)
        try:
            i = int(input("Posición a modificar: "))
            juegos[i] = input("Nuevo nombre: ")
            print("Juego modificado.")
        except (IndexError, ValueError):
            print("Índice inválido")

    elif opcion == "4":
        print("Inventario:", juegos)

    elif opcion == "5":
        break

    else:
        print("Opción inválida")
#cierre de programa
print("Cerrando programa.")

