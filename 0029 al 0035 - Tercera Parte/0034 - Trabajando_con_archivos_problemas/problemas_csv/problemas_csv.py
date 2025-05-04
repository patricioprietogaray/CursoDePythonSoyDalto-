# https://youtu.be/nKPbfIU442g?t=24473
# Problema 1
# cambiar el tipo de dato de una columna

import pandas as pd
# para que funcione tengo que estar en el mismo directorio del proyecto
# ojo con el terminal
df = pd.read_csv('datos.csv')
# # muestro el contenido de df
# # print(df)
# # print(type(df))  # <class 'pandas.core.frame.DataFrame'> todo el df
# # print(type(df['edad'])) # <class 'pandas.core.series.Series'>  todo edad [columna]
# print(type(df['edad'][0])) # <class 'numpy.int64'>  es un entero [columna][fila] -> 48
# # print(df['edad'][0])  # 48 de --> Patricio Sebastian,Prieto Garay, 48

# # convertir todas las edades (toda la columna) de numero a string
# df['edad'] = df['edad'].astype(str)
# # print(df)
# # en la terminal no hay diferencia, pero en el archivo tampoco
# # pido entonces el tipo de dato
# print(type(df['edad'][1])) # <class 'str'>

# # reemplazo prieto por genio
# # df['apellido'].replace("Prieto", "Genio")  # asi no funciona
# # df['apellido'] = df['apellido'].replace("Prieto", "Genio")
# # df.replace({'apellido':'Prieto'}, {'apellido':'Genio'}, inplace=True)
# df['apellido'] = df['apellido'].str.replace("Prieto", "Genio")
# print(df['apellido'])
# print(df)

# en el archivo csv --> Moni,Argento,
# cuando muestro los datos --> 11                   Moni           Argento   nan
# nan (NaN para string, nan para numeros) aparece cuando no hay datos

# cuando faltan los datos, elimino la fila -> axis=0
# df = df.dropna() # o tambien df = df.dropna(axis=0)

# # cuando faltan datos, elimino la columna -> axis=1
# # pero solo elimina las columnas con NaN o sea string 
# # con nan o sea numerica no se elimina
# df = df.dropna(axis=1)
# print(df)
df = df.dropna()

# eliminar datos repetidos
print(df)
df =df.drop_duplicates()
print(df)





# guardar los cambios en el archivo
df.to_csv('datos_limpios.csv', index=False)

