def dar_cambio(monto, monedas):
    if monto == 0:
        return []
    for moneda in monedas:  # ya están ordenadas de mayor a menor
        if moneda <= monto:
            return [moneda] + dar_cambio(monto - moneda, monedas)

cambio = int(input("Monto del cambio: "))
monedas = [20, 10, 5, 2, 1]  # ordenadas manualmente

resultado = dar_cambio(cambio, monedas)

print("Cambio:", cambio)
print("Monedas:", resultado)
