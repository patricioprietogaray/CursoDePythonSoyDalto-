# Ejercicios de Bucles
# Ejercicio 1
# Escribir un programa que pida al usuario una palabra 
# y la muestre por pantalla 10 veces.

# word = input('Ingrese una palabra: ')
# for n in range(10):
#     print(word)

# solucion del ejercicio
# idem


# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# age = int(input('Enter your age: '))
# for n in range(age):
#     print(n+1)

# solucion del ejercicio
# age = int(input("¿Cuántos años tienes? "))
# for i in range(age):
#     print("Has cumplido " + str(i+1) + " años")


# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 
# hasta ese número separados por comas.

# numero_positivo = int(input('Ingrese un numero entero positivo: '))
# respuesta = ""
# if numero_positivo > 0:
#     for i in range(numero_positivo):
#         if not (i % 2 == 0):
#             if (numero_positivo == i + 1):
#                 respuesta += str(i)
#             else:
#                 respuesta += str(i) + ', '
# else:
#     print('Debe ingresar un numero entero positivo')

# print(respuesta)

# solucion del ejercicio
# n = int(input("Introduce un número entero positivo: "))
# for i in range(1, n+1, 2):
#     print(i, end=", ")


# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# for a in range(10,1, -1):
#     print(a)    --> muestra 10 a 2 cada numero en una linea
# numero_positivo = int(input('Ingrese un numero entero positivo: '))
# respuesta = ""
# if numero_positivo > 0:
#     # numero positivo
#     # print("Es un numero positivo mayor a cero!")
#     for a in range(numero_positivo, -1, -1):
        
#         # respuesta += respuesta + str(a)   
#         # esta mal o es
#         # respuesta = respuesta + srt(a) --> 3, 3, 2, 3, 3, 2, 1, 3, 3, 2, 3, 3, 2, 1, 0
#         #  o es
#         # respuesta += str(a)
#         respuesta += str(a)
#         if a != 0:
#             respuesta += ', '
#         else:
#             respuesta += '.'
# else:
#     print("Debe ser un numero positivo mayor que cero!!!!")

# print(respuesta)

# soucion del ejercicio
# n = int(input("Introduce un número entero positivo: "))
# for i in range(n, -1, -1):
#     print(i, end=", ")




# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

# capital = float(input('Ingrese el dinero a invertir € '))
# interes_anual = float(input('Ingrese el interes anual %: '))
# años = int(input('Ingrese los años que durará la inversión: '))

# for i in range(1,años+1):
#     print(f'Intereses generados en el año {i} €{(capital * (interes_anual / 100) * i):06.2f}')

# solucion del ejercicio
# amount = float(input("¿Cantidad a invertir? "))
# interest = float(input("¿Interés porcentual anual? "))
# years = int(input("¿Años?"))
# for i in range(years):
#     amount *= 1 + interest / 100 
#     print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

# Ejercicio 6
# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla un triángulo rectángulo 
# como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

# numero = int(input('Indique la cantidad de lineas que tendrá el triangulo rectangulo que va a construir: '))
# imprimir = ""
# for nro in range(numero):
#     linea = nro + 1
#     imprimir = '*' * linea
#     print(imprimir)



# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# linea=""
# print("------------------ Tabla pitagórica -------------------")
# print("    | x01| x02| x03| x04| x05| x06| x07| x08| x09| x10|")

# for tabla in range(10):
#     linea = f"T {tabla + 1:02.0f}|"
#     # print({tabla + 1})
#     for nro in range(10):
#         if nro == 0:
#             linea = f"T {tabla + 1:02.0f}|" + str(f'{((tabla + 1) * (nro +1)):03} |')
#         else:
#             linea += str(f'{((tabla + 1) * (nro +1)):03} |')
#         # linea += '\n'
#     print(linea)


# Ejercicio 8
# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

# numero_entero=int(input("ingrese un numero entero: "))  # 5
# # numero_anterior = str(numero_entero) # 5
# for a in range(1, (numero_entero + 1),2): # 5,1,-2
#     if a == 1:
#         numero_anterior = str(a) + ' '
#     else:
#         numero_anterior += str(a) + ' ' 
#     print(numero_anterior[::-1]) # lee al reves la cadena 1 3 5 7 9 --> 9 7 5 3 1 
    


# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# contraseña = 'Pepe_Argento_1234'
# login = ""

# while contraseña != login:
#     login = input("Ingrese la contraseña correcta: ")
#     print('La contraseña ingresada es incorrecta')

# print("Bienvenido!!!")

# Ejercicio 10
# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es un número primo o no.

# es_primo = int(input('Ingrese un numero para saber si es primo: '))
# control_es_primo = es_primo - 1
# control_de_resultado = True

# while control_es_primo >= 2:
#     if es_primo % control_es_primo != 0:
#         # print(f"el resto entre {es_primo} y {control_es_primo} es distinto a cero")
#         #     print(f'El numero {es_primo} es primo')
#         control_es_primo -= 1
#         continue
#     else: 
#         # print(f"el resto entre {es_primo} y {control_es_primo} es cero")
#         print(f'El numero {es_primo} no es primo')
#         control_de_resultado=False
#         break
# if es_primo == 1:
#     print("El numero 1 no se considera como primo")
# elif es_primo == 2:
#     print("El numero 2 es primo")
# elif control_de_resultado == True:
#     print(f'El numero {es_primo} es primo')
    


# Ejercicio 11
# Escribir un programa que pida al usuario una palabra 
# y luego muestre por pantalla una a una las letras de la palabra 
# introducida empezando por la última.

# palabra = input("Ingrese una palabra: ")
# resultado = ""
# for i in range(len(palabra)):
#     resultado += palabra[len(palabra) - i - 1]
    
# print(resultado)

# sdolucion del ejercicio
# word = input("Introduce una palabra: ")
# for i in range(len(word)-1, -1, -1):
#     print(word[i])



# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

# frase = input("Ingrese una frase: ")
# letra = input("Ingrese la letra que quiere contar que se encuentre en la frase: ")
# contador = 0

# for i, a in enumerate(frase):
#     if a == letra:
#         contador += 1
    
# print(f'La cantidad de letras {letra} que se encontro en la frase fueron: {contador}')
### print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

# Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
# hasta que el usuario escriba “salir” que terminará.


while True:
    frase = input("Ingrese una frase: ")
    if frase == "salir":
        break
    print(frase)



