def cambio_minimo(cambio, monedas):
    # Caso base
    if cambio == 0:
        return []
    
    mejor_solucion = None

    for moneda in monedas:
        if moneda <= cambio:
            resultado = cambio_minimo(cambio - moneda, monedas)
            
            if resultado is not None:
                solucion = [moneda] + resultado
                
                if (mejor_solucion is None or 
                    len(solucion) < len(mejor_solucion)):
                    mejor_solucion = solucion

    return mejor_solucion


# Programa principal
cambio = 27
monedas = [1, 2, 5, 10, 20]

# Ordenamos de mayor a menor (mejora rendimiento)
monedas.sort(reverse=True)

resultado = cambio_minimo(cambio, monedas)

print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)
