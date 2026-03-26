
def menu():
    print("-----Menu-----")
    print("1.-Agregar videojuego ")
    print("2.-Mostrar lista complta")
    print("3.-Buscar videojuego")
    print("4.-Eliminar videojuego")
    print("5.-salir ")
videojuegos = ["minecraft", "free fire", "warzone"]
while True:
    menu()
    o = input("Selecciona alguna opcion ")
    if o == "5":
        print ("Saliendo del programa ")
        break
    match o:
        case "1":
            videojuegos.append(input("Ingresa el nombre del videojuego"))
        case "2":
            print("la lista de los juegos es: ",videojuegos)
        case "3":
            n = input("ingresa el nombre del juego")
            if n in videojuegos:
                print("el videojuego se encontro")
            else:
                print("el videojuego no se encontro")
        case "4":
            videojuegos.remove(input("ingresa el nombre del videojuego que vas a eliminar"))
        case _:
            print("opción no valida ")
