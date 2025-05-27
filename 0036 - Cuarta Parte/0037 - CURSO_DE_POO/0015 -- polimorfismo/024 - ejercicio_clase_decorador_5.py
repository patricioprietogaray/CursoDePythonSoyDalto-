# #Crea un decorador llamado @limitar_llamadas(max_llamadas) 
# # que tome un argumento max_llamadas. 
# # Este decorador debe permitir que el método 
# # decorado se llame como máximo max_llamadas veces. 
# # Si se intenta llamar más veces, 
# # debe lanzar una excepción o imprimir un mensaje de 
# # advertencia. El contador de llamadas debe ser 
# # específico para cada instancia del objeto 
# # si el método es de instancia, 
# # o para la clase si el método es de clase.

# def limitar_llamadas(max_llamadas):
#     def decorador(funcion):
#         def wrapper(self, *args, **kwargs):
#             if getattr(self, '_llamadas', 0) >= max_llamadas:
#                 return 'Máximo de llamadas permitido!.'
#             setattr(self, '_llamadas', )




# # 
# # Crea una clase ServicioWeb.
# # Dentro de ServicioWeb, crea un método de 
# # instancia realizar_peticion(url) 
# # que simule hacer una petición. 
# # Aplica el decorador @limitar_llamadas(3) a este método.
# # 
# class ServicioWeb:
#     def __init__(self, url, llamar=1, max_llamadas=2):
#         self.url = url
#         self.llamar = llamar
#         self.max_llamadas = max_llamadas
        
#     def realizar_peticion(self):
#         return f'realizando la peticion a {self.url}'
    
#     @classmethod
#     def crear_servicio_tipo(self, tipo_servicio):
#         if tipo_servicio == 'premium':
#             return 'El servicio es premium'
#         else:
#             return 'El servicio es básico'
        

# # Crea un @classmethod en ServicioWeb llamado 
# # crear_servicio_tipo(tipo_servicio). 
# # Este método actuará como una fábrica simple. 

# class ServicioWebPremium(ServicioWeb):
#     pass

# class ServicioWebBasico(ServicioWeb):
#     # servicio basico de dos llamados
#     def __init__(self, url, llamar=1, max_llamadas=2):
#         super().__init__(url, llamar, max_llamadas)
#         print(limitar_llamadas(servicioWEB.realizar_peticion(self.url, self.llamar, self.max_llamadas)))
    



# # Si tipo_servicio es "premium", devuelve una 
# # instancia de ServicioWebPremium 
# # (que hereda de ServicioWeb). 
# # Si es "basico", devuelve una instancia de 
# # ServicioWebBasico (que también hereda de ServicioWeb).
# # 
# # ServicioWebPremium podría tener el método 
# # realizar_peticion decorado con @limitar_llamadas(10).
# # ServicioWebBasico podría tener el método realizar_peticion 
# # decorado con @limitar_llamadas(2).
# # 
# # Prueba creando diferentes tipos de servicios y llamando 
# # a realizar_peticion varias veces para ver cómo funciona 
# # el límite. 
# # 
# # ¡Espero que estos ejercicios te sirvan para practicar! 
# # Recuerda que la clave es entender los conceptos 
# # y luego intentar aplicarlos. 
# # No dudes en preguntar si tienes alguna duda con 
# # alguno de ellos. ¡Mucha suerte!

# servicioWEB = ServicioWeb('www.abc.com')
# print(servicioWEB.realizar_peticion())
# basico = ServicioWebBasico('www.abc.com')
# print(basico.crear_servicio_tipo('basico'))
# print(basico.realizar_peticion())
# print(basico.realizar_peticion())
# print(basico.realizar_peticion())









# RESOLUCION

#Crea un decorador llamado @limitar_llamadas(max_llamadas)
# que tome un argumento max_llamadas.
# Este decorador debe permitir que el método
# decorado se llame como máximo max_llamadas veces.
# Si se intenta llamar más veces,
# debe lanzar una excepción o imprimir un mensaje de
# advertencia. El contador de llamadas debe ser
# específico para cada instancia del objeto
# si el método es de instancia,
# o para la clase si el método es de clase.

def limitar_llamadas(max_llamadas):
    def decorador(funcion):
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, '_llamadas'):
                setattr(self, '_llamadas', 0)
            if self._llamadas >= max_llamadas:
                return f'Máximo de {max_llamadas} llamadas permitido para {funcion.__name__}.'
            self._llamadas += 1
            return funcion(self, *args, **kwargs)
        return wrapper
    return decorador



