# Ejercicio 1
# Escribir un programa que almacene las asignaturas 
# de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.

# materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# print(materias)

# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.

# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# for i, asignatura in enumerate(asignaturas):
#     print(f'Yo estudio {asignatura}')

# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# for subject in subjects:
#     print("Yo estudio " + subject)
    
# Ejercicio 3
# Escribir un programa que almacene las asignaturas 
# de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con 
# el mensaje En <asignatura> has sacado <nota> donde <asignatura> es 
# cada una des las asignaturas de la lista y <nota> cada una de las 
# correspondientes notas introducidas por el usuario.
    
# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas = []
# for n in asignaturas:
#     print(f'Ingrese la nota obtenida en {n}')
#     nota_final = int(input())
#     notas.append(nota_final)

# for asig, notaa in zip(asignaturas, notas):
#     print(f'Has obtenido {notaa} en {asig}.')
    
    
# Ejercicio 4
# Escribir un programa que pregunte al usuario los números 
# ganadores de la lotería primitiva, los almacene en una lista 
# y los muestre por pantalla ordenados de menor a mayor.

# loteria = []
# for i in range(6):
#     print(f'Ingrese un numero ganador del quini 6: ')
#     numero_ganador = int(input())
#     loteria.append(numero_ganador)

# print(f'Los numeros son: {sorted(loteria)}')

# # solucion:
# awarded = []
# for i in range(6):
#     awarded.append(int(input("Introduce un número ganador: ")))
# awarded.sort()
# print("Los números ganadores son " + str(awarded))

# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

# inverso = []
# for a in range(10):
#     inverso.append(a+1)
    
# print(inverso)
# print(inverso[::-1])


# # solucion:
# for i in range(1,11): # de 1 a 10 sera la variable i
#     print(inverso[-i], end=', ') #en una sola linea imprimer los numeros con ,

# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en 
# cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas 
# que el usuario tiene que repetir.

# #indice             0           1           2           3           4 
# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# calificaciones = [int(7), int(9), int(3), int(2), int(8)]

# print(f'Antes que nada pase las asignaturas son: {asignaturas}')

# # for n in asignaturas:
# #     print(f'Ingrese la nota obtenida en {n}')
# #     nota_final = int(input())
# #     calificaciones.append(int(nota_final))

# for materia, nota in zip(asignaturas, calificaciones):    
#     print(f'Las notas son: ({nota}) en {materia}.')

# # print(f'Final: Las materias que quedan para rendir: {asignaturas}')   

# # levanto los indices de calificaciones en reversa
# for indice in range(len(calificaciones)-1,0-1,-1):
#     # if nota >= 7:
#     # print(f"indice: {indice}")
#     # print(f'Asignatura: {asignaturas[indice]}') # devuelve el valor de la materia
#     # print(f'Calificación: {calificaciones[indice]}') # devuelve el valor de la calificacion
    
#     if calificaciones[indice] >= 7:    
#         calificaciones.pop(indice) #borro la calificacion quqe este aprobada
#         asignaturas.pop(indice)
        
#         # print(f'Final: Las materias que quedan para rendir: {asignaturas}')   

        
# print(f'Final: Las materias que quedan para rendir: {asignaturas}')   
        
    
    
    
#     #     print(f'materia desaprobada: {materia}, con una nota de {nota}')
#     # else:
#     #     print("Ya la aprobaste la eliminamos de las pendientes!")
#     #     # Al usar remove dentro de un bucle for, puedes alterar 
#     #     # el índice de las listas y causar que algunos elementos sean omitidos.
#     #     # calificaciones.remove(nota)
#     #     asignaturas.remove(materia)

# # solucion::::
# # OTRA FORMA MAS SIMPLE DE HACER LAS COSAS NO CARGA LA NOTA
# # subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# # passed = []
# # for subject in subjects:
# #     score = float(input("¿Qué nota has sacado en " + subject + "?"))
# #     if score >= 5:
# #         passed.append(subject)
# # for subject in passed:
# #     subjects.remove(subject)
# # print("Tienes que repetir " + str(subjects))



