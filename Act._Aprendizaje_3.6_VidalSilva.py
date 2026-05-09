# Act._Aprendizaje_3.6_VidalSilva

def cambio_minimo(cambio, monedas):
# Caso base
    if cambio == 0:
        return []

    mejor = None

    for moneda in monedas:
        if moneda <= cambio:
#FUNCIÓN RECURSIVA
            resultado = cambio_minimo(cambio - moneda, monedas)

            if resultado is not None:
                combinacion = [moneda] + resultado

#Elegir la menor cantidad de monedas
                if mejor is None or len(combinacion) < len(mejor):
                    mejor = combinacion

    return mejor
#Corre el programa 
monedas = [1, 2, 5, 10, 20]
cambio = 27

resultado = cambio_minimo(cambio, monedas)

print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)

#para pruebas diferentes 
for c in [13, 8, 19]:
    print("\nCambio total:", c)
    print("Monedas utilizadas:", cambio_minimo(c, monedas))
