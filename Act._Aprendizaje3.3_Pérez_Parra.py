# 1. Iniciamos con la lista vacía 
videojuegos = []
opcion = 0

# 4. Ciclo while para que el menú se repita hasta que se elija la opción 5
while opcion != 5:
    # 2. Mostramos el menú
    print("\nMENÚ")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")
    
    # 3. Solicitamos la opción y validamos
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Por favor introduce un número.")
        continue # Reinicia el ciclo si no es un número

    if opcion < 1 or opcion > 5:
        print("Opción inválida.")
        continue

    # 5. Condicionales para cada acción
    if opcion == 1:
        # Agregar videojuego al arreglo
        nombre = input("Nombre del videojuego a agregar: ")
        videojuegos.append(nombre)
        print("Videojuego agregado.")

    elif opcion == 2:
        # Mostrar lista
        if not videojuegos: # Validación de lista vacía
            print("No hay videojuegos registrados.")
        else:
            print("Lista de Videojuegos")
            for juego in videojuegos:
                print(f"- {juego}")

    elif opcion == 3:
        # Buscar videojuego en la lista
        nombre_buscar = input("Nombre del videojuego a buscar: ")
        if nombre_buscar in videojuegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")

    elif opcion == 4:
        # Eliminar un videojuego de la lista
        nombre_eliminar = input("Nombre del videojuego a eliminar: ")
        if nombre_eliminar in videojuegos:
            videojuegos.remove(nombre_eliminar)
            print(f"'{nombre_eliminar}' ha sido eliminado.")
        else:
            print("No está en la lista.")

    elif opcion == 5:
        # Exit
        print("Programa finalizado.")
