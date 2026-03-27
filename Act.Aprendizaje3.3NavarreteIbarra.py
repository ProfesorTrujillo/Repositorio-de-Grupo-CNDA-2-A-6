videojuegos = []
print(" ingresa 3 videojuegos:")
for i in range(3):
    nombre = input(f"Ingrese el nombre del videojuego {i+1}: ")
    videojuegos = videojuegos + [nombre]

print("Los videojuegos iniciales son:")
for juego in videojuegos:
    print(juego)

while True:
    print("\n¿Quieres cambiar la lista o salir?")
    print("1. Cambiar")
    print("2. Salir")
    opcion_principal = input("Elige una opción: ")
    if opcion_principal == "1":
        while True:
            print("\nSubmenú de cambios:")
            print("1. Agregar videojuego")
            print("2. Quitar videojuego")
            print("3. Mostrar lista")
            print("4. Volver al menú principal")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                nombre = input("Ingrese el nombre del videojuego: ")
                videojuegos = videojuegos + [nombre]
            elif opcion == "2":
                if videojuegos:
                    print("Lista actual:")
                    for i, juego in enumerate(videojuegos):
                        print(f"{i+1}. {juego}")
                    indice = int(input("Ingrese el número del videojuego a quitar: ")) - 1
                    if 0 <= indice < len(videojuegos):
                        videojuegos = videojuegos[:indice] + videojuegos[indice+1:]
                    else:
                        print("Número inválido")
                else:
                    print("La lista está vacía")
            elif opcion == "3":
                print("Los videojuegos en la lista son:")
                for juego in videojuegos:
                    print(juego)
            elif opcion == "4":
                break
            else:
                print("Opción inválida")
    elif opcion_principal == "2":
        break
    else:
        print("Opción inválida")
