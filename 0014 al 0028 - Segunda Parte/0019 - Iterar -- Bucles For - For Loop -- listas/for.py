# bucles for  - ITERAR

# Un bucle o una iteración es una repeticion de cierto código que realiza el programa
# python tiene elementos iterables y otros no son iterables una lista es iterable, una 
# cadena de caracteres es iterable, una tupla es iterable, una variable con un numero no es iterable.

# Bucle FOR
# Supongamos que tenemos una lista de animales
# animales = ["perro", "gato", "raton", "lechuza"]
#               [0]      [1]     [2]        [3]   ---> índices
# 
# for animal in animales:
#       print(animal)
# 
# que es animales? es la lista que consta de 4 animales distintos
# 
# que es animal? Es una variable que se va a crear solo para la iteración, terminada
# la iteración se borra. 
# La primera vez que se ejecute el código animal va a ser igual
# al primer elemento (indice=0 -> "perro") y luego preguntará hay más elementos?
# si la respuesta es true entonces muestra "gato", luego "raton" y asi hasta 
# llegar al último elemento "lechuza", cuando ya no hay mas elementos que iterar
# sale del ciclo for.

animales = ['pez', 'gato', 'perro']

print(f'Con print muestro de un saque a todos los elementos de animales: {animales}')

print('-------------------------------------------------')

print('Ahora voy a iterarlos con for:')
for animal in animales:
    print(f'El valor de animal es : {animal}')
    print(f'El valor de animales es: {animales}')
    

numeros = [1,2,3,4,5]
for multiplicado_por_dos in numeros:
    print(f'Multiplico por dos: 2 x {multiplicado_por_dos} =  {multiplicado_por_dos * 2}')

# ¿como iterar dos listas a la vez???
for numero, animal in zip(numeros, animales):
    print(f'Iteración con numero {numero}, animal {animal}')
# Resultado:
# Iteración con numero 1, animal pez
# Iteración con numero 2, animal gato
# Iteración con numero 3, animal perro

# que paso con el 4 y 5???   
# La razón por la cual no se muestran los números 4 y 5 en el resultado 
# es porque la función zip() detiene su iteración en el momento en que llega 
# al final de la lista más corta.

# generar un contador de 0 a 5
for num in range(0,5):
    print(f'Contando: {num}')

# Salida:
# Contando: 0
# Contando: 1
# Contando: 2
# Contando: 3
# Contando: 4
# incluye el 0 pero no el 5

# generar un contador con un parametro de range
# generar un contador de 0 a 5
for num in range(5):
    print(f'Contando: {num}')

# igual resultado que el anterior este parametro dira donde parar (no incluye dicho numero)


# recorrer una lista de una manera que no es óptima
for num in range(len(numeros)):
    print(numeros[num])     # -->  print(numeros[0]) ==> 1 (el valor del elemento con indice 0)
    print(f'num devuelve el indice: {num}, numeros: {numeros}')
    

# salida:
# 1 
# 2 
# 3 
# 4 
# 5


# FORMA CORRECTA DE RECORRER UNA LISTA POR EL INDICE
for num in enumerate(numeros):
    # num es una tupla con dos variables
    # el primero o num[0] es el indice
    # el segundo o num[1] es el valor
    print(type(num))
    print(num)
    print('-------------')

# resultado:
# <class 'tuple'>
# (0, 1)
# -------------
# <class 'tuple'>
# (1, 2)
# -------------
# <class 'tuple'>
# (2, 3)
# -------------
# <class 'tuple'>
# (3, 4)
# -------------
# <class 'tuple'>
# (4, 5)
# -------------


for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'En el índice {indice} se encuentra el valor {valor}')
    # print(num) # --> (0, 1)

for animal in enumerate(animales):
    indice = animal[0]
    valor = animal[1]
    print(f'En el índice {indice} se encuentra el valor {valor}')
    # print(animal) # --> (0, 'pez')

# En el índice 0 se encuentra el valor 1
# En el índice 1 se encuentra el valor 2
# En el índice 2 se encuentra el valor 3
# En el índice 3 se encuentra el valor 4
# En el índice 4 se encuentra el valor 5
# En el índice 0 se encuentra el valor pez
# En el índice 1 se encuentra el valor gato
# En el índice 2 se encuentra el valor perro

# la manera más práctica de desempaquetar una tupla con enumerate es 
# for a,b in enumerate(animales):
    # print(f'En el indice {a} está el valor {b}')

for a,b in enumerate(animales):
    print(f'En el indice {a} está el valor {b}')

# En el indice 0 está el valor pez
# En el indice 1 está el valor gato
# En el indice 2 está el valor perro


# mas elaborado
# animales = ["perro", "gato", "leon", "lechuza"]
# cuantos_animales = len(animales) -1
# print(cuantos_animales)
# print(animales.index("perro"))
# for animal in animales:
#     if animales.index(animal) < cuantos_animales:
#          print(f'el animal {animal} mira al ...')
#     else:
#         print(f'el animal {animal} se durmió.')




# Utilizando el else (en el for)
#  Al final de un bucle siempre se ejecuta el else haya elementos o no que iterar

print('----------------------------')
print('For Else')
paises=[]
for pais in paises:
    print(pais)
else:
    print('El bucle for se terminó si hay datos se muestran antes, si no esta linea siempre se ve')

# For Else
# El bucle for se terminó si hay datos se muestran antes, si no esta linea siempre se ve


print('----------------------------')
print('For Else')
paises=['Argentina', 'Brasil']
for pais in paises:
    print(pais)
else:
    print('El bucle for se terminó si hay datos se muestran antes, si no esta linea siempre se ve')

# For Else
# Argentina
# Brasil
# El bucle for se terminó si hay datos se muestran antes, si no esta linea siempre se ve

#  EL ELSE SIEMPRE A LA ALTURA DEL FOR

# https://youtu.be/nKPbfIU442g?t=13623