# # Variables 2.0
# # Desempaquetado: en una sola accion se asignan varios valores a varias variables
# # por ejemplo de una lista, tupla o conjunto se asignan dichos valores a distintas
# # variables. Debe coincidir la cantidad de elementos con la cantidad de variables.

# tupla_de_nombres = ('Pepe', 'Argento', 48)
# lista_de_nombres = ['Moni', 'Argento', 60]
# conjunto_de_nombres = {'Paola', 'Argento', 17}

# pepe_nombre, pepe_apellido, pepe_edad = tupla_de_nombres
# print(pepe_nombre)
# print(pepe_apellido)
# print(pepe_edad)

# moni_nombre, moni_apellido, moni_edad = lista_de_nombres
# print(moni_nombre)
# print(moni_apellido)
# print(moni_edad)

# paola_nombre, paola_apellido, paola_edad = conjunto_de_nombres
# print(paola_nombre)
# print(paola_apellido)
# print(paola_edad)

# # print(conjunto_de_nombres[nombre])   -> no funciona para lista, tuplas y conjuntos
# print(f'lista de nombres: {lista_de_nombres[0]}.') # --> con indice funciona

# https://youtu.be/nKPbfIU442g?t=11353

# crear una tupla
# para desempaquetar los datos
# datos es una tupla () que contiene dos elementos
# cuando desempaqueto debo respetar los indices de los elementos
# para asignarlos correctamente a las variables que se declaran
# es necesario declarar n variables para n elementos

datos = ("Patricio", "Prieto Garay")
nombre, apellido = datos
print(f'nombre: {nombre}')
print(f'apellido: {apellido}')
print('asignando con _:')
# ahora si tengo tres elementos 
datos = ("Patricio", "Prieto Garay", 15)
del nombre
del apellido
# y quiero asignar solo dos elementos de los tres utilizo como tercer elemento el _
nombre, _ , _ = datos
print(f'nombre: {nombre}')
# print(f'apellido: {apellido}') --> name 'apellido' is not defined

# conjuntos desempaquetado
#  no sigue un orden y llena cualquier dato en cualquier clave.
datos_conjunto = {'Pato', 'Prieto', 123}
print(datos_conjunto)
sobrenombre, apellido, nro = datos_conjunto
print(f'sobrenombre: {sobrenombre}')
print(f'el apellido: {apellido}')
print(f'Un número: {nro}')

# https://youtu.be/nKPbfIU442g?t=11393