# # print(f'Las materias que quedan para rendir: {asignaturas}')
# # print(f'Las materias que quedan para rendir: {asignaturas}')

# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, 
# elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
# y muestre por pantalla la lista resultante.

# abecedario = ["a", "b", "c", "d", "e", "f", "g"]
# queda_abece = []
# for i, letra in enumerate(abecedario):
#     if not i % 3 == 0:
#         queda_abece.append(letra)
#     # print(i)
#     # print(letra)

# print(queda_abece)

# solucion:
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for i in range(len(alphabet), 1, -1):
#     if i % 3 == 0:
#         alphabet.pop(i-1)
# print(alphabet)

# Ejercicio 8
# Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla si es un palíndromo (famosas palabras capicua).
# palíndromo es una frase o palabra que se lee del derecho y del reves y es lo mismo
# anilina o neuquen

# palabra = "alas"
# palíndromo = ""
# for i in range(len(palabra)-1, -1, -1): #acordate que termina uno antes si termina en 0 es-1
#     palíndromo += palabra[i]
#     # print(i)

# if palabra == palíndromo:
#     print(f'La palabra {palabra} es un palíndromo')
# else:
#     print(f'La palabra {palabra} no es un palíndromo')

# solucion:
# word = input("Introduce una palabra: ")
# reversed_word = word
# word = list(word)
# reversed_word = list(reversed_word)
# reversed_word.reverse()
# if word == reversed_word:
#     print("Es un palíndromo")
# else:
#     print("No es un palíndromo")



# Ejercicio 9
# Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla el número de veces que contiene cada vocal.

# palabra=""
# # en la lista vocales en el indice 0 son cantidad de a, 1 e, 2 i, .....
# vocal_a=0
# vocal_e=0
# vocal_i=0
# vocal_o=0
# vocal_u=0

# palabra = input('Ingrese una palabra: ')
# for letra in palabra:
#     if letra == 'a':
#         vocal_a += 1
#     if letra == 'e':
#         vocal_e += 1
#     if letra == 'i':
#         vocal_i += 1
#     if letra == 'o':
#         vocal_o += 1
#     if letra == 'u':
#         vocal_u += 1



# print(f'En la palabra {palabra} la vocal a se repite {vocal_a} veces.')
# print(f'En la palabra {palabra} la vocal e se repite {vocal_e} veces.')
# print(f'En la palabra {palabra} la vocal i se repite {vocal_i} veces.')
# print(f'En la palabra {palabra} la vocal o se repite {vocal_o} veces.')
# print(f'En la palabra {palabra} la vocal u se repite {vocal_u} veces.')

# solucion
# word = input("Introduce una palabra: ")
# vocals = ['a', 'e', 'i', 'o', 'u']
# for vocal in vocals: 
#     times = 0
#     for letter in word: 
#         if letter == vocal:
#             times += 1
#     print("La vocal " + vocal + " aparece " + str(times) + " veces")

# con el primer for busco las vocales en la lista y pongo en 0 el contador
# en el segundo for cuento cuantas veces se repite la vocal 

# # Ejercicio 10
# # Escribir un programa que almacene en una lista los siguientes precios, 
# # 50, 75, 46, 22, 80, 65, 8, 
# # y muestre por pantalla el menor y el mayor de los precios.

# lista = [50, 75, 46, 22, 80, 65, 8]
# menor_precio = min(lista)
# mayor_precio = max(lista)
# print(menor_precio)
# print(mayor_precio)
# del menor_precio
# del mayor_precio

# # solucion larga
# menor_precio=100
# mayor_precio=0
# for precio in lista:
#     if menor_precio > precio:
#         menor_precio = precio
#     if mayor_precio < precio:
#         mayor_precio = precio

# print(f'El precio menor es {menor_precio}.')
# print(f'El precio mayor es {mayor_precio}.')
    
    
# # Ejercicio 11
# # Escribir un programa que 
# # almacene los vectores (1,2,3) y (-1,0,2) 
# # en dos listas y muestre por pantalla su producto escalar (producto punto).

