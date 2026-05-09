def cambio_minimo(cambio, monedas, memo=None):
    if memo is None:
        memo = {}

    # Caso base
    if cambio == 0:
        return []

    # Si ya lo calculamos
    if cambio in memo:
        return memo[cambio]

    mejor = None

    for moneda in monedas:
        if moneda <= cambio:
            resultado = cambio_minimo(cambio - moneda, monedas, memo)

            if resultado is not None:
                actual = [moneda] + resultado

                if mejor is None or len(actual) < len(mejor):
                    mejor = actual

    memo[cambio] = mejor
    return mejor


# ===== PROGRAMA PRINCIPAL =====
try:
    cambio = int(input("Ingresa el monto de cambio: "))
    entrada = input("Ingresa las monedas separadas por coma (ej: 1,2,5,10,20): ")

    monedas = [int(x.strip()) for x in entrada.split(",")]
    monedas.sort(reverse=True)

    resultado = cambio_minimo(cambio, monedas)

    print("\n--- RESULTADO ---")
    print("Cambio total:", cambio)

    if resultado is None:
        print("No se puede dar cambio con esas monedas.")
    else:
        print("Monedas utilizadas:", resultado)
        print("Cantidad mínima de monedas:", len(resultado))

except ValueError:
    print("Error: Ingresa solo números válidos.")
