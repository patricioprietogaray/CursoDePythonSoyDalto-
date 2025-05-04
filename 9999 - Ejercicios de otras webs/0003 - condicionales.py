# Ejercicio 1
# Escribir un programa que pregunte 
# al usuario su edad y muestre por pantalla 
# si es mayor de edad o no.

# edad = int(input('¿Cual es tu edad?: '))

# if edad >= 18:
#     print(f'Tiene {edad} años y es mayor de edad.')
# else:
#     print(f'Tiene {edad} años y No es mayor de edad.')


# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña 
# en una variable, pregunte al usuario por la contraseña 
# e imprima por pantalla si la contraseña introducida por el usuario coincide 
# con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# contraseña = "ContraSeña"
# login = input('Ingrese la contraseña: ')

# if login.lower() == contraseña.lower():
#     print('Bienvenido usuario')
# else:
#     print('Usted no es un usuario registrado.')

# Ejercicio 3
# Escribir un programa que pida al usuario dos números y 
# muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

# dividendo = float(input('Ingrese el dividendo: '))
# divisor = float(input('Ingrese el divisor: '))

# if divisor == 0.0:
#     print('No se puede realizar una división cuyo divisor sea cero!')
# else:
#     print(f'La división entre {dividendo} / {divisor} es {dividendo/divisor}.')



# Ejercicio 4
# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es par o impar.

# numero = int(input('Ingrese un número: '))
# if numero % 2 == 0:
#     print('Es par!')
# else:
#     print('Es impar!')


# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años 
# y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad 
# y sus ingresos mensuales y muestre por pantalla si el 
# usuario tiene que tributar o no.


# edad = int(input('Ingrese su edad: '))
# ingresos_mensuales = float(input('¿Cuales son sus ingresos mensuales en euros?: '))

# if edad > 16 and ingresos_mensuales > 1000:
#     print('Usted debe tributar')
# else:
#     print('Usted no debe tributar!')

# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B 
# de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N 
# y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.

# nombre = input('Ingrese el nombre: ')
# sexo = input('Ingrese el sexo: ')
# sexo = sexo.lower()
# nombre = nombre.lower()

# if sexo[0] == 'f':
#     if nombre[0] < 'm':
#         print('Pertenece al grupo A')
#     else:
#         print('Pertenece al grupo B')

# if sexo[0] == 'm':
#     if nombre[0] >= 'm':
#         print('Pertenece al grupo A')
#     else:
#         print('Pertenece al grupo B')


# Ejercicio 7
# Los tramos impositivos para la declaración de la renta 
# en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual 
# y muestre por pantalla el tipo impositivo que le corresponde.

# print('Renta tipo impositivo')
# renta_anual = int(input('Ingrese su ingreso anual: '))
# if renta_anual > 60000:
#     print(f'Debe pagar de renta {renta_anual * 0.45} euros. (45%)')
# elif renta_anual > 35000:
#     print(f'Debe pagar de renta {renta_anual * 0.3} euros. (30%)')
# elif renta_anual > 20000:
#     print(f'Debe pagar de renta {renta_anual * 0.2} euros. (20%)')
# elif renta_anual > 10000:
#     print(f'Debe pagar de renta {renta_anual * 0.15} euros. (15%)')
# else:
#     print(f'Debe pagar de renta {renta_anual * 0.05} euros. (5%)')
    
    
# Ejercicio 8
# En una determinada empresa, 
# sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 
# y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
# pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes 
# a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ 
# multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e 
# indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.

# puntos = float(input('Ingrese los puntos obtenidos: '))
# dinero = 2400 * puntos
# if (puntos >= 0.6):
#     print("Usted tiene un nivel de puntuación MERITORIO")
# elif (puntos == 0.4):
#     print("Usted tiene un nivel de puntuación ACEPTABLE")
# elif puntos == 0.0:
#     print("Usted tiene un nivel de puntuación INACEPTABLE")
    
# else:
#     print("La puntuación deberá ser 0.0, 0.4, 0.6 o más")

# if (puntos >= 0.6 or puntos == 0.4 or puntos == 0.0):
#     print(f'Usted tiene un premio de ${dinero:.2f}')



# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos 
# para todas las edades y quiere calcular de forma automática 
# el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente 
# y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar 5€ 
# y si es mayor de 18 años, 10€.

# age = int(input('Ingrese la edad del cliente: '))
# if age <= 4:
#     print('Free Pass!')
# elif age > 4 and age < 19:
#     print('Deberá pagar 5€')
# else:
#     print('Deberá pagar 10€')


# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes 
# disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate 
# que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no 
# y todos los ingredientes que lleva.


