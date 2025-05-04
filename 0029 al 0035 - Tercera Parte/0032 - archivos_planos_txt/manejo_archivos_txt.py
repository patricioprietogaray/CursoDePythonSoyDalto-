# https://youtu.be/nKPbfIU442g?t=21153

#  Manupular o manejar archivos.txt

# Un archivo es un contenedor de información.
# Un archivo tiene varios tipos de formatos (antiguamente extension)
# Ej: imagen png, audio mp3, video mp4, etc...


# para abrir un archivo usar open --->   ruta absoluta     encoding = UTF-8 por el formato (por las dudas)
archivo = open("/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt" ,encoding='UTF-8')
# hay que asignarle una variable

# print(archivo)  # ---> error

# <_io.TextIOWrapper 
# name='/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt' 
# mode='r' encoding='UTF-8'>

# # ¿que se hace? se lee
# print(archivo.read())

# # mostrar el contenido del archivo en lineas
# lineas = archivo.readlines() # --> LINEAS
# print(lineas)

# # para poder leer todas las lineas se debe abrir el archivo nuevamente
# archivo = open("/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt" ,encoding='UTF-8')
# lineas = archivo.readlines()
# print(lineas)

# linea = archivo.readline()  # --> LINEA
# print(linea)


linea_caracteres = archivo.readline(10)  # --> lee los primeros 10 caracterres de la 1° linea
print(linea_caracteres) # --> devuelve "Hola Patri"

# https://youtu.be/nKPbfIU442g?t=21646


# para cerrar un archivo se utiliza el metodo close
archivo.close()

# print(archivo.read())  # --> ValueError: I/O operation on closed file.
print(linea_caracteres)  # --> se muestra sin problemas porque la info esta en una variable




# archivo.write('\nHola macho, te edite desde python!!!')
# print(archivo.read())