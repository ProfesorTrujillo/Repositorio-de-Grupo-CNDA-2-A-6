##  Cuanto de vendio en total  ##
def total_venta(pedidos):
    total=0
    for monto in pedidos:
        total+= monto
    return total

def promedio_pedidos(pedidos):
    if len(pedidos) == 0:
        return 0
    
    suma = 0 
    for monto in pedidos:
        suma += monto
    return suma / len(pedidos)

def pedido_mayor(pedidos):
    if len(pedidos) == 0:
        return None
    
    mayor = pedidos[0]
    for monto in pedidos:
        if monto > mayor:
            mayor = monto
    return mayor

def pedido_menor(pedidos):
    if len(pedidos) == 0:
        return None
    
    menor= pedidos[0]
    i = 0
    while i < len(pedidos):
        if pedidos[i] < menor:
            menor = pedidos[i]
        i += 1
    return menor

def contar_mayores(pedidos, limite):
    contador = 0
    for monto in pedidos:
        if monto > limite:
            contador += 1
    return contador


# 🔥 NUEVA: calcular descuentos
def aplicar_descuentos(total, cantidad_pedidos, cliente_nuevo):
    descuento = 0

    # Descuento por comprar más de 3 pedidos
    if cantidad_pedidos > 3:
        descuento += 0.10  # 10%

    # Descuento por cliente nuevo
    if cliente_nuevo.lower() == "si":
        descuento += 0.05  # 5%

    total_final = total * (1 - descuento)
    return descuento * 100, total_final


# ---------- PROGRAMA PRINCIPAL ----------

pedidos = []

n = int(input("¿Cuántos pedidos desea registrar?: "))

for i in range(n):
    monto = float(input(f"Ingrese el monto del pedido {i+1}: "))
    pedidos.append(monto)

cliente_nuevo = input("¿El cliente es nuevo? (si/no): ")

print("\n----- RESULTADOS -----")

total = total_ventas(pedidos)
print("Total de ventas:", total)

print("Promedio de pedidos:", promedio_pedidos(pedidos))
print("Pedido mayor:", pedido_mayor(pedidos))
print("Pedido menor:", pedido_menor(pedidos))
print("Pedidos mayores a $200:", contar_mayores(pedidos, 200))

# Aplicar descuentos
porcentaje_desc, total_con_desc = aplicar_descuentos(
    total, len(pedidos), cliente_nuevo
)

print("\n----- DESCUENTOS -----")
print(f"Descuento aplicado: {porcentaje_desc}%")
print(f"Total a pagar con descuento: {total_con_desc:.2f}")