#
# Crea una clase ServicioWeb.
# Dentro de ServicioWeb, crea un método de
# instancia realizar_peticion(url)
# que simule hacer una petición.
# Aplica el decorador @limitar_llamadas(3) a este método.
#
class ServicioWeb:
    def __init__(self, url):
        self.url = url

    @limitar_llamadas(3)
    def realizar_peticion(self):
        return f'Realizando la petición básica a {self.url}'

    @classmethod
    def crear_servicio_tipo(cls, tipo_servicio):
        if tipo_servicio == 'premium':
            return ServicioWebPremium('www.premium.com')
        elif tipo_servicio == 'basico':
            return ServicioWebBasico('www.basico.com')
        else:
            return ServicioWeb(f'www.{tipo_servicio}.com')


# Crea un @classmethod en ServicioWeb llamado
# crear_servicio_tipo(tipo_servicio).
# Este método actuará como una fábrica simple.

class ServicioWebPremium(ServicioWeb):
    @limitar_llamadas(10)
    def realizar_peticion(self):
        return f'Realizando petición premium a {self.url}'

class ServicioWebBasico(ServicioWeb):
    @limitar_llamadas(2)
    def realizar_peticion(self):
        return f'Realizando petición básica con límite de 2 llamadas a {self.url}'




# Si tipo_servicio es "premium", devuelve una
# instancia de ServicioWebPremium
# (que hereda de ServicioWeb).
# Si es "basico", devuelve una instancia de
# ServicioWebBasico (que también hereda de ServicioWeb).
#
# ServicioWebPremium podría tener el método
# realizar_peticion decorado con @limitar_llamadas(10).
# ServicioWebBasico podría tener el método realizar_peticion
# decorado con @limitar_llamadas(2).
#
# Prueba creando diferentes tipos de servicios y llamando
# a realizar_peticion varias veces para ver cómo funciona
# el límite.
#
# ¡Espero que estos ejercicios te sirvan para practicar!
# Recuerda que la clave es entender los conceptos
# y luego intentar aplicarlos.
# No dudes en preguntar si tienes alguna duda con
# alguno de ellos. ¡Mucha suerte!

print("--- ServicioWeb (límite de 3 llamadas) ---")
servicio_base = ServicioWeb('www.base.com')
print(servicio_base.realizar_peticion())
print(servicio_base.realizar_peticion())
print(servicio_base.realizar_peticion())
print(servicio_base.realizar_peticion())

print("\n--- ServicioWeb Premium (límite de 10 llamadas) ---")
servicio_premium = ServicioWeb.crear_servicio_tipo('premium')
for _ in range(12):
    print(servicio_premium.realizar_peticion())

print("\n--- ServicioWeb Básico (límite de 2 llamadas) ---")
servicio_basico = ServicioWeb.crear_servicio_tipo('basico')
print(servicio_basico.realizar_peticion())
print(servicio_basico.realizar_peticion())
print(servicio_basico.realizar_peticion())


# Líneas 1-17: Definición del decorador limitar_llamadas

# Línea 8: Se define la función limitar_llamadas que toma un 
# argumento max_llamadas. Esta función es un "decorador de fábrica".

# Línea 9: Dentro de limitar_llamadas, se define otra función llamada 
# decorador que toma una función (funcion - el método que se va a decorar) 
# como argumento. Esto es lo que convierte a limitar_llamadas 
# en un decorador de fábrica.

# Línea 10: Dentro de decorador, se define la función wrapper. 
# Esta función es la que realmente se ejecutará cuando se 
# llame al método decorado. 
# Recibe self (la instancia del objeto), *args (argumentos posicionales) 
# y **kwargs (argumentos de palabra clave) 
# para poder trabajar con cualquier método.

# Línea 11-12: Se verifica si el atributo _llamadas existe 
# en la instancia del objeto. Si no existe, se inicializa a 0. 
# Esto asegura que cada instancia tenga su propio contador de llamadas.

# Línea 13: Se comprueba si el número de llamadas 
# (self._llamadas) es mayor o igual al max_llamadas permitido.

# Línea 14: Si se alcanza o supera el límite, 
# se retorna un mensaje indicando el máximo de llamadas permitido 
# y el nombre de la función.

