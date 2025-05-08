# encapsulamiento - encapsulation

# El encapsulamiento es otro item de la POO
# Es un concepto interesante. 
# NO EXISTE COMO TAL EN PYTHON.
# PERO AYUDA CON LA PROGRAMACION.
# Ayuda al desarrollador, a la legibilidad del código,
# a la documentación.
# Basicamente protege los elementos de una clase.
# En otros lenguajes esta private y public para 
# proteger métodos y atributos, pero en Python
# no existe.
# El encapsulamiento permite ocultar cierta 
# complejidad interna que hay dentro de la clase
# el encapsulamiento permite que la clase
# sea más fácil de usar.
# ....

# class MiClase:
#     def __init__(self):
#         self._atributo_privado = "valor del atributo privado"
#         self.__atributo_muy_privado = 'valor del atributo muy privado'

# miclase = MiClase()
# print(miclase._atributo_privado)
# print(miclase.__atributo_muy_privado) #error 
# # no se accede de esa manera!

# misma idea que la anterior
# usando getter y setters (conceptos)

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    # acceder con getters y setters (concepto)
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def set_nombre(self,nomb):
        self.__nombre = nomb
        return self.__nombre

# # no se puede acceder en forma directa
# pato = Persona('Patricio', 48)
# print(pato.__edad)

# acceder con getters y setters (concepto)
pato = Persona('Patricio', 48)
print(pato.get_nombre())
print(pato.get_edad())
print(pato.set_nombre('Sebastián'))

# print(pato.get_edad)
# esto no funciona asi pero se puede utilizar
# los decoradores