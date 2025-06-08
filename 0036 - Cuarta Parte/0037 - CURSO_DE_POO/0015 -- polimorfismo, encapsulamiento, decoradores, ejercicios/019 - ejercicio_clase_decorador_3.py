import time

# Un decorador personalizado
def medir_tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"El método '{func.__name__}' tardó {fin - inicio:.4f} segundos en ejecutarse.")
        return resultado
    return wrapper

class Calculadora:
    historial_operaciones = [] # Atributo de clase

    def __init__(self, valor_inicial=0):
        self._valor = valor_inicial # "Protegido"

    @property # Permite tratar un método como un atributo (getter)
    def valor(self):
        print("Obteniendo valor...")
        return self._valor

    @valor.setter # Permite asignar a la "propiedad" valor (setter)
    def valor(self, nuevo_valor):
        print(f"Estableciendo valor a {nuevo_valor}...")
        if isinstance(nuevo_valor, (int, float)):
            self._valor = nuevo_valor
            Calculadora.agregar_al_historial(f"Valor establecido a {self._valor}")
        else:
            print("Error: El valor debe ser numérico.")

    @valor.deleter # Permite usar 'del' en la propiedad (deleter)
    def valor(self):
        print("Eliminando valor (reseteando a 0)...")
        self._valor = 0
        Calculadora.agregar_al_historial("Valor reseteado a 0")

    @medir_tiempo_ejecucion
    def sumar(self, cantidad):
        self.valor += cantidad # Usa el setter de valor implícitamente
        Calculadora.agregar_al_historial(f"Sumó {cantidad}, nuevo valor: {self._valor}")
        time.sleep(0.01) # Simular trabajo
        return self._valor

    @medir_tiempo_ejecucion
    def restar(self, cantidad):
        self.valor -= cantidad # Usa el setter de valor implícitamente
        Calculadora.agregar_al_historial(f"Restó {cantidad}, nuevo valor: {self._valor}")
        time.sleep(0.02) # Simular trabajo
        return self._valor

    @classmethod # Método que opera sobre la clase, no la instancia
    def agregar_al_historial(cls, operacion):
        cls.historial_operaciones.append(operacion)

    @classmethod
    def ver_historial(cls):
        print("\n--- Historial de Operaciones ---")
        for i, op in enumerate(cls.historial_operaciones):
            print(f"{i+1}. {op}")
        print("--------------------------------")

    @staticmethod # Método que no depende ni de la clase ni de la instancia
    def es_numero_valido(numero):
        return isinstance(numero, (int, float))

# Uso
calc = Calculadora(10)
print(f"Valor inicial: {calc.valor}") # Llama al getter @property

calc.valor = 20 # Llama al setter @valor.setter
print(f"Valor después de set: {calc.valor}")

calc.sumar(5)
calc.restar(3)

print(f"Valor final: {calc.valor}")

del calc.valor # Llama al deleter @valor.deleter
print(f"Valor después de del: {calc.valor}")

Calculadora.ver_historial()

print(f"¿Es 100 un número válido? {Calculadora.es_numero_valido(100)}")
print(f"¿Es 'abc' un número válido? {Calculadora.es_numero_valido('abc')}")

calc2 = Calculadora()
calc2.sumar(7)
Calculadora.ver_historial() # El historial es compartido