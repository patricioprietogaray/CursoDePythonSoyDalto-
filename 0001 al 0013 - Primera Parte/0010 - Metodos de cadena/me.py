# metodos de cadenas

# Los métodos son las funciones que se utilizan aplicadas a un objeto.
# Un objeto en Python es la mayoría de las cosas.
# Por ejemplo una variable, una lista o un texto es un objeto.
# Una funcion tiene esta arquitectura : funcion(parámetros).
# Un parámetro es el valor que le pasamos a la funcion para que se ejecute (la funcion).
# ..

cadena1 = 'Hola soy Patricio'

# para mostrar todos los metodos de cadena1 (string) utilizo DIR 
# dir(cadena1)
# dir es una funcion(parámetro) --> dir(cadena1)
# y para que se muestre por pantalla utilizo print
print(dir(cadena1))
# 
# Los metodos de una cadena o string
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
# 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
# 'title', 'translate', 'upper', 'zfill']

# pasar todo a mayusculas usando metodos() --> dato.metodo()
print(cadena1.upper())
# funcion len (longitud de la cadena)  --> funcion(parametro)
print(len(cadena1))

cadenaNormal = cadena1
mayusculas = cadenaNormal.upper()
minusculas = cadenaNormal.lower()
longitud = len(cadena1)

# capitalize() convierte todo en minusculas y solo la primer letra la convierte en 
# mayúsculas
texto1 = 'la cadena tiene'.capitalize()

retornar_un_valor = f'{texto1.capitalize()} {longitud} caracteres'


print(f'La cadena como se declaró: {cadenaNormal}')
print(f'La misma cadena en minúsculas: {minusculas}')
print(f'La misma cadena en mayúsculas: {mayusculas}')
print(f'{texto1} {longitud} caracteres.')

# Retornar un valor: Ya se dijo que es una funcion y que es un parámetro,
# la funcion recibe un parametro y esta funcion 'trabaja' con ese parametro,
# para que me retorne un valor. Pensemos en una funcion matemática para clarificar
# la idea. f(x)=x+1; entonces a x le asignamos un valor -> x=5, luego la funcion
# realiza el calculo 5+1 (x+1) y retorna un valor f(x)=6 (imagen).
# En sintesis las funciones aceptan valores (ingreso) y retornan valores (egreso).

print(f'Retorno el valor: --->   {retornar_un_valor}')


buscar_find = cadenaNormal.find('P')

print(f'''Encontrar la palabra Hola en el texto, en la siguiente posición: {buscar_find}
    (si es un numero >=0 lo encontró, si es -1 no lo encontró)''')

# la diferencia entre find e index que si hay un error nos lanza una excepcion 
# las excepciones se pueden manejar.
# Buscar una cadena dentro de otra cadena
# buscar_indice = cadenaNormal.index('A')
# print(f"buscar_indice = 'a' respuesta: {buscar_indice}" )
# Hola
# 0123
buscar_indice = cadenaNormal.index('o')
print(f"buscar_indice = 'o' respuesta: {buscar_indice}" ) # si encontro --> indice
                                                        # si no encontro --> -1

# 1:59
# tener en cuenta que si hay espacio no se cumplen las condiciones
cadenaNormal='Holache123'
print(f'Cadena: {cadenaNormal}')
es_numerico = cadenaNormal.isnumeric()
print('Es numerico?')
print(es_numerico)
# verifica si todos los caracteres de la cadena son números
# devuelve false porque hay letras

es_alfabetico = 'cadena Normal'.isalpha()
print('es alfabetico (solo letras) "cadena Normal"? (falso porque hay un espacio)')
print(es_alfabetico)
# comprueba si todos los caracteres son letras. También devolverá False
# porque hay un espacio. Caracteres validos a-z y A-Z.



es_alfanumerico = cadenaNormal.isalnum()
print('es alfanumerico (letras y numeros) (HolaChe123)')
print(es_alfanumerico)

# Busqueda con index
# buscar_index = cadenaNormal.index('P')
# print(buscar_index)  # ---> excepcion no se encontro en Holache123

# Busqueda una cadena con index
buscar_index = cadenaNormal.index('123')  #Holache123
print(buscar_index)  # ---> 7              01234567 

# un método es una 'funcion' especifica de un objeto
# un objeto tiene metodos que son las acciones que puede hacer dicho objeto


# count devuelve el numero de ocurrencias de una subcadena en una cadena dada
# en vez de encontrar una coincidencia nos dice cuantas coincidencias encontro 
# (incluido caracteres especiales)
# si no encuentra devuelve 0, si busca un numero en vez de letras hay excepcion
nombre = "Patricio Sebastian Prieto Garay!"
cadena_a_buscar = 'a'
contar_coincidencias = nombre.count(cadena_a_buscar)
print(f'Encontro {contar_coincidencias} coincidencias buscando "{cadena_a_buscar}" en {nombre}. ')


# len cuenta los caracteres de una cadena ES UNA FUNCION
cuantos_caracteres_hay = len(nombre)
print(f'En {nombre} hay {cuantos_caracteres_hay} caracteres (incluyendo los especiales).')


# startwith y endswidth son metodos que devuelve un booleano si el comienzo o 
# la finalizacion coincide con la cadena. 
nombre = "Patricio Sebastian Prieto Garay"
comienzo = 'Patro'
finaliza = 'ray'
comienza_con_Pat = nombre.startswith(comienzo)
finaliza_con_ray = nombre.endswith('ray')
print(f'comienza con {comienzo}: {comienza_con_Pat} ')
print(f'finaliza con {finaliza}: {finaliza_con_ray}')


# replace: reemplaza un valor por otro devuelve un string, se puede reemplazar
# una parte de la cadena por otra, si encuentra la cadena original, la reemplaza
# por la nueva, si no devuelve la cadena original
del comienzo
del finaliza
del comienza_con_Pat
del finaliza_con_ray
nombre_original = "Patricio Sebastian Prieto Garay"
nombre_reemplazado = nombre.replace(nombre_original, "Maria de las Mercedes Rimoli Echarren")
print(f'El nuevo nombre es: {nombre_reemplazado}.')
del nombre_reemplazado
nombre_hijo = nombre_original.replace("Patricio Sebastian", "Nehuen")
nombre_hijo = nombre_hijo.replace("Garay", 'Rimoli')
print(f'Transfomando el nombre del padre al hijo: {nombre_hijo}')


del nombre_original
del nombre
del nombre_hijo


# split: separa por el parametro dado devuelve una lista
nombre_original = "Patricio Sebastian Prieto Garay"
nombre_split = nombre_original.split(' ')
print(f'Lista separada por el espacio del nombre original: {nombre_split}')

# 2:07
