# 1. Creamos un arreglo vacío para empezar
videojuegos = []

print("--- Registro de Videojuegos ---")

# 2. Usamos un ciclo para pedir los datos 3 veces
for i in range(3):
    nombre = input(f"Introduce el nombre del videojuego {i+1}: ")
    
    # 3. Guardamos el nombre en nuestro arreglo
    videojuegos.append(nombre)

# 4. Mostramos el arreglo completo
print("\nTu lista de videojuegos es:")
print(videojuegos)