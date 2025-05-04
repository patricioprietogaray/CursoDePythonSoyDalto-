# Ejercicios de Funciones
# # Ejercicio 1
# # Escribir una función que muestre por pantalla el saludo 
# # ¡Hola amiga! cada vez que se la invoque.

# def saludo():
#     print("Hola amiga!")

# saludo()

# Ejercicio 2
# # Escribir una función a la que se le pase una cadena 
# # <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

# def saludo(nom):
#     print(f'Hola {nom}')

# saludo('Pepe')

# Ejercicio 3
# # Escribir una función que reciba un número entero positivo 
# # y devuelva su factorial.

# import math

# def factorial(num):
#     if num > 0:
#         print(f'Factorial de {num}: {num}! = ')
#         print(math.factorial(num))
#     else:
#         print('Debe ingresar un numero entero positivo mayor a cero!')

# factorial(4)

# Ejercicio 4
# # Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# # La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# # y devolver el total de la factura. 
# # Si se invoca la función sin pasarle el porcentaje de IVA, 
# # deberá aplicar un 21%.

# def impuesto(precio, iva=21):
#     print(f'El importe a pagar es de ${precio + ( precio * (iva/100))}')

# impuesto(100)
# impuesto(1000,9.5)

# Ejercicio 5
# # Escribir una función que calcule el área de un círculo 
# # y otra que calcule el volumen de un cilindro usando 
# # la primera función.

# # reemplazo funcion lambda
# area_circulo = lambda radio : radio ** 2 * 3.14
# volumen_cilindro = lambda altura, radio : area_circulo(radio) * altura

# # def area_circulo(radio):
# #     return 3.14 * radio ** 2

# # def volumen_cilindro(altura, radio):
# #     return area_circulo(radio) * altura

# print(f'Area de un circulo (radio = 3) es {area_circulo(3)}')
# print(f'Volumen de un cilindro (radio = 3 y altura = 5) es {volumen_cilindro(5,3)}')

# Ejercicio 6
# # Escribir una función que reciba una muestra de números en una lista 
# # y devuelva su media.

# lista=[3,5,2,2]

# def media(lista):
#     med = sum(lista)
#     elem = len(lista)
#     return med / elem

# print(f'La media de {lista} es: {media(lista)}')

# Ejercicio 7
# # Escribir una función que reciba una muestra de números en una lista 
# # y devuelva otra lista con sus cuadrados.
# lista=[3,5,2,2]
# lista_cuadrados=[]

# def cuadrados(lista):
#     for x in lista:
#         cuad = x ** 2
#         lista_cuadrados.append(cuad)

# cuadrados(lista)
# print(f'Dado una lista {lista} se elevan al cuadrado cada elemento: {lista_cuadrados}')



# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista 
# y devuelva un diccionario con su media, 
# varianza y 
# desviación típica.




# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números 
# y otra que calcule el mínimo común múltiplo.



# Ejercicio 10
# Escribir una función que convierta un número decimal en binario 
# y otra que convierta un número binario en decimal.


# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.