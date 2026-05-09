def dar_cambio(dinero_que_debo, mis_monedas):
    if dinero_que_debo == 0:
        return []

    for moneda in sorted(mis_monedas, reverse=True):
        if moneda <= dinero_que_debo:
            return [moneda] + dar_cambio(dinero_que_debo - moneda, mis_monedas)

cambio_usuario = int(input("Introduce el monto del cambio a devolver: "))

mis_denominaciones = [1, 2, 5, 10, 20]

resultado = dar_cambio(cambio_usuario, mis_denominaciones)

print(f"Para un cambio de {cambio_usuario}, entrega estas monedas:")
print(resultado)
