# importar pandas y universalmente se le asigna pd
# de ahora en mas puedo llamarla como pd
# import pandas as pd

# pero hay que intalar PIP y Pandas
# apt install python3-pip python3-pandas

# ahora si funciona pandas... sigamos
# py -m pip 
# sudo apt install pythonpy se puede usar py en vez de python3
# pero use python3 -m pip y me mostro todo lo que se puede hacer

# python3 -m pip install pandas  # --> dice: que es mejor con apt install ....

# vamos a ver si funciona
# print(type(pd))  # --> si <class 'module'> entonces funciona

# como queda el codigo:

# ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0033 - archivos_planos_csv/datos.csv"
# # codificacion = "UTF-8"
# # escritura = "r"

# import pandas as pd
# archivo = pd.read_csv(ruta)
# print(archivo)      # muestra la lista
#                     #                   nombre            apellido  edad
#                     # 0     Patricio Sebastian        Prieto Garay    48
#                     # 1  Maria de las Mercedes   "Rimoli Echarren"    44


# # utilizando jupyter tenemos una forma optima de trabajar con la ciencia de datos
# # en Jupyter poner lo siguiente:
# import pandas as pd
# ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0033 - archivos_planos_csv/datos.csv"
# # codificacion = "UTF-8"
# archivo = pd.read_csv(ruta)
# archivo # --> muestra los datos con estilos (solo en jupyter)


# # volviendo al codigo
# ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0033 - archivos_planos_csv/datos.csv"
# # codificacion = "UTF-8"
# # escritura = "r"

# import pandas as pd
# # df -> dataframe
# df = pd.read_csv(ruta)
# print(df)      # muestra la lista


# # Según la IA explica un dataframe como:
# # Un DataFrame CSV es una tabla de datos que se guarda en un archivo 
# # de texto con formato CSV (valores separados por comas). 
# # Los DataFrames son estructuras de datos bidimensionales 
# # que se pueden usar para almacenar y analizar datos. 
# # Los archivos CSV son un formato común para compartir datos tabulares. 
# # Cómo se relacionan DataFrames y CSV?
# # Para leer datos de un archivo CSV en un DataFrame de Pandas, 
# # se usa la función read_csv(). 
# # Para exportar un DataFrame de Pandas a un archivo CSV, 
# # se usa el método to_csv().
# # Ventajas de usar DataFrames y CSV
# # Los DataFrames son una herramienta potente para analizar 
# # y manipular grandes cantidades de datos. 
# # Los archivos CSV son fáciles de mover entre programas 
# # y son leídos fácilmente por muchas aplicaciones. 
# # Características de los DataFrames
# # Los DataFrames pueden guardar datos de diferentes tipos, 
# # como caracteres, enteros, valores de punto flotante, y más.
# # Los DataFrames son similares a una hoja de cálculo o una tabla de SQL.
# # Los DataFrames facilitan el manejo de grandes cantidades de datos, 
# # la realización de cálculos y el filtrado de información. 


# # si deseo agregar un encabezado, o sea que la totalidad del archivo.cvs
# # son datos. Lo haria de la siguiente manera:
# df = pd.read_csv(ruta, names=["name", "lastname", "age"])
# print(df)

# # la salida vieja es: 
# #                   nombre          apellido  edad
# # 0     Patricio Sebastian      Prieto Garay    48
# # 1  Maria de las Mercedes   Rimoli Echarren    44
# # 2                   Pepe           Argento    58

# # la salida con names es:
# #                     name          lastname   age
# # 0                 nombre          apellido  edad
# # 1     Patricio Sebastian      Prieto Garay    48
# # 2  Maria de las Mercedes   Rimoli Echarren    44
# # 3                   Pepe           Argento    58
# # ahora nombre, apellido y edad son datos fila 0

# # OTRO CONCEPTO:
# # Slicing
# # Podemos extraer subconjuntos pertenecientes a un array usando:

# # x [start : stop : step]

# # Si no definimos alguno de ellos, los valores por defecto 
# # son: start = 0, stop = size of dimension, step = 1.
# # Otra lectura: https://keepcoding.io/blog/indexing-y-slicing-en-python/

# cadena = [0,1,2,3,4,5,6,7,8,9]
# print(f'Muestro la lista completa({type(cadena)}): {cadena}')
# print(f'Primer elemento de la lista: {cadena[0]}')
# print(f'Último elemento de la lista: {cadena[-1]}')
# print('Quiero mostrar utilizando Slicing:')
# print(f'Todos los elementos de cadena (cadena[:]): {cadena[:]}')
# print(f'Todos los elementos de cadena menos el ultimo (cadena[:-1]): {cadena[:-1]}')
# print(f'Desde el elemento 0 al elemento 2 (no se incluye el 2, igual que en el anterior con -1) de la cadena (cadena[0:2]): {cadena[0:2]}')

