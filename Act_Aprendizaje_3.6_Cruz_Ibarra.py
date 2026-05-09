def cambio(c):
    monedas = [ 20, 10, 5, 2, 1,]
    
    if c == 0:
        return []
    
    for m in monedas:
        if m <= c:
            return [m] + cambio(c - m)


# Pedir solo el cambio
cambio_total = int(input("Ingresa el cambio: "))

# Resultado
resultado = cambio(cambio_total)

print("Cambio total:", cambio_total)
print("Monedas utilizadas:", resultado)
