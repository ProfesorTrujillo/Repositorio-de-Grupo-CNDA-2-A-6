#Asignamos la variable y definimos la funcion!
def cambio_minimo(monto, monedas, memo=None):
    if memo is None:
        memo = {}

    if monto == 0:
        return 0, []

    if monto in memo:
        return memo[monto]

    min_monedas = float('inf')
    mejor_combinacion = []

    for moneda in monedas:
        if moneda <= monto:
            cantidad, combinacion = cambio_minimo(monto - moneda, monedas, memo)

            if cantidad + 1 < min_monedas:
                min_monedas = cantidad + 1
                mejor_combinacion = combinacion + [moneda]

#Aqui vamos a guardar todo ese visne en memo, una ves ya hicimos las funciones 
    memo[monto] = (min_monedas, mejor_combinacion)
    return memo[monto]

#Aqui asignamos por partes tanto lo que se va a imprimir para que el usuario lo leea, como definir valores 
monto = int(input("Ingresa el monto a devolver: "))
monedas = [1, 2, 5, 10, 20]
monedas.sort(reverse=True)
cantidad, combinacion = cambio_minimo(monto, monedas)

#Ahora mostramos los resultados :D
print("Resultado:")
print("Cantidad mínima de monedas:", cantidad)

print("Desglose de monedas:")
desglose = {}
for moneda in combinacion:
    desglose[moneda] = desglose.get(moneda, 0) + 1

for moneda in sorted(desglose, reverse=True):
    print(f"{moneda}: {desglose[moneda]}")