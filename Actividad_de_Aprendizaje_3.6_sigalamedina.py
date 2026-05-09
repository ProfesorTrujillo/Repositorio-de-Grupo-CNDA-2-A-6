class Cambio:
    def __init__(self, monto, monedas):
        self.monto = monto
        self.monedas = sorted(monedas)  # Ordenar monedas para eficiencia
        self.memo = {}  # Diccionario para memoización

    def calcular_cambio_minimo(self, restante):
        """
        Función recursiva con memoización para calcular el cambio mínimo.
        Devuelve una tupla: (número mínimo de monedas, lista de monedas usadas)
        """
        if restante == 0:
            return 0, []
        if restante < 0:
            return float('inf'), None
        if restante in self.memo:
            return self.memo[restante]

        min_monedas = float('inf')
        mejor_desglose = None

        for moneda in self.monedas:
            if moneda <= restante:
                num_monedas, desglose = self.calcular_cambio_minimo(restante - moneda)
                if num_monedas + 1 < min_monedas:
                    min_monedas = num_monedas + 1
                    mejor_desglose = [moneda] + desglose

        self.memo[restante] = (min_monedas, mejor_desglose)
        return min_monedas, mejor_desglose

    def obtener_desglose(self):
        """
        Método principal para obtener el desglose del cambio.
        """
        num_monedas, desglose = self.calcular_cambio_minimo(self.monto)
        if num_monedas == float('inf'):
            return None
        return desglose

def main():
    """
    Función principal que solicita datos al usuario e imprime el resultado.
    """
    try:
        # Solicitar monto al usuario
        monto = int(input("Ingrese el monto de dinero a devolver como cambio: "))
        if monto < 0:
            print("El monto debe ser un número positivo.")
            return

        # Solicitar monedas al usuario (opcional, con valores por defecto)
        monedas_input = input("Ingrese las denominaciones de monedas separadas por comas (ej: 1,2,5,10,20) o presione Enter para usar valores por defecto: ")
        if monedas_input.strip():
            monedas = [int(x.strip()) for x in monedas_input.split(',')]
        else:
            monedas = [1, 2, 5, 10, 20]

        # Crear instancia de Cambio
        cambio = Cambio(monto, monedas)

        # Calcular desglose
        desglose = cambio.obtener_desglose()

        if desglose is not None:
            # Contar monedas por denominación
            conteo = {}
            for moneda in desglose:
                conteo[moneda] = conteo.get(moneda, 0) + 1

            print(f"\nCambio a devolver para {monto} unidades usando {len(desglose)} monedas:")
            for moneda, cantidad in sorted(conteo.items()):
                print(f"- {cantidad} moneda(s) de {moneda}")
        else:
            print("No es posible devolver el cambio con las monedas disponibles.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")

if __name__ == "__main__":
    main()