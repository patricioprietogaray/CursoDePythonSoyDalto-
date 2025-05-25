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
# 
# Crea una clase ServicioWeb.
# Dentro de ServicioWeb, crea un método de 
# instancia realizar_peticion(url) 
# que simule hacer una petición. 
# Aplica el decorador @limitar_llamadas(3) a este método.
# 
# Crea un @classmethod en ServicioWeb llamado 
# crear_servicio_tipo(tipo_servicio). 
# Este método actuará como una fábrica simple. 
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

