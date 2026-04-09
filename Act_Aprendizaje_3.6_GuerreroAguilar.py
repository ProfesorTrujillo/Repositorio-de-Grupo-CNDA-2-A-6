def cambio_minimo(cambio, monedas):
    """
    Función recursiva que devuelve la lista de monedas necesarias
    para dar el cambio exacto con la menor cantidad posible.
    """
    # Caso base: si el cambio es 0, no se necesitan monedas
    if cambio == 0:
        return []

    # Inicializamos con None para comparar después
    mejor_opcion = None

    # Probar cada moneda disponible
    for moneda in monedas:
        if moneda <= cambio:
            # Llamada recursiva reduciendo el cambio
            resultado = cambio_minimo(cambio - moneda, monedas)

            # Evaluar si esta opción es mejor (menos monedas)
            if mejor_opcion is None or len(resultado) + 1 < len(mejor_opcion):
                mejor_opcion = [moneda] + resultado

    return mejor_opcion


# Bloque principal
if __name__ == "__main__":
    # Entrada: monto de cambio y denominaciones
    cambio = int(input("Ingrese el monto de cambio: "))
    monedas = [1, 2, 5, 10, 20]

    # Procesamiento
    resultado = cambio_minimo(cambio, monedas)

    # Salida
    print("Cambio total:", cambio)
    print("Monedas utilizadas:", resultado)
