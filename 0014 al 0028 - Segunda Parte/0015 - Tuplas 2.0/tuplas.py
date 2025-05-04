#  tuplas
# tuple es una funcion que permite crear una tupla
# una tupla es una colección de elementos ordenados e inmutables. 
# Se definen utilizando paréntesis () y los elementos dentro de la tupla 
# se separan por comas.

tupla4 = ('a', 'b')

# inmutables porque una vez definida no se puede cambiar
# Las tuplas son útiles cuando quieres almacenar datos que 
# no deben cambiar a lo largo del tiempo.
# print(tupla4[0])
# tupla4[0]="z"     -> TypeError: 'tuple' object does not support item assignment


# como parámetro debo pasarle una lista

tupla = tuple(['datos1', 'datos2'])


# otra forma de crear una tupla es sin los paréntesis ni corchetes
# de multiples datos
tupla2 = "dato1", "dato2"

# otra forma de crear una tupla con un solo elemento es de la siguiente forma
# tupla = "dato",
# con la coma al final (si no tiene coma se trata de una variable)
tupla3 = "pepe",
# tupla3 = "pepe"   -> es una variable de nombre tupla3 definida con el valor "pepe"

print(tupla)
print(tupla2)
print(tupla3)
print(tupla4)

# las tuplas son inmutables y se guardan en un solo lugar en la memoria
# mientras que las listas se guardan en dos lugares de memoria uno tiene los datos
# originales y otros son los que se modifican, luego los datos modificados pasan a 
# los datos fijos.

# https://youtu.be/nKPbfIU442g?t=11637