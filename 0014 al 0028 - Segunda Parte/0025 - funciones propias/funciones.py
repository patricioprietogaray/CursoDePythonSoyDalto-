# crear una funcion simple
# def saludar():
    # print('Hola Pepe Argento como estas?')

# saludar()
# saludar()
# saludar  no tira error pero no llama a saludar()

# # funciones que tengan parámetros
# # ¿Que es un parámetro?
# # Un parámetro es una variable que no existe fuera de la funcion 
# # que se crea y usa solo dentro de la funcion.
# # cuando sale de la función la variable se elimina.

# def saludar(nombre,sexo):
#     sexo = sexo.lower()
#     nombre = nombre.capitalize()
#     if sexo == 'mujer':
#         adjetivo = 'mi reina'
#     elif sexo == 'hombre':
#         adjetivo = 'maestro'
#     else:
#         adjetivo = 'crack'
    
#     print(f'Hola {nombre} {adjetivo} ¿Cómo estas?.')

# # saludar()
# saludar('Pepe','hombre')
# saludar('maria','mujer')
# saludar('Mistela', 'no binario')


# # crear una funcion que nos retorne valores
# def crear_contraseña_random(num):
#     # 10 caracteres (0 a 9)
#     chars = 'abcdefghij'
#     # numero como string
#     num_string = str(num)
#     # obtengo el primer numero Si num_string = '89'  -> num = 8 (entero)
#     num = int(num_string[0])
#     # juego con los indices en chars
#     c1 = num -1
#     c2 = num         # 0987654321 (menos)
#     c3 = num - 5     # abcdefghij
#     #                  0123456789
#     # genero la contraseña
#     contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
#     # print(contraseña)  DE ESTA FORMA LO PUBLICO Y NO QUIERO ESO
#     # return contraseña  # RETORNO EL VALOR QUE SE ALMACENARA EN UNA VARIABLE
#     return contraseña, num # retorno multiples valores

# numero = int(input('Ingrese un numero: '))
# # password = crear_contraseña_random(numero) #retorno un solo valor

# # desempaqueto: en la funcion utilizo varias variables
# password, numerito = crear_contraseña_random(numero)

# # mostrando los resultados obtenidos y los datos utilizados para obtenerlo
# print(f'La contraseña es {password} y para generarla usaste el numero {numerito}')



# suma de dos sumandos
# def sumar(a,b):
#     return a+b

# sumado = sumar(3,5)
# print(sumado)


# # sumar mas numeros forma no optima!
# def sumar(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados += numero
#     return numeros_sumados

# resultado = sumar([5,3,6,8,7,11])
# print(resultado)


