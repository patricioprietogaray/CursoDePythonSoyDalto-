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


def decorador(funcion):
    def funcion_modificada():
        print('Antes de saludar desde el decorador')
        funcion()
        print('Después de saludar desde el decorador')
    return funcion_modificada


@decorador
def saludo():
    print('Hola decorador desde saludo')

saludo()