# El principio Abierto/Cerrado (Open/Closed Principle - OCP) 
# es un principio de diseño de software 
# que establece que las entidades de software 
# (clases, módulos, funciones, etc.) 
# deben estar abiertas para su extensión, pero cerradas para su modificación. 
# En otras palabras, se busca que el comportamiento de una entidad 
# pueda ser extendido sin necesidad de cambiar su código fuente.
#  
# ¿Qué significa "abierto para extensión"?
# Significa que se puede agregar nueva funcionalidad 
# a la entidad sin necesidad de modificar su código existente. 
# Esto se logra típicamente mediante el uso de abstracciones 
# como interfaces o clases base, 
# y la creación de nuevas clases que extiendan o implementen estas abstracciones.
#  
# ¿Qué significa "cerrado para modificación"?
# Significa que una vez que una entidad 
# ha sido implementada y probada, 
# no debe ser modificada para agregar nuevas funcionalidades. 
# Cualquier cambio en el código existente 
# podría afectar su funcionamiento correcto y potencialmente 
# introducir errores en otras partes del sistema que dependen de esa entidad.
#  
# Beneficios de aplicar el principio Abierto/Cerrado:
# Mayor mantenibilidad:
# El código existente no se modifica, 
# lo que reduce el riesgo de introducir errores 
# al agregar nuevas funcionalidades.
# Mayor flexibilidad:
# Permite adaptar el sistema a nuevos requerimientos 
# sin afectar el código base.
# Mejor diseño:
# Fomenta un diseño más modular y desacoplado.
# Pruebas más fáciles:
# Las pruebas unitarias existentes no necesitan 
# ser modificadas para agregar nuevas funcionalidades.
#  
# Ejemplo:
# Imaginemos una clase Calculadora que calcula 
# el área de diferentes formas geométricas. 
# Si utilizáramos el principio Abierto/Cerrado, 
# podríamos definir una interfaz Forma con un método calcularArea(). 
# La clase Calculadora recibiría objetos que implementen 
# esta interfaz. Para agregar una nueva forma, 
# como un triángulo, simplemente crearíamos 
# una nueva clase Triangulo que implemente 
# la interfaz Forma y sobrescriba el método calcularArea(). 
# La clase Calculadora no necesitaría ser modificada. 
# 
# En resumen, 
# el principio Abierto/Cerrado es una herramienta 
# poderosa para construir sistemas de software robustos, 
# flexibles y mantenibles. 
# Al adherirse a este principio, 
# se promueve un diseño que facilita la adaptación a los cambios 
# sin comprometer la estabilidad del código existente. 




# clases que no modifico (cerrada para su modificacion)
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


# clases que estan abiertas para su extension
# usan mail y les puedo enviar un mail
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por E-Mail a {self.usuario.email}")

# ahora mando por sms
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

# ahora se implementa el whatsapp
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por Whatsapp a {self.usuario.whatsapp}")

# ..... y todas las implementaciones futuras 
# de sistemas que todavia no se han inventado

# de esta manera tenemos un codigo mas limpio y escalable