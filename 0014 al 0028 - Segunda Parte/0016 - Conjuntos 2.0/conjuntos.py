# Crear conjuntos con set()

# set() se puede como una lista [] o como un conjunto {}. No permite tuplas ()
# tampoco diccionarios {clave: valor}

# set() es inmutable. Una vez definido no se puede modificar.

conjunto = set({'dato1', 'dato2'})

# no puedo agregar una lista dentro de un conjuntos porque esta se modifica
# conjunto_para_modificar = set({'dato1', ['lista1', 'lista2']})  # --> TypeError: unhashable type: 'list'

# conjunto2 = set(conjunto, "Dato 3") TypeError: set expected at most 1 argument, got 2
# de esta manera no se puede.
print(conjunto)
# print(conjunto_para_modificar)

# Solucion:
# Hay una funcion llamada frozenset() conjunto congelado. Que ahora si es hasheable
conjunto1 = frozenset(['DatoUno', 'DatoDos'])
conjunto2 = set({conjunto1, "DatoTres"})

print(f'Conjunto 1: {conjunto1}')
print('-----------------------------------------')
print(f'Conjunto 2: {conjunto2}')
print('-----------------------------------------')
print(f'Navegando por el Conjunto 2: {conjunto2}')


# - conjunto = set({'dato1', 'dato2'}): Aquí se crea un conjunto llamado 
# conjunto que contiene dos elementos:       'dato1' y 'dato2'. 
# Los conjuntos en Python son colecciones desordenadas de elementos únicos.

# - conjunto2 = set(conjunto, "Dato 3"): Esta línea intenta crear un nuevo 
# conjunto llamado conjunto2. Sin embargo, hay un error aquí. La función 
# set() solo acepta un iterable como argumento, por lo que debería ser algo 
# como set([conjunto, "Dato 3"]) para funcionar correctamente. 
# En su forma actual, generará un error.
# - print(conjunto): Esta línea imprime el contenido del 
# conjunto 'conjunto', que debería mostrar {'dato1', 'dato2'}.


# 3. Más Comentarios:
# - Solucion:
# Este comentario sugiere que lo que sigue es una solución 
# o una forma corregida de trabajar con conjuntos.

# 4. Código de la Solución: 
# - conjunto1 = frozenset(['DatoUno', 'DatoDos']): Aquí se crea un 
# frozenset , que es una versión inmutable de un conjunto. 
# conjunto1 contiene los elementos 'DatoUno' y 'DatoDos'.
# - conjunto2 = set({conjunto1, "DatoTres"}): En esta línea, se crea 
# un nuevo conjunto conjunto2 que contiene el frozenset conjunto1 
# y el string "DatoTres". Esto es válido porque los frozensets son 
# inmutables y pueden ser elementos de un conjunto.
# 
# - print(f'Conjunto 1: {conjunto1}'): Esta línea imprime 
# el contenido de conjunto1, mostrando Conjunto 1: frozenset({'DatoUno', 'DatoDos'}).

# - print(f'Conjunto 2: {conjunto2}'): Finalmente, esta línea imprime el contenido de 
# conjunto2, que incluirá el frozenset y el string "DatoTres"..


### Resumen 
# El código intenta trabajar con conjuntos y frozensets, pero tiene un error 
# en la creación de conjunto2 en la primera parte. La segunda parte del código 
# es una forma correcta de utilizar conjuntos y frozensets. Si se corrige 
# el error en la primera parte, el código funcionará como se espera. 