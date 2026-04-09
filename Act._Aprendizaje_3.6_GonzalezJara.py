def cambio_minimo(monto, monedas, desglose=None):
    """
    Algoritmo recursivo para calcular el cambio con la menor cantidad de monedas.
    monto: cantidad de dinero a devolver
    monedas: lista de denominaciones disponibles (ej. [20, 10, 5, 2, 1])
    desglose: diccionario para registrar cuántas monedas de cada tipo se usan
    """
    if desglose is None:
        desglose = {m: 0 for m in monedas}

    # Caso base: si el monto es 0, ya no necesitamos más monedas
    if monto == 0:
        return 0, desglose

    # Si no hay monedas disponibles, no se puede dar cambio
    if not monedas:
        return float("inf"), desglose

    moneda_actual = monedas[0]

    if monto >= moneda_actual:
        desglose[moneda_actual] += 1
        cantidad, desglose = cambio_minimo(monto - moneda_actual, monedas, desglose)
        return 1 + cantidad, desglose
    else:
        return cambio_minimo(monto, monedas[1:], desglose)

if __name__ == "__main__":
    denominaciones = [20, 10, 5, 2, 1]

    precio = int(input("Ingrese el precio de la compra: "))
    pago = int(input("Ingrese el billete con el que paga el cliente: "))

    cambio = pago - precio

    if cambio < 0:
        print("\nEl pago es insuficiente, faltan", abs(cambio), "pesos.")
    elif cambio == 0:
        print("\nNo se necesita dar cambio.")
    else:
        print(f"\nEl cambio a devolver es: {cambio} pesos")

        cantidad, desglose = cambio_minimo(cambio, denominaciones)

        print(f"Cantidad mínima de monedas: {cantidad}")
        print("Desglose de monedas:")
        for moneda, num in desglose.items():
            if num > 0:
                print(f"{moneda}: {num}")
