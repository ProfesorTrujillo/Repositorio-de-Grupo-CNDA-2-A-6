#PROGRAMA PARA PEDIR 3 NOMBRES Y GUARDARLOS EN UN ARREGLO 
videojuegos = []
for i in range(3):
    nombre = input("Ingrese el nombre de un videojuego: ")
    videojuegos(nombre)
print("Los videojuegos ingresados son:")
for juego in videojuegos:
    print(juego)
#.append sir