# vector_A = [1,2,3]
# vector_B = [-1,0,2]
# # vector_A . vector_B (producto punto, punto por que es obligatorio ponerlo al punto)
# # se multiplica y se suma
# # (vector_A[0]*vector_B[0])+(vector_A[1]*vector_B[1])+ ......
# # si el resultado es cero los vectores son perpendiculares
# producto_escalar = 0
# for a in range(0,len(vector_A)):
#     # print(f'vector_A: {vector_A[a]} y b: {vector_B[a]}')
#     producto_escalar += (vector_A[a] * vector_B[a])

# print(f'El producto escalar o producto punto (multiplicacion de dos vectores) es: {producto_escalar}.')

# print("El producto de los vectores " + str(vector_A) + " y " + str(vector_B) + " es " + str(producto_escalar)) 



# Ejercicio 12
# Escribir un programa que almacene las matrices
 
#  A = 1  2  3            B = -1  0
#      4  5  6                 0  1
#                              1  1

# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante tuplas usar tuplas anidadas, 
# representando cada vector fila en una lista.



# matrices para su multiplicacion la cantidad de columnas de una matriz debe ser igual
# a la cantidad de filas de la otra matriz (se cumple)

# para obtener el producto de la matriz se multiplica la columna i (primera matriz)
# por la fila j (segunda matriz)

# la matriz a es de 2 filas x 3 columnas
# la matriz b es de 3 filas x 2 columnas
#  -->  2 x 3      3 x 2   como coincide el numero de columnas de a y el num de filas de b
# se puede hacer la multiplicacion
# el resultado es uma matriz de 2 x 2 (2 filas de A y 2 columnas de B)

# C = 11   12
#     21   22

# que es 11? debo multiplicar la primera fila de A * la primer columna de B
# C11 = fila A (1,2,3)* col B (-1,0,1)
# C11 = (1*-1)+(2*0)+(3*1)= -1 + 0 + 3 = 2
# con cada elemento del vector c

lista_A=((1,2,3),
         (4,5,6))
# lista_A[0] --> [1,2,3]    lista_A[1] --> [4,5,6]
# lista_A[0][0] --> 1
lista_B =((-1,0),
          (0,1),
          (1,1))

# lista_B[2][1] --> 1  (la ultima)
lista_C=[[0,0],
         [0,0]]

# print(lista_A[0][0])

# for fila_a in range(len(lista_A)):
#     # print(f'lista A: {a}')  # lista A: 0 -- lista A: 1 (indices)
#     for elem_fila_a in range(len(lista_A[fila_a])):
#         print(f'Indice fila {fila_a}: {elem_fila_a}') #indices
#         print(f'Contenido elemento es: {lista_A[fila_a][elem_fila_a]}')


# for fila_a in range(len(lista_A)):
#     # lista las filas de A (son dos)   0 y 1
#     print(f'Lista A fila iterada, primer elemento: {lista_A[fila_a][0]}.')
#     print(f'Lista B primera columna, fila de A iterada: {lista_B[0][fila_a]}')
#     # for col_b in (len(lista_B)/len(lista_A)):
#         # print(int(col_b))

# CODIFICANDO EL ALGORITMO

# cantidad_filas_en_A = 0
# cantidad_columnas_en_A = 0
# cantidad_filas_en_B = 0
# cantidad_columnas_en_B = 0
# cantidad_filas_en_C = 0
# cantidad_columnas_en_C = 0
# print('Dimensiones de Lista A')
# cantidad_filas_en_A = len(lista_A)
# if cantidad_filas_en_A >= 0:
#     cantidad_columnas_en_A = len(lista_A[0])
# print(f'Cantidad de filas en la lista A: {cantidad_filas_en_A}')
# print(f'Cantidad de columnas en la lista A: {cantidad_columnas_en_A}')

# print('Dimensiones de Lista B')
# cantidad_columnas_en_B = len(lista_B[0])
# if cantidad_columnas_en_B >= 0:
#     cantidad_filas_en_B = len(lista_B)
# print(f'Cantidad de filas en la lista B: {cantidad_filas_en_B}')
# print(f'Cantidad de columnas en la lista B: {cantidad_columnas_en_B}')

