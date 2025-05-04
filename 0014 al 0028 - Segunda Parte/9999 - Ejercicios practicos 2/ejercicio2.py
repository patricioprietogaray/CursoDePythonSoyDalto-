# ejercicio 2
# ingresar un numero y mostrar todos los primos anteriores a ese numero

# # Funcion para determinar si un número es primo
# def es_primo(num):
#     # Si el número es menor que 2, no es primo
#     if num < 2:
#         return False


# # Verificamos si el número es divisible por 
# # algún número entre 2 y la raiz cuadrada del número
#     # x**2     -> x al cuadrado
#     # x**0.5   -> raiz cuadrada de x
#     for i in range(2,int(num**0.5) + 1):
#         # si el numero es 
#         # divisible por i, no es primo
#         if num % i == 0:
#             return False
#     # Si no es divisible por ninguno de los 
#     # numeros anteriores, es primo
#     return True

# # función que retrocede desde el número dado 
# # y muestra los numeros primos anteriores
# def bucle_retroceso(nro_retrocede):
    
#     # Recorre los números desde nro_retrocede -1 
#     # hasta 2 en orden decreciente
#     for x in range(nro_retrocede - 1, 1, -1):
#         # si el numero es primo, lo mostramos
#         if es_primo(x):
#             print(x)

# # solicitamos al usuario que ingrese un numero
# numero = int(input('Ingrese un numero y se mostrarán todos los numeros primos anteriores: '))
# # llama a la funcion bucle_retroceso con el numero 
# # ingresado por el usuario
# bucle_retroceso(numero)


# # https://youtu.be/nKPbfIU442g?t=18274
# # https://youtu.be/nKPbfIU442g?t=18217


# # soucion Dalto
# # Funcion que verifica si un numero es primo
# def es_primo(num):
    
#     # itero desde 2 hasta num -1 (para no incluir el numero porque va a dar resto 0, el uno tampoco)
#     for i in range(2, num-1):
#         if num % i == 0:
#             return False  #No es primo
#     return True  # es primo


# # recorro desde el 3 hasta el numero que ingreso y pregunto de a uno si es primo (llamo a es_primo())
# def primos_hasta(num):
#     # guardo en la lista todos los nros primos encontrados
#     primos = []
#     for i in range(3, num+1): #num+1 para que incluya el numero que le pasamos en caso que sea primo
#         resultado = es_primo(i)
#         if resultado == True: primos.append(i)
#     return primos

# resultado = primos_hasta(13)
# print(resultado)

primos_hasta = lambda num: list( filter( lambda x: all( x % i != 0 for i in range ( 2, int( x ** 0.5 ) + 1 )), range(2, num)))
print(primos_hasta(15))

# 1. Definición de la función primos_hasta con lambda:

# primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, 
# int(x ** 0.5) + 1)), range(2, num)))

# lambda num:: Esto define una función anónima llamada primos_hasta 
# que toma un argumento num. 
# La función lambda se usa aquí para definir la función de manera 
# compacta sin necesidad de usar la palabra clave def.

# range(2, num): Aquí, range(2, num) genera una lista de 
# números que va desde 2 hasta num-1. 
# Es decir, esta es la lista de números candidatos para los que verificaremos 
# si son primos, desde el 2 hasta num-1.

# filter(...): La función filter toma dos argumentos:

# Una función (en este caso, la función lambda x: all(...)).

# Un iterable (en este caso, range(2, num)).

# La función filter devuelve un iterador que contiene solo 
# los elementos de la lista range(2, num) para los cuales la función 
# que le pasamos devuelve True. 
# Es decir, filtrará los números primos de la lista.

# 2. Función lambda interna:

# lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
# x: Este es el número que estamos evaluando para ver si es primo.

# all(...): La función all devuelve True si todas las condiciones 
# dentro de ella son True. En este caso, estamos comprobando 
# si el número x no es divisible por ningún número entre 2 
# y la raíz cuadrada de x 
# (esto es una optimización para no tener que comprobar hasta x-1).

# x % i != 0: Comprobamos si x no es divisible por i. 
# Si x % i != 0 para todos los valores de i en el rango 
# de 2 hasta int(x ** 0.5) + 1, entonces x es primo. 
# Si encontramos un divisor, x no es primo.

# range(2, int(x ** 0.5) + 1): La razón de verificar hasta la 
# raíz cuadrada de x es que si x tiene un divisor mayor que su raíz cuadrada, 
# entonces también debe tener un divisor menor que su raíz cuadrada. 
# Esto mejora la eficiencia del algoritmo.


# 3. Convertir el resultado a una lista:

# list(...)
# Finalmente, filter devuelve un iterador, 
# y con list(...) convertimos ese iterador a una lista de números primos.


# 4. Llamada a la función primos_hasta con el valor 15:

# print(primos_hasta(15))
# Esto llamará a la función primos_hasta(15) 
# y devolverá todos los números primos menores a 15. El resultado será:
# [2, 3, 5, 7, 11, 13]


# Resumen:
# Este código define una función primos_hasta que, 
# dada un número num, devuelve una lista de todos 
# los números primos menores que num. 
# Para verificar si un número es primo, 
# verifica si no es divisible por ningún número 
# desde 2 hasta la raíz cuadrada de ese número.