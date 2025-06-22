# El Principio de Responsabilidad Única (PRU), 
# también conocido como Single Responsibility Principle (SRP), 
# es un principio de diseño de software que establece que cada módulo, 
# clase o función debe tener una única razón para cambiar. 
# En otras palabras, cada elemento de software debe tener una sola 
# responsabilidad o tarea bien definida, 
# encapsulando esa funcionalidad dentro de sí mismo. 

# En resumen:
# Una clase, una responsabilidad: 
# Cada clase debe estar enfocada en una única tarea o función específica. 
# Evitar múltiples razones para cambiar: 
# Si una clase tiene múltiples responsabilidades, 
# es más probable que sufra cambios o modificaciones por diferentes motivos, 
# lo que puede llevar a problemas de mantenimiento y errores. 
# Facilita la comprensión, el mantenimiento y la reutilización: 
# Al tener clases con responsabilidades claras y definidas, 
# el código se vuelve más fácil de entender, mantener y reutilizar 
# en otros proyectos. 

# Ejemplo:
# Imagina una clase llamada Factura. 
# Si esta clase se encarga de generar la factura, 
# imprimirla y además calcular el total,
# estaría violando el principio de responsabilidad única. 
# Lo ideal sería dividir estas responsabilidades en clases separadas: 
# Factura para la generación, 
# una clase ImpresoraDeFacturas para la impresión, 
# y otra clase para el cálculo del total.
#  
# Beneficios de aplicar el PRU:
# Código más limpio y organizado:
# Clases con una sola responsabilidad son más fáciles de entender y mantener. 
# Mayor flexibilidad y mantenibilidad:
# Si una clase necesita cambiar, solo se realizarán cambios 
# en el código relacionado con su única responsabilidad. 
# Reutilización de código:
# Clases con responsabilidades bien definidas 
# pueden ser reutilizadas en diferentes proyectos. 
# Menos errores:
# Al reducir la complejidad y la interdependencia entre clases, 
# se reducen las posibilidades de introducir errores. 
# El PRU es uno de los cinco principios SOLID, 
# propuestos por Robert C. Martin, que buscan mejorar la calidad 
# y mantenibilidad del código orientado a objetos.
# 
# 


# esta mal porque en la vida real si se desea escalar el programa
# se hará engorroso la clase por ello es mejor dividir y que 
# cada clase se ocupe de algo unico.

# class Auto():
#     def __init__(self):
#         self.posicion = 0
#         self.combustible = 100
    
#     def mover(self, distancia):
#         if self.combustible >= distancia / 2:
#             self.posicion += distancia
#             self.combustible -= distancia / 2
#         else:
#             print('No hay suficiente combustible')

#     def agregar_combustible(self, cantidad):
#         self.combustible += cantidad

#     def obtener_combustible(self):
#         return self.combustible


class Auto():
    # tanque es un objeto que sale de la clase tanqueDeCombustible
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        # metodo obtener combustible que viene de la clase tanqueDeCombustible
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print('No hay suficiente combustible')

    def obtener_posicion(self):
        return self.posicion
    

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


# instanciamos el tanque (que ya tiene 100)
tanque = TanqueDeCombustible()

# instanciamos el auto que le pasamos tanque
autito = Auto(tanque)


# mostrar la posicion
print(autito.obtener_posicion())
print(tanque.obtener_combustible())
autito.mover(20)
print(autito.obtener_posicion())
print(tanque.obtener_combustible())
autito.mover(50)
print(autito.obtener_posicion())
print(tanque.obtener_combustible())
autito.mover(30)
print(autito.obtener_posicion())
print(tanque.obtener_combustible())
autito.mover(120)
print(autito.obtener_posicion())
print(tanque.obtener_combustible())

# 3.00.00

# explicacion: primero creamos un tanque de combustible, el tanque va a tener
# una propiedad estática (self.combustible) con el valor de 100
# cuando se crea el objeto el combustible sera 100
# Luego se crean los metodos agregar combustible (suma el combustible), 
# obtener combustible (devuelve el valor) y usar combustible (resta el combustible).
# Despues esta la clase Auto, que inicia con el objeto tanque y la 
# posicion = 0 (propiedad estatica), luego creamos un metodo de mover
# que le vamos a decir la distancia que se movera el auto que se pasa
# como parametro la distancia. Se hace la validacion por medio del 
# metodo obtener combustible de tanque (lo que le pase de distancia la mitad
# me lo saque de combustible) luego cargo el metodo usar combustible que le 
# paso la distancia recorrida y disminuira la mitad de combustible
# 
# y por ultimo obtener posicion que devolvera
# la posicion del vehiculo.
#                 .....

