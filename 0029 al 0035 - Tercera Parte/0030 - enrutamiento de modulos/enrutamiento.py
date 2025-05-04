# https://youtu.be/nKPbfIU442g?t=20297


# Enrutamiento de módulos


# # modulo_saludo.py se encuentra en el mismo directorio
# import modulo_saludo
# -------------------------------------------------

# # Ahora el módulo a importar se encuentra en un subdirectorio del proyecto
# # /mi_proyecto/modulos/funciones.py 

# from modulos.funciones import Saludar
# print(Saludar('Pepe'))
# ---------------------------------------------------------

#    carpeta.archivo.py (sin .py)
# from modulos.operaciones_algebraicas import sumar, restar, multiplicar, dividir, modulo
# from modulos.menu_principal import presentacion_menu

# con import
# import modulos.operaciones_algebraicas
# import modulos.menu_principal
# a cada acceso debo poner
# modulos.menu_principal.presentacion_menu()
# y asi con todos

# --------------------------------------------------------

# Ahora el módulo a importar se encuentra en un directorio al mismo nivel del proyecto
# / ---- modulos ---- modulo_saludar.py
#  |____ proyecto ---- enrutamiento.py  (este es el modulo donde llamo a Saludar)

# importar sys para agregar la ruta relativa
# import sys
# print(sys)  # -->  <module 'sys' (built-in)>
# si quiero ver todos los módulos que tiene sys
# print(sys.builtin_module_names)
# al importar un modulo entre dos modulos de igual nombre uno nativo (viene con python) 
# y otro propio la prioridad esta en el modulo nativo.

# quiero ver las rutas de todos los modulos, el primero es el modulo
# que uso en el programa (el mio)
# ['/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0030 - enrutamiento de modulos',

# ahora muestra los modulos de python
# '/usr/lib/python312.zip', '/usr/lib/python3.12', 
# '/usr/lib/python3.12/lib-dynload', '/usr/local/lib/python3.12/dist-packages', 
# '/usr/lib/python3/dist-packages']

# print(sys.path)  # --> muestra las rutas propias y de python

# agrego la ruta ABSOLUTA a la carpeta de los modulos importados
# sys.path.append("/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0029 - Módulos")
# # al final del path se agrega:  '/0029 al ---- - Tercera Parte/0029 - Módulos'

# print(sys.path)

# # importo el modulo Saludar (tira como error pero no lo es)
# import modulo_saludar

# print(modulo_saludar.Saludar('Pato'))

# ---------------------------------------------------------------
# Si el módulo en una subcarpeta del proyecto se debe pasar la direccion
# /home/pepe..../mis_modulos
# con append 
# luego importo el archivo.py (sin .py) en este caso funciones.py (no dar bola al error)
# y para acceder al método es 
# lo_importado.metodo(). En este caso funciones.Saludar('PEPE)
# y el resultado es 
# Hola PEPE espero que hayas tenido un maravilloso día!.

# ****
# puedo renombrar el nombre de la funcion con as
# import funciones as modulo_saludo
# y lo llamo como 
# print(modulo_saludo.Saludar('PEPE'))
# con el mismo resultado

import sys
# print(sys.path)
sys.path.append("/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0030 - enrutamiento de modulos/modulos")
# print(sys.path)
import funciones as modulo_saludo
# print(funciones.Saludar('PEPE'))
print(modulo_saludo.Saludar('PEPE'))

# -----------------------------------------------------------------------------------

# import os
# print(os.path.abspath("/0029 al ---- - Tercera Parte/0029 - Módulos"))




# # # para importar desde un archivo se usa from <archivo> import <metodo/funcion>
# from modulo_saludar import Saludar


# print(Saludar('Pepe'))