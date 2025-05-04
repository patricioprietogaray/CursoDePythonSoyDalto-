# la funcion lambda es como la funcion flecha en js
#    Función tradicional
# function (a, b){
#   return a + b + 100;
# }

#     Función flecha
# (a, b) => a + b + 100;


# Funcion lambda
# nombre = lambda x: x*2
# multiplicar por dos es donde se guardara el resultado???
# lambda es una funcion anonima porque no tiene nombre, 
# y multiplicar_por_dos es donde se guardará el return de dicha funcion
# string anonimo   -->    "pepe"  no sabemos donde se guarda
# def nombre_de_la_funcion(parametro)  la funcion tiene un nombre
# x es el parámetro y retorno x*2


# # funcion lambda
# multiplicar_por_dos = lambda x: x*2
# print(multiplicar_por_dos(5))

# # se utiliza lambda para hacer algo sencillo y rapido
# # no tenemos que retornar la funcion, se almacena en forma directa
# # solo una linea de codigo (varias -> funcion tradicional)

# # funcion normal
# def mul_por_dos(x):
#     return x*2

# multip = mul_por_dos(5)
# print(multip)


# si es par o no
# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# funcion que devuelve si es true o false
# # metodo con funciones tradicionales
# def es_par(num):
#     if num%2==0:  # si al dividir por 2 el resto es 0 es True (es par)
#         return True

# # usando filter con una funcion comun
# # filter va a recorrer todos los numeros y evaluara con la funcion es_par
# numeros_pares = filter(es_par, numeros)
# print(list(numeros_pares))  # -> convierto a lista los numeros_pares  
#                             # -> [2, 4, 6, 8, 10, 12, 14, 16]


# mismo tarea con funcion lambda
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# numeros_pares donde voy a guardar todos los resultados que sean True
# a la funcion lambda le paso x como parametro (viene de la lista numeros)
# evaluo que el numero sea par, si es así cargo el numero a numeros_pares
#       si no no se carga 
# numeros es la lista que se iterará
numeros_pares = filter(lambda x: x%2==0,numeros)

# tengo que transformar a una lista para poderlo ver si no tira error
# <filter object at 0x7645f1934220>
print(list(numeros_pares)) # -> [2, 4, 6, 8, 10, 12, 14, 16] transformo en lista

