#Act._Aprendizaje_3.6_Trejo
def cambio_minimo(monto, monedas, desglose=None):
    if desglose is None:
        desglose = {m: 0 for m in monedas}

    if monto == 0:
        return 0, desglose
    
    if not monedas:
        return float("inf"), desglose

    moneda_actual = monedas[0]

    if monto >= moneda_actual:
        nuevo_desglose = desglose.copy()
        nuevo_desglose[moneda_actual] += 1
        cantidad, resultado = cambio_minimo(monto - moneda_actual, monedas, nuevo_desglose)
        return 1 + cantidad, resultado
    else:
        return cambio_minimo(monto, monedas[1:], desglose)

if __name__ == "__main__":
#monedas que si se permiten 
    denominaciones = [20, 10, 5, 2, 1]

    # Entrada para que el usuario ingresa la cantidad
    try:
        monto_cambio = int(input("Ingrese la cantidad de cambio a devolver: "))
        cantidad, desglose = cambio_minimo(monto_cambio, denominaciones)

        print(f"\nCambio total: {monto_cambio}")
        print(f"Cantidad mínima de monedas: {cantidad}")
        print("Desglose de monedas:")
        for moneda, num in desglose.items():
            if num > 0:
                print(f"{moneda}: {num}")
    except ValueError:
        print("Por favor ingrese un número entero válido.")