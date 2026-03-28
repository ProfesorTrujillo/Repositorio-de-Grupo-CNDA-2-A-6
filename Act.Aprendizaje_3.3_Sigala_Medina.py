"""
Escribe un programa en Python que:
Pida al usuario 3 nombres de videojuegos.
Los guarde en una lista.
Muestre la lista completa
INSTRUCCIONES PARA CREAR UN MENÚ EN PYTHON
----- MENÚ -----
1. Agregar videojuego
2. Mostrar lista completa
3. Buscar videojuego
4. Eliminar videojuego
5. Salir
El menú debe repetirse hasta que se elija 5. Salir.
3. Solicitar una opción al usuario
4. Usar un ciclo while para repetir el menú
El menú debe ejecutarse continuamente:
5. Usar condicionales if-elif-else
Mostrar mensaje: “Videojuego agregado”.
Opción 2: Mostrar la lista completa
Si la lista está vacía: mostrar “No hay videojuegos registrados”..
Mostrar cada videojuego en una línea.
Opción 3: Buscar videojuego
Pedir un nombre a buscar.
Revisar si existe en la lista con:
if nombre in videojuegos:
Si existe: “Videojuego encontrado”.
Si no: “No se encuentra en la lista”.
Opción 4: Eliminar videojuego
Pedir el nombre del videojuego.
Verificar si está en la lista.
Si existe: usar remove() para eliminarlo.
Si no existe: mostrar “No está en la lista”.
Opción 5: Salir
Mostrar: “Programa finalizado”.
Terminar el ciclo.
"""

# Crear una lista vacía para almacenar los nombres de los videojuegos
videojuegos = []
# Mostrar el menú y solicitar opciones al usuario
while True:
    print("\n----- MENÚ -----")
    print("1. Agregar videojuego")
    print("2. Mostrar lista completa")
    print("3. Buscar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        nombre = input("Ingresa el nombre del videojuego: ")
        videojuegos.append(nombre)
        print("Videojuego agregado.")
    elif opcion == '2':
        if not videojuegos:
            print("No hay videojuegos registrados.")
        else:
            print("Lista de videojuegos:")
            for juego in videojuegos:
                print(juego)
    elif opcion == '3':
        nombre = input("Ingresa el nombre del videojuego a buscar: ")
        if nombre in videojuegos:
            print("Videojuego encontrado.")
        else:
            print("No se encuentra en la lista.")
    elif opcion == '4':
        nombre = input("Ingresa el nombre del videojuego a eliminar: ")
        if nombre in videojuegos:
            videojuegos.remove(nombre)
            print("Videojuego eliminado.")
        else:
            print("No está en la lista.")   
    elif opcion == '5':
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")