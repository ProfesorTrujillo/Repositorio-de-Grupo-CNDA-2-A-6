print("--- Registro de Videojuegos ---")

videojuegos = []

for i in range(3):
    nombre = input("Ingresa un videojuego: ")
    videojuegos.append(nombre)

print("\nLista de videojuegos:")
for juego in videojuegos:
    print(juego)