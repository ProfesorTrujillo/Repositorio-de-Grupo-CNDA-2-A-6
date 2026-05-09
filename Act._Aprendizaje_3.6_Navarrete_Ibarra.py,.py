#programa de cambio de cajero dando la cantidad minima de monedas
monedas = [20, 10, 5, 2, 1]
def cambio(cantidad):
    resultado = []
    for moneda in monedas:
        while cantidad >= moneda:
            resultado.append(moneda)
            cantidad -= moneda
    return resultado
cantidad = int(input("¿Cantidad de compra? "))
dinero_ingresado = int(input("¿Cuánto dinero ingreso? "))
cambio_a_devolver = dinero_ingresado - cantidad
if cambio_a_devolver < 0:
    print("Falta dinero")
else:
    cambio_resultado = cambio(cambio_a_devolver)
    print("El cambio es:", cambio_a_devolver)
    print("Se puede dar las monedas:")
    print(*cambio_resultado, sep=",")