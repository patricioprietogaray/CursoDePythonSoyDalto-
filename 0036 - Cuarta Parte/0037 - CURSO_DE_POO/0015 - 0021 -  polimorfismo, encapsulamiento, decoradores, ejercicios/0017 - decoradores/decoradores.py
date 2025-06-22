# decoradores o decorators

# En python un decorador es una funcion especial que decora a otra
# el decorador agrega algo a la funcion que ya existe y llama a esta funcion
# con el agregado

# los decoradores son utilizados para las excepciones para la validacion de entrada, etc

# ejemplo tengo una funcion x con su codigo interno y
# el decorador agregara a antes y d despues de ejecutar la funcion x
# NO SE MODIFICA LA FUNCION X NI Y

### def funcionX():
###   y....
###   Y....

### def funcion_decoradora(funcionX):
###   a...
###   funcionX()
###   b...

### decorada = funcion_decoradora(funcionX)
### decorada()

# ¿Qué hace?
# defino a funcionX
# defino a funcion_decoradora que le paso como argumento una funcion
# funcion_decoradora devuelve una funcion
# ejecuto decorada()

# otra forma de hacer lo mismo que está más aceptado


# def decorador(funcion):
#     def funcion_modificada():
#         print('Antes de saludar desde el decorador')
#         funcion()
#         print('Después de saludar desde el decorador')
#     return funcion_modificada


# @decorador
# def saludo():
#     print('Hola decorador desde saludo')

# saludo()


def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a funcion()')
        funcion()
        print('Despues de llamar a funcion()')
    return funcion_modificada

def saludo():
    print ('Hola mundo!')


# terminal

# solo llamo a la funcion
# saludo() 
# muestra por pantalla hola mundo!


# llamo al decorador
# decorador(saludo) 
# y no devuelve nada, o sea el terminal no se muestra nada

# print(decorador(saludo))
# salida: <function decorador.<locals>.funcion_modificada at 0x7f72141d4680>


# print(decorador(saludo()))
# Hola mundo!
# <function decorador.<locals>.funcion_modificada at 0x7f8401518680>


# asigno una variable y que funcionara como la funcion -> en js
saludo_modificado = decorador(saludo)
# ahora saludo_modificado es como una funcion y lo llamo
# saludo_modificado   #no devuelve nada

saludo_modificado()
# devuelve:
# Antes de llamar a funcion()
# Hola mundo!
# Despues de llamar a funcion()




# otra forma mas rápida

def decorador(funcion):
    def funcion_modificada():
        print('Decorador: Antes de llamar a funcion()')
        funcion()
        print('Decorador: Despues de llamar a funcion()')
    return funcion_modificada


@decorador
def saludo():
    print ('Hola mundo con decorador!')

saludo()

# con @decorador es igual a     ---->  saludo_modificado = decorador(saludo)
#                               ---->  saludo_modificado()


#  hasta aca con el video
# https://youtu.be/HtKqSJX7VoM?t=7668