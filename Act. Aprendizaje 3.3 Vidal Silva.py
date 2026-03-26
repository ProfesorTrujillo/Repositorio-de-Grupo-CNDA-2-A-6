# Crear arreglo vacío
videojuegos = []

# Pedir 3 videojuegos para ser registrados 
for i in range(3):
    nombre = input(f"Ingrese el nombre del videojuego {i+1}: ")
    videojuegos.append(nombre)

# Muestra el arreglo completo con la lista de los videojuegos
print("\nLista de videojuegos:")
print(videojuegos)