# if cantidad_columnas_en_A == cantidad_filas_en_B: 
#     print('Felicidades se puede hacer el ejercicio')

# print(f'La matriz resultante tiene una dimension de fila A {cantidad_filas_en_A} x columnas B {cantidad_columnas_en_B}')

# print('Dimensiones de Lista C')
# cantidad_columnas_en_C = len(lista_C[0])
# if cantidad_columnas_en_C >= 0:
#     cantidad_filas_en_C = len(lista_C)
# print(f'Cantidad de filas en la lista C: {cantidad_filas_en_C}')
# print(f'Cantidad de columnas en la lista C: {cantidad_columnas_en_C}')



# # almacenar los resultados
# dato_A=0
# for filaA in range(0, cantidad_filas_en_A):
#     for columnaA in range(0, cantidad_columnas_en_A):
        




# for filaC in range(0, cantidad_filas_en_C):
#     print(f'linea en c: {filaC}')
#     for columnaC in range(0, cantidad_columnas_en_C):
#         # print(f'columna en c: {lista_C[filaC][columnaC]}')
#         # lista_C[filaC][columnaC] = 10
        

# print(lista_C)



# for indice_col_A in range(cantidad_columnas_en_A):
#     print(f'Indice col A: {indice_col_A}')
#     for indice_filas_B in range(cantidad_filas_en_B):
#         print(f'Indice fila B: {indice_filas_B}')
        # hasta acá recorre las matrices matemáticas de manera correcta
        # for a, b in zip(lista_A[indice_fila_A], lista_B[indice_col_B]):
        # # lista_C[indice_fila_A][indice_col_B] = 
        #     print(f'dato a: {a}; dato b: {b}')


#  A = 1  2  3            B = -1  0
#      4  5  6                 0  1
#                              1  1

# que es 11? debo multiplicar la primera fila de A * la primer columna de B
# C11 = fila A (1,2,3)* col B (-1,0,1)
# C11 = (1*-1)+(2*0)+(3*1)= -1 + 0 + 3 = 2
# con cada elemento del vector c

# # Resultado:
# # iterar sobre las filas de A
# for i in range(len(lista_A)):
#     # iterar sobre las columnas de B
#     for j in range(len(lista_B[0])):
#         # iterar sobre las columnas de A o Filas de B
#         for k in range(len(lista_B)):
#             lista_C[i][j] += lista_A[i][k] * lista_B[k][j]

# # mostrar matriz resultante C - iteramos C
# print('El producto de los vectores entre A y B:')
# for filaC in lista_C:
#     print(filaC)
    

# Ejercicio 13
# Escribir un programa que pregunte por una muestra de números, 
# separados por comas, los guarde en una lista 
# y muestre por pantalla su media y desviación típica.

import math

ingreso_de_datos=""             # ingreso de datos desde la consola
lista_de_datos_string=[]        # lista de datos con formato string
lista_de_datos_integer=[]       # lista de datos con formato integer
datos_x=[]
datos_f=[]
datos_x_f=[]
promedio = 0.0
datos_F=[]                      # Lista de la Frecuencia absoluta acumulada
F = 0                           # acumulador de la frecuencia asoluta
Me = 0.0                        # mediana
frecuencia_corresponde_Me = 0.0 # ubicar la frecuencia que corresponde a la mediana
indice_mediana = 0
Mo = 0                          # La moda es la frecuencia que más se repite
indice_Mo = []

print("ESTADISTICAS")
# ingreso datos desde la consola
ingreso_de_datos = input('Ingrese una serie de numeros enteros separados por comas: ')
# ingreso_de_datos="1,1,2,3,5,4,4"
print(f'Los datos ingresados son: {ingreso_de_datos}.')

# Los datos marcados por comas los transformo en un listado y elimino las comas
lista_de_datos_string = ingreso_de_datos.split(",")

# el listado string lo transoformo a un listado integer
for i in lista_de_datos_string:
        lista_de_datos_integer.append(int(i))

