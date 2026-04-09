def cambio_minimo(monto, monedas):
    monedas.sort(reverse=True)  # Ordenamos de mayor a menor
    resultado = []

    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)

    return resultado


# Programa principal 
monedas = [1, 2, 5, 10, 20]

monto = int(input("Ingresa el cambio a devolver: "))

resultado = cambio_minimo(monto, monedas)

print("Cambio total:", sum(resultado))
print("Monedas utilizadas:", resultado)
print("Cantidad de monedas:", len(resultado))