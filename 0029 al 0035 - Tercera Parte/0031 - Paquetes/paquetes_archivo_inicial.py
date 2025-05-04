# https://youtu.be/nKPbfIU442g?t=20826

# Un paquete es una carpeta con muchos modulos
# dentro de la carptea paquete
# tengo dos modulos saludar y saludar_raro

# python diferencia una carpeta con modulos o una carpeta con paquete
# la carpeta con paquete tiene un archivo __init__.py (sin contenido), 
# listo es un paquete!!!!

# # importar el paquete (nombre de la carpeta)
# import paquete
# # print(type(paquete)) # --> <class 'module'> lo llama igual pero es un modulo 
# # porque lo diferencia el modulo __init__.py

# # si borro __init__.py y ejecuto
# # devuelve la ruta mas el mensaje que sigue
# # print(type(paquete.__path__))  # --> <class '_frozen_importlib_external._NamespacePath'>

# # si tengo el archivo __init__.py (debe estar vacío)
# # devuelve la ruta mas el mensaje que sigue
# print(type(paquete.__path__))  # --> <class 'list'>
# # ahora si es un paquete!!!

# como funciona???
import paquete.paquete_modulo_saludar

#     carpeta.    modulo.py         .metodo (argumento)
print(paquete.paquete_modulo_saludar.Saludar('Dalto'))

# NOTA: si un archivo se llama igual que la carpeta(donde estan los paquetes)
# python le da prioridad a las carpetas

# NOTA: si tenemos dentro de la carpeta paquete otras subcarpetas que sean paquetes
# en cada subcarpeta se debe agregar __init__.py


