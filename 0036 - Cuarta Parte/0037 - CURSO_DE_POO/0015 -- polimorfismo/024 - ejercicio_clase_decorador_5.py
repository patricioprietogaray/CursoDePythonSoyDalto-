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

def limitar_llamadas(funcion):
    def wrapper(self, *args, **kwargs):
        if self.llamar > self.max_llamadas:
            return 'Maximo de llamadas permitido'
        self.llamar += 1
        return funcion(self, *args, **kwargs)
    return wrapper


# 
# Crea una clase ServicioWeb.
# Dentro de ServicioWeb, crea un método de 
# instancia realizar_peticion(url) 
# que simule hacer una petición. 
# Aplica el decorador @limitar_llamadas(3) a este método.
# 
class ServicioWeb:
    def __init__(self, url, llamar=1, max_llamadas=2):
        self.url = url
        self.llamar = llamar
        self.max_llamadas = max_llamadas
        
    def realizar_peticion(self):
        return f'realizando la peticion a {self.url}'
    
    @classmethod
    def crear_servicio_tipo(self, tipo_servicio):
        if tipo_servicio == 'premium':
            return 'El servicio es premium'
        else:
            return 'El servicio es básico'
        

# Crea un @classmethod en ServicioWeb llamado 
# crear_servicio_tipo(tipo_servicio). 
# Este método actuará como una fábrica simple. 

class ServicioWebPremium(ServicioWeb):
    pass

class ServicioWebBasico(ServicioWeb):
    # servicio basico de dos llamados
    def __init__(self, url, llamar=1, max_llamadas=2):
        super().__init__(url, llamar, max_llamadas)
        print(limitar_llamadas(max_llamadas))
    



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

servicioWEB = ServicioWeb('www.abc.com')
print(servicioWEB.realizar_peticion())
basico = ServicioWebBasico('www.abc.com')
print(basico.crear_servicio_tipo('basico'))
print(basico.realizar_peticion())
print(basico.realizar_peticion())
print(basico.realizar_peticion())
