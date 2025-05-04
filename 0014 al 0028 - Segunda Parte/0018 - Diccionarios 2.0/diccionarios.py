# Diccionarios
# para crear tuplas vacias usamos la funcion tuple()
# para crear listas vacias usamos la funcion list()
# para crear diccionarios vacios usamos la funcion dict()

diccionario_con_dict = dict(nombre='Pepe', apellido= 'Argento')

# las tuplas pueden ser claves, pero las listas no
diccionario_con_tupla_como_clave = {("dalto", "rancio"):'jajaja'}

# conjuntos con frozenset SI
diccionario_conjunto_frozenset = {frozenset(["dalto", "rancio"]): 'jajajaja'}


# creando diccionarios sin valores solo definir las claves
diccionario_sin_valores = dict.fromkeys('nombre', 'apell')
# de esta manera itera el 'nombre' que esta primero y le asigna a cada clave
# iterada el valor apellido. ¿como itera nombre???
# {'n': 'apell', 'o': 'apell', 'm': 'apell', 'b': 'apell', 'r': 'apell', 'e': 'apell'}

# El comando que mencionas utiliza el método fromkeys() de los diccionarios en Python. 
# Vamos a desglosarlo un poco. La sintaxis es la siguiente: 
# diccionario_sin_valores = dict.fromkeys(iterable, valor) 
# - iterable: En tu caso, parece que has escrito 'nombre' y 'apell', pero esto 
# debería ser un iterable, como una lista o una cadena. Si usas una cadena, 
# cada carácter se convierte en una clave del diccionario.
# 
# - valor: Este es el valor que se asignará a cada clave en el diccionario. 
# Si no se especifica, el valor predeterminado será None. 
# Si tomamos tu ejemplo tal cual, dict.fromkeys('nombre', 'apell') crearía 
# un diccionario donde cada letra de la palabra "nombre" se convierte en una clave, 
# y todas esas claves tendrán el mismo valor, que en este caso es 'apell'.
#  
# El resultado sería algo así: 
# {'n': 'apell', 'o': 'apell', 'm': 'apell', 'b': 'apell', 'r': 'apell', 'e': 'apell'} 
# 
# Así que, en resumen, este comando crea un diccionario con las letras de "nombre" 
# como claves y 'apell' como el valor asociado a cada una de ellas. 
# 
# # para evitar lo anterior definimos nombre y apellido como claves, ¿como? 
#   encerrados en corchetes como si fuese una lista (list) donde las claves
#   serán los valores dados y el valor será nada (None).
diccionario_sin_valores = dict.fromkeys(['nombre', 'apellido'])
# aqui esta el resultado deseado!!!!
# {'nombre': None, 'apellido': None}

diccionario_con_valores_predeterminados = dict.fromkeys(['nombre', 'apellido'], 'Sin datos')

print(diccionario_con_dict)
print(diccionario_con_tupla_como_clave)
print(diccionario_conjunto_frozenset)
print(diccionario_sin_valores)
print(f'''
      Le paso una cadena de texto para que me muestre 
      los valores de la clave (nombre): {diccionario_sin_valores['nombre']} ''')

print(f'diccionario_con_valores_predeterminados: {diccionario_con_valores_predeterminados}')

# https://youtu.be/nKPbfIU442g?t=12596
