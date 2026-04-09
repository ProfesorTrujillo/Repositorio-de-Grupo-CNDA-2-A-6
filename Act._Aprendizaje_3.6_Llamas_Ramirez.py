# Act._Aprendizaje_3.6_LlamasRamirez.py

def cambio_recursivo(cambio, monedas):
    
    if cambio == 0:
        return []
    
    monedas = sorted(monedas, reverse=True)
    
    for moneda in monedas:
        if moneda <= cambio:
            resultado = cambio_recursivo(cambio - moneda, monedas)
            
            if resultado is not None:
                return [moneda] + resultado
    
    return None


cambio = 48
monedas = [1, 2, 5, 10, 20]
 
resultado = cambio_recursivo(cambio, monedas)


print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)