# Línea 15: Si no se ha alcanzado el límite, se incrementa el 
# contador de llamadas self._llamadas en 1.

# Línea 16: Finalmente, se llama a la función original 
# (funcion) con los argumentos recibidos y se retorna su resultado.

# Línea 17: La función decorador devuelve la función wrapper.

# Línea 18: La función limitar_llamadas devuelve la función decorador.

# Líneas 22-36: Definición de la clase ServicioWeb

# Línea 26: Se define la clase ServicioWeb.

# Línea 27-28: El método __init__ se ejecuta al crear 
# una instancia de ServicioWeb. Inicializa el atributo url del objeto.

# Línea 31: Se aplica el decorador @limitar_llamadas(3) 
# al método realizar_peticion. 
# Esto significa que este método solo podrá 
# ser llamado 3 veces por cada instancia de ServicioWeb.

# Línea 32: El método realizar_peticion simula realizar una petición 
# a la URL del servicio web.

# Línea 35: Se define el método de clase crear_servicio_tipo. 
# Los métodos de clase reciben cls como primer argumento, 
# que representa la clase en sí.

# Línea 36-41: Este método actúa como una fábrica. 
# Si tipo_servicio es 'premium', crea y devuelve una instancia 
# de la clase ServicioWebPremium. 
# Si es 'basico', crea y devuelve una instancia de ServicioWebBasico. 
# Para cualquier otro tipo_servicio, crea y devuelve una 
# instancia de la clase base ServicioWeb.

# Líneas 45-47: Definición de la clase ServicioWebPremium

# Línea 45: Se define la clase ServicioWebPremium que hereda de ServicioWeb.

# Línea 46: Se aplica el decorador @limitar_llamadas(10) 
# al método realizar_peticion. Esto indica que las instancias 
# de ServicioWebPremium podrán llamar a este método hasta 10 veces.

# Línea 47: El método realizar_peticion de ServicioWebPremium 
# simula una petición premium.

# Líneas 49-51: Definición de la clase ServicioWebBasico

# Línea 49: Se define la clase ServicioWebBasico que hereda de ServicioWeb.

# Línea 50: Se aplica el decorador @limitar_llamadas(2) 
# al método realizar_peticion. 
# Las instancias de ServicioWebBasico podrán llamar 
# a este método como máximo 2 veces.

# Línea 51: El método realizar_peticion de ServicioWebBasico 
# simula una petición básica con un límite.

# Líneas 69-74: Prueba de la clase ServicioWeb

# Línea 69: Se crea una instancia de la clase ServicioWeb 
# llamada servicio_base con la URL 'www.base.com'.

# Líneas 70-73: Se llama al método realizar_peticion 
# de servicio_base cuatro veces. 
# Las primeras tres llamadas deberían devolver 
# el mensaje de realización de la petición, 
# mientras que la cuarta llamada debería devolver 
# el mensaje del límite alcanzado.

# Líneas 76-79: Prueba de la clase ServicioWebPremium

# Línea 76: Se utiliza el método de fábrica crear_servicio_tipo 
# de la clase ServicioWeb para crear una instancia 
# de ServicioWebPremium y se guarda en la variable servicio_premium.

# Líneas 77-78: Se realiza un bucle para llamar al método 
# realizar_peticion de servicio_premium 12 veces. 
# Las primeras 10 llamadas deberían simular la petición premium, 
# mientras que las dos últimas deberían mostrar el mensaje del límite alcanzado.

# Líneas 81-84: Prueba de la clase ServicioWebBasico

# Línea 81: Se utiliza el método de fábrica crear_servicio_tipo 
# para crear una instancia de ServicioWebBasico y se guarda en servicio_basico.

# Líneas 82-84: Se llama al método realizar_peticion de servicio_basico tres veces. 
# Las primeras dos llamadas deberían simular la petición básica con límite, 
# y la tercera debería mostrar el mensaje del límite alcanzado.

# En resumen, el código define un decorador que permite 
# limitar el número de veces que se puede llamar a un método en 
# una instancia de un objeto. 
# Luego, se definen tres clases (ServicioWeb, ServicioWebPremium, ServicioWebBasico) 
# con diferentes límites de llamadas para su método realizar_peticion, 
# y se utiliza un método de clase como fábrica para crear 
# instancias de estos servicios, demostrando cómo funciona 
# el límite de llamadas en cada caso.