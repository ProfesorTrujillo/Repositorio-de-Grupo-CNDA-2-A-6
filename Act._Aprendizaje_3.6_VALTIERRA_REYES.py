def cambio_minimo(cambio, monedas, memo={}):
    if cambio == 0:
        return []
    if cambio < 0:
        return None
    if cambio in memo:
        return memo[cambio]
    mejor = None
    for moneda in sorted(monedas, reverse=True):
        resultado = cambio_minimo(cambio - moneda, monedas, memo)
        if resultado is not None:
            opcion = [moneda] + resultado
            if mejor is None or len(opcion) < len(mejor):
                mejor = opcion
    memo[cambio] = mejor
    return mejor
def main():
    monedas = [1, 2, 5, 10, 20]
    cambio = int(input("Ingresa el cambio a devolver: "))
    memo = {}
    resultado = cambio_minimo(cambio, monedas, memo)
    if resultado:
        print(f"\nCambio total: {cambio}")
        print(f"Monedas utilizadas: {resultado}")
        print(f"Cantidad de monedas: {len(resultado)}")
    else:
        print("No es posible dar ese cambio con las monedas disponibles.")
main()