# Ordenar los datos
# volviendo al codigo
ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0033 - archivos_planos_csv/datos.csv"
# codificacion = "UTF-8"
# escritura = "r"

import pandas as pd
# df -> dataframe
df = pd.read_csv(ruta)
print(df)      # muestra la lista
print('Ordenamos por edad')
df_ordenado_edad = df.sort_values("edad", ascending=True)
print(df_ordenado_edad)
# fijarse que los indices estan desordenados cuando se ordena por una clave
print('Ordenamos por apellido')
df_ordenado_apellido = df.sort_values("apellido", ascending=False)
print(df_ordenado_apellido)
print('Ordenamos por nombre')
df_ordenado_nombre = df.sort_values("nombre")
print(df_ordenado_nombre)
print('concatenar dos listas (en este caso la misma lista)')
df2 = df
# para concatenar se usa el método pd (pandas)
# el parámetro pide una lista (elem1 df y elem2 df2)
df_concatenado = pd.concat([df, df2]) 
print(df_concatenado)

# accediendo a la primera fila con head()
df_primeras_dos_filas = df.head(2)
print('Las dos primeras filas')
print(df_primeras_dos_filas)

# accediendo a la primera fila con tail()
df_ultimas_dos_filas = df.tail(2)
print('Las dos últimas filas')
print(df_ultimas_dos_filas)

# https://youtu.be/nKPbfIU442g?t=23659


# quiero saber que cantidad de filas y columnas tiene datos.cvs
cantidad_filas_y_columnas = df.shape

# desempaquetando
cantidad_de_filas, cantidad_de_columnas = df.shape
# cantidad_de_filas = df.shape[0] # es igual a decir cantidad_filas_y_columnas[0]
# cantidad_de_columnas = df.shape[1]
print(f'El dataframe tiene las siguientes dimensiones: {cantidad_filas_y_columnas}')
print(f'El dataframe tiene {cantidad_de_filas} filas.')
print(f'El dataframe tiene {cantidad_de_columnas} columnas.')
print(f'''Descripción del dataframe (estadísticas):
      mean = promedio
      std = desviacion estandar
      25%..75% = son los cuartiles
      min y max = minima y maxima
      
      {df.describe()}''')

# accediendo a la edad de la fila 2 (patricio: 48)
edad_del_indice_dos = df.loc[2,"edad"]
print(f'Accediendo a la edad del indice 2 del cvs: {edad_del_indice_dos}')
nombre_del_inidce_dos = df.loc[2, "nombre"]
print(f'Accediendo al nombre del indice 2 del cvs: {nombre_del_inidce_dos}')
# acceder a todos los datos del indice 2 con loc
print(f'\nAccediendo al indice 2 y mostrar todos sus datos con loc:\n{df.loc[2,:]}\n')
print(f'\nAccediendo al indice 2 y mostrar todos sus datos con iloc:\n{df.iloc[2,:]}\n')
elem_especif_linea_col = df.iloc[2,2]
print(f'Accediendo al elemento especifico [2,2] 2° fila (Pepe) 2° col edad (58) -es como el índice: comienza desde cero-: {elem_especif_linea_col}')
todos_elem_una_columna = df.iloc[:,0]
# x:y,z --> filas: desde x hasta y. columnas: z donde se selecciona la columna a mostrar
print(f'Seleccionar todas las filas de una columna (todos los nombres): {todos_elem_una_columna}')
print(f'Mostrar todos los nombres:\n{df.iloc[:, 0]}')
print(f'Mostrar todos los apellidos:\n{df.iloc[:, 1]}')
print(f'Mostrar los nombres y los apellidos:\n{df.iloc[:,:2]}')

# z -->   0             1            2
#       nombre      apellido        edad    indice0
# x -->  pepe       argento         58      indice1


# https://youtu.be/nKPbfIU442g?t=23986

# accediendo a las filas donde la edad sea mayor a 30
# variable = df.iloc[:,:] --> todos
# variable = df.iloc[df["edad"]>30,:] --> pongo la condicion dentro de filas
# muestra las filas que cumplan con la condicion mas todas las columnas
mayor_que_30 = df.loc[df["edad"]>30,]
print(f'accediendo a las filas donde la edad sea mayor a 30 con loc: {mayor_que_30}')

menor_que_30 = df.loc[df["edad"]<=30,]
ordeno_por_edad = df.loc[df["edad"] <= 30].sort_values("edad", ascending=True)
print(f'accediendo a las filas donde la edad sea menor o igual que 30 con loc: {menor_que_30}')
print(f'Personas menores o iguales a 30, ordenadas por edad:\n{ordeno_por_edad}')