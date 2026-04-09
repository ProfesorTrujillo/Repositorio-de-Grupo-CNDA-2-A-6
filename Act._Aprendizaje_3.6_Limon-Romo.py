def cambio_minimo(cambio, monedas, i=0):
    # Caso base: cambio exacto
    if cambio == 0:
        return []
    
    # Caso base: sin monedas disponibles
    if i >= len(monedas):
        return None

    # Opción 1: usar la moneda actual (si se puede)
    usar = None
    if monedas[i] <= cambio:
        resultado_usar = cambio_minimo(cambio - monedas[i], monedas, i)
        if resultado_usar is not None:
            usar = [monedas[i]] + resultado_usar

    # Opción 2: no usar la moneda actual
    no_usar = cambio_minimo(cambio, monedas, i + 1)

    # Elegir la mejor opción (menos monedas)
    if usar is None:
        return no_usar
    if no_usar is None:
        return usar
    
    return usar if len(usar) < len(no_usar) else no_usar


# Programa principal
cambio = 27
monedas = [20, 10, 5, 2, 1]  # puedes cambiar el orden

resultado = cambio_minimo(cambio, monedas)

print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)
