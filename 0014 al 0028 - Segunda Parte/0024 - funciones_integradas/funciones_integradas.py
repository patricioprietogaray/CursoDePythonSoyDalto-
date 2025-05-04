#  funciones integradas

# Como ya se dijo cuando empezamos este curso se dijo hay que usar la funcion print(),
# len(), type(), input(), etc... 
# Estas son funciones es decir código que esta creado para que nuestro código se comporte
# de una manera en particular, no nos interesa como esta programado, son funciones que 
# vienen con python, lo que si nos interesa es la manera de utilizarla al 100% asi le 
# sacamos todo el 'jugo' posible.

# En python hay un concepto llamado ABSTRACCION, simplemente no nos importa que codigo
# esta compuesta, solo nos interesa saber como usar dicha funcion y aprovecharla al 
# 100% para hacer nuestro codigo.

# Una funcion está compuesta por cierto codigo que permite ejecutarlo en distintos
# lugares de nuestro programa sin tener que repetir cada vez todas 
# las lineas de ese código
# para llamar a esa funcion hacemos referencia a su nombre y listo.
# Características:
# 1) No repetimos código muchas veces.
# 2) Modularidad: Separar el programa en partes más pequeñas. Incluso permite
#    probar el codigo a parte para que no afecte el programa y luego incluirlo
#    en el proyecto principal.
# 3) Que el código sea más mantenible, solo modificamos la funcion y los cambios
#    estarán reflejados en todo el programa.
# 4) Creacion de código más legible.
# EL 90% DEL TIEMPO LEEMOS CÓDIGO, EL 10% LO ESCRIBIMOS

# Hay funciones creadas por python que se denominan build-in, son las que 
# incorpora python al ser instalado.

# 4.05
# https://youtu.be/nKPbfIU442g?t=14706

# FUNCIONES BUILD-IN
numeros=[25,2,48,32,10]

# funcion que devuelve el numero mayor
numero_mas_alto = max(numeros)
# print(numero_mas_alto)

# funcion que devuelve el numero mayor
numero_mas_bajo = min(numeros)
# print(numero_mas_bajo)

# funcion round
# dado un numero de tipo float 12.34567 utilizar round para redondearlo
redondeado = 12.34567
print(f'Redondeado de float {redondeado} ----> a int: {round(redondeado)}')
# para redondearlo a dos desimales multiplico por 100
print(f'Redondeo a dos decimales multiplicando y dividiendo: {round(redondeado*100)/100}')
# 12.34567 * 100 --> 1234.567 se redondea --> 1234 y ahora divido por 100 ---> 12.34
print(f'Redondeo con round a dos decimales: {round(redondeado,2)}')

print('Ejercicio optimizado con round')

#  Ejercicios prácticos

# El timing para ver estos conceptos en python en un curso de corrido es de 
# 2,5 hs de corrido como mínimo, 7 hs como máximo y 4 hs en promedio, este 
# curso lo logró en 1,5 hs.
# a) cuanta diferencia en porcentajes hay: 
#     - entre el mas rapidos de los cursos (2,5) y este curso (1.5)
#     - el mas lento de los otros cursos (7)
#     - el promedio de los cursos (4)
    
# b) teniendo en cuenta que el promedio de crudo es de 5 hs y con edicion lo convierten
#     en 4 horas y el crudo de este video fue de 3,5 hs y se redujo a 1,5 hs
#     - que porecentaje se reduce en
#         * el promedio de los cursos
#         * este curso

# c) Ver 10 hs de este curso sería equivalente a ver... cuantas horas de los otros cursos?
#     y ver 10 hs de otros cursos cuantas horas equivalen para este curso?


otros_cursos_min = 2.5
otros_cursos_max = 7.0
otros_cursos_prom = 4.0
este_curso = 1.5

print('Ejercicio 1 - Resoluciones')
# round(numero,2) --> redondea el valor a dos digitos no se usa porque si da un 
# numero redondo ej: 60  -> 60.0% y necesito 60.00%
# Con el uso de   :.2f   , te aseguras de que los números 
# se muestren siempre con dos decimales, incluso si son enteros.

# Datos proporcionados
otros_cursos_min = 2.5  # Curso más rápido
otros_cursos_max = 7.0  # Curso más lento
otros_cursos_prom = 4.0  # Curso promedio
este_curso = 1.5  # Este curso

# Cálculo de las diferencias en porcentajes con round() y redondeo a 2 decimales
diferencia_con_curso_min = round(((otros_cursos_min - este_curso) / otros_cursos_min) * 100, 2)
diferencia_con_curso_max = round(((otros_cursos_max - este_curso) / otros_cursos_max) * 100, 2)
diferencia_con_curso_prom = round(((otros_cursos_prom - este_curso) / otros_cursos_prom) * 100, 2)

# Mostrar resultados con dos decimales como texto - se agregan los ceros decimales a la derecha
print(f'a) Diferencia en porcentajes con este curso:')
print(f'    Este curso es el {diferencia_con_curso_min:.2f}% más rápido que el curso de menor duración de otros.')
print(f'    Este curso es el {diferencia_con_curso_prom:.2f}% más rápido que el curso promedio en duración de otros.')
print(f'    Este curso es el {diferencia_con_curso_max:.2f}% más rápido que el curso de mayor duración de otros.')


# funcion bool() -> True cuando hay algun tipo de informacion
# --> False cuando sea 0, [], (), False
print(bool(0))
print(bool(["sgfd"]))

# funcion all() -> True todo el iterable tiene que ser verdadero
print(all([1,"True"]))
print(all([1,True,"letra",[]]))

# sumar todo un iterable
sumandos = [1,2,3,4]
print(sum(sumandos))

