# Algoritmo recursivo para dar el cambio exacto con la menor cantidad de monedas.

# Solicitamos el monto
monto = int(input("Ingrese la cantidad a devolver en cambio: "))

def calcular_cambio_recursivo(cambio, monedas):
    # Si el cambio llega a 0, ya no necesitamos devolver más monedas
    if cambio == 0:
        return []
    
    # Variable para guardar la moneda que elegiremos
    moneda_a_usar = 0
    
    # Lógica básica para encontrar la moneda más grande que no supere el cambio
    # Recorremos la lista de monedas desde la más grande a la más chica
    indice = len(monedas) - 1
    
    while indice >= 0:
        if monedas[indice] <= cambio:
            moneda_a_usar = monedas[indice]
            # En cuanto encontramos la moneda adecuada, detenemos el ciclo
            break
        indice = indice - 1
        
    # Restamos el valor de la moneda elegida al cambio total
    monedas_restantes = calcular_cambio_recursivo(cambio - moneda_a_usar, monedas)
    
    # Retornamos la moneda actual junto con las que se calcularon
    return [moneda_a_usar] + monedas_restantes

# Definimos las denominaciones de las monedas disponibles
denominaciones = [1, 2, 5, 10]

# Llamamos a la función y mostramos el resultado
resultado = calcular_cambio_recursivo(monto, denominaciones)
print("Monedas utilizadas:", resultado)
print("Cambio total:", monto)
print("-" * 30)
