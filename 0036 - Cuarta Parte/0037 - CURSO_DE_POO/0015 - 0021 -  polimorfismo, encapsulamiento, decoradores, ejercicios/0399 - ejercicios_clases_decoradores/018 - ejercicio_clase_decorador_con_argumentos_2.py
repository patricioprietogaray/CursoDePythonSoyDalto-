# CALCULADORA CON LOG

# decorador con argumentos

# Este decorador 'registrar_operacion' es una función que toma otra función
# (en este caso, un método de clase) y le añade funcionalidad de "logging".
def registrar_operacion(funcion_a_decorar):
    # 'funcion_envolvente' es la que realmente se ejecuta en lugar
    # de la función original. Necesita 'self' porque va a decorar 
    # un método de una clase. '*args' y '**kwargs' son para manejar 
    # cualquier argumento que la función original reciba. (siempre se debe utilizar
    # dichos argumentos que vienen por defecto)
    def funcion_envolvente(self, *args, **kwargs):
        # Obtiene el nombre del método (ej. 'sumar')
        nombre_funcion = funcion_a_decorar.__name__ 

        # Mensaje antes de ejecutar el método original
        print(f"[{nombre_funcion.upper()}] Iniciando operación con argumentos: {args}, {kwargs}")
        
        # Ejecuta el método original y guarda su resultado
        resultado = funcion_a_decorar(self, *args, **kwargs)
        
        # Mensaje después de ejecutar el método original, mostrando el resultado
        print(f"[{nombre_funcion.upper()}] Operación completada.\nResultado: {resultado}")
        
        # Devuelve el resultado que el método original hubiera devuelto
        return resultado 
    
    # El decorador devuelve la función "envuelta"
    return funcion_envolvente 

# clase

# --- 2. Definición de la Clase ---
# Aquí definimos nuestra clase 'Calculadora'.
class Calculadora:
    def __init__(self):
        # El constructor, se ejecuta al crear una nueva instancia de Calculadora.
        # En este ejemplo, no hace nada especial, solo 'pass'.
        pass

    # Aplicamos el decorador '@registrar_operacion' justo encima del método 'sumar'.
    # Esto significa que 'sumar' ahora tiene la funcionalidad extra de 'registrar_operacion'.
    @registrar_operacion
    def sumar(self, a, b):
        # Este es el código original del método sumar.
        return a + b
    
    # El método 'restar' NO tiene el decorador, por lo que se comporta de forma normal.
    def restar(self, a, b):
        return a - b

# ejecucion del programa desde aqui

# --- 3. Uso de la Clase y el Método Decorado ---

# Creamos una instancia (un objeto) de nuestra clase Calculadora.
mi_calculadora = Calculadora()

# Llamamos al método 'sumar'. Como está decorado, verás los mensajes de registro del decorador
# ANTES y DESPUÉS de que se realice la suma real.
print("\n--- Probando el método 'sumar' (¡Decorado!) ---")
resultado_suma = mi_calculadora.sumar(5, 3)
print(f"El resultado final de la suma es: {resultado_suma}")

# Llamamos al método 'restar'. Como NO está decorado, solo verás el resultado directo.
print("\n--- Probando el método 'restar' (¡No Decorado!) ---")
resultado_resta = mi_calculadora.restar(10, 4)
print(f"El resultado final de la resta es: {resultado_resta}")