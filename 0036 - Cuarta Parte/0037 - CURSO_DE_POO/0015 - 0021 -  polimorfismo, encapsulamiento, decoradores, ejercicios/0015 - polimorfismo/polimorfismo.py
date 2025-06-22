# pollimorfismo en python (polymorphism)
# poly= muchos       morfismo = formas

# El polimorfismo es un tema muy importante dentro de la programacion.
# El polimorfismo se aplica a la programacion orientada a objetos y 
# segun el tipo de lenguaje varia. 
# El polimorfismo es un concepto que hace referencia a poder enviar
# un mensaje sintactico a diferentes objetos.
# El mensaje es el mismo pero el resultado que tiene que generar es
# un resultado distinto
# ¿Por qué? por sus propiedades.

# Por ejemplo si a un objeto le digo "hace tu sonido"
# la clase vaca responde "Mu"
# la clase gato responde "Miau" y
# la clase perro responde "Guau".



# las variables en python son polimorfas, es decir pueden
# tomar distintos tipos de datos (polimorfismo en tiempos de ejecucion)
# o polimorfismos de inclusion
#  
# ...

# # polimorfismo con objetos mismo método y distintos objetos
print('polimorfismo con objetos mismo método y distintos objetos')

class GatoPOMM:
    def sonido(self):
        return 'Miau'
    
class PerroPOMM:
    def sonido(self):
        return 'Guau'
    

gato_p_o_m_m = GatoPOMM()
perro_p_o_m_m = PerroPOMM()

print('Implementando el mismo metodo sonido() para perro y gato')
print(perro_p_o_m_m.sonido())
print(gato_p_o_m_m.sonido())


# polimorfismo de funcion mismo metodos para distintos objetos
print('polimorfismo de funcion mismo metodos para distintos objetos')
class Gato:
    def sonido(self):
        return 'Miau'
    
class Perro:
    def sonido(self):
        return 'Guau'

def hacer_sonido(instancia):
    return instancia.sonido()

perro = Perro()
gato = Gato()

print(hacer_sonido(perro))
print(hacer_sonido(gato))

# en otros lenguajes de programacion como java
# el mismo método se puede sobrecargar
# ejemplo
# class Gato:
#     def sonido(self):
#         return 'Miau'
#     def sonido(self, otro):
#         return 'Miau'
#     def sonido(self, otro, otro2):
#         return 'Miau'
# 
# se puede crear un método con args
# y kwargs para que el mismo método reciba distintos tipos de datos
# y se pueda sobrecargar


# se puede hacer un polimorfismo de cohersion
num1 = 10
num2 = 20.3
print(type(num1))
print(type(num2))
resultado = num1 + num2
print(resultado)
print(type(resultado))
# el resultado es un float
# el polimorfismo de coercion es cuando un tipo de dato se convierte
# a otro tipo de dato

print('otro tipo de polimorfismo')
def recorrer(elemento):
    for i in elemento:
        print(f'el elemento actual es: {i}')


print('recorriendo una lista: [1,2,3,4,5]')
recorrer([1,2,3,4,5])
print('recorriendo una cadena: "hola"')
recorrer('hola')
print('recorriendo una tupla: (1,2,3,4,5)')
recorrer((1,2,3,4,5))
print('recorriendo un set: {1,2,3,4,5}')
recorrer({1,2,3,4,5})
print('recorriendo un diccionario: {"uno":1, "dos":2, "tres":3}')
recorrer({'uno':1, 'dos':2, 'tres':3})
print('recorriendo un range: range(10)')
recorrer(range(10))
print('recorriendo un range con paso: range(1,10)')
recorrer(range(1,10))
print('recorriendo un range con paso 2: range(1,10,2)')
recorrer(range(1,10,2))
print('recorriendo un range con paso -1: range(10,0,-1)')   
recorrer(range(10,0,-1))
print('recorriendo un range con paso -2: range(10,0,-2)')
recorrer(range(10,0,-2))

