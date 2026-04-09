def cambio_minimo(cambio, monedas):
    if cambio == 0:
        return []
    if not monedas:
        return None
    moneda = monedas[0]
    if moneda > cambio:
        return cambio_minimo(cambio, monedas[1:])
    usar = cambio_minimo(cambio - moneda, monedas)
    if usar is not None:
        usar = [moneda] + usar
    no_usar = cambio_minimo(cambio, monedas[1:])
    if usar is None:
        return no_usar
    if no_usar is None:
        return usar
    if len(usar) < len(no_usar):
        return usar
    return no_usar

cambio = 27
monedas = [20, 10, 5, 2, 1]
resultado = cambio_minimo(cambio, monedas)
print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)