# ordenar la lista de numeros
lista_de_datos_integer.sort()

# elimino el listado string
del lista_de_datos_string

# construir la tabla de estadisticas: datos únicos (x) y sus frecuencias (f)

# x es el dato almacenado en la lista
for x in lista_de_datos_integer:
    # pregunto si x no esta en datos_x
    if x not in datos_x:
        # agrego el dato a la lista datos_x
        datos_x.append(x)
        # agrego el dato (1) a la lista datos_f
        datos_f.append(1)
    else:
        # aca accedo al indice de manera individual
        indice_datos_x = datos_x.index(x)
        datos_f[indice_datos_x] += 1


# # recorro las listas x y f para agregar el producto de las mismas

print("-- Tabla de frecuencias --")
print("--------------------------")
print("  x  |  f  |  F  |  x.f  |")
print("--------------------------")
# recorro las listas y las presento en la tabla
for i in range(len(datos_x)):
    x = datos_x[i]
    f = datos_f[i]
    x_f = x * f
    F += datos_f[i] 
        
    print(f"  {x}  |  {f}  |  {F}  |  {x_f}  |")
    # agrego a la lista x_f el resultado de su producto
    datos_x_f.append(x_f)
    datos_F.append(F)


# calculo el total de f (frecuencia)
total_de_f=sum(datos_f)

# calculo el total de x.f
total_de_xf = sum(datos_x_f)

# calcular el media
media = total_de_xf / total_de_f

# calcular la media
Me = total_de_f / 2
# buscar la frecuencia que corresponde a la Me
for Mediana in datos_F:
    if Mediana >= Me:
        frecuencia_corresponde_Me = Mediana
        # print(f'For Media es: {datos_x.index(Media)}')
        indice_mediana = datos_x.index(Mediana)
        break
        


print(f"TOTAL|  {total_de_f}  |  F  |  {total_de_xf}  |")
print(f"La media (promidio) es {media}")
print(f'La Mediana es: {Me} y la frecuencia que corresponde es: {indice_mediana}')
# el dato que mas se repite es la moda
# buscar el dato de mayor frecuencia en la tabla datos_f
for moda in datos_f:
    if moda > Mo:
        Mo = moda

for ind in range(len(datos_f)):
    if datos_f[ind] == Mo:
        indice_Mo.append(datos_x[ind])

print(f'La moda es: {Mo} y se encuentra en x: {indice_Mo} ')

print(f'Calculo de la Desviacción típico o Desviación estandar')
#  CALCULO DE LA DESVIACION TIPICA
# 1. Calcular la varianza

# su equivalente
# varianza = sum([(x - media)**2 * f for x, f in zip(datos_x, datos_f)]) / total_de_f

# mismo codigo desglosado
# Paso 1: Calcular la diferencia al cuadrado (x - media)² para cada valor de x
diferencias_cuadradas = []
for x, f in zip(datos_x, datos_f):
    diferencia = x - media  # Diferencia entre el valor x y la media
    diferencia_cuadrada = diferencia ** 2  # Elevamos al cuadrado
    diferencias_cuadradas.append(diferencia_cuadrada)

# Paso 2: Multiplicar cada diferencia al cuadrado por la frecuencia f
productos = []
for diferencia_cuadrada, f in zip(diferencias_cuadradas, datos_f):
    producto = diferencia_cuadrada * f  # Multiplicamos por la frecuencia
    productos.append(producto)

# Paso 3: Sumar todos los productos
suma_productos = sum(productos)  # Suma de todos los productos

# Paso 4: Dividir entre el total de frecuencias (sum(datos_f)) para obtener la varianza
varianza = suma_productos / total_de_f

# Mostrar la varianza
print(f"Varianza: {varianza}")




print(f'La varianza es: {varianza}')

# 2. Calcular la desviación típica (raíz cuadrada de la varianza)
desviacion_tipica = math.sqrt(varianza)

print(f'La desviación estandar es: {desviacion_tipica}')








# print(f'Los numeros a continuacion: {numeros} se le calculara su media y su desviación típica')


# print(f'Su media es: {media}')
