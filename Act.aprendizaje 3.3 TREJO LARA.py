#Trabajando con Arreglos
cantidad = int(input("¿Cuántos videojuegos deseas ingresar? "))
juegos = []
for i in range(cantidad):
     juego = input("ingresa el nombre del videojuego {}: ".format(i+1))
     juegos.append(juego)
print("Los videojuegos ingresados son:", juegos)
 