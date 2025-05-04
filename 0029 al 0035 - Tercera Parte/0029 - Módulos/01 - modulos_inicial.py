# ¿Que es un módulo? Rta: Cualquier archivo.py
# ¿Por que le decimos módulos?
# Porque desde un módulo podemos llamar a otro, 
# desde un módulo podemos crear otro,
# podemos cambiar las rutas, 
# podemos acceder, 
# podemos formar paquetes.
# Si creo un módulo con muchas funciones, supongamos 
# que tengo que calcular la funcion fibonacci que ya creamos en un 
# ejercicio anterior.
# Ya está creada y no quiero andar copiando el código cada vez que lo necesito
# entonces, creo un módulo con la funcion fibonacci y todas las demas funciones
# que necesite.
# Entonces, desde un módulo nuevo llamo a ese módulo anterior.
# Y solo con llamarlo puedo usar todas las funciones que contenga ese módulo. 
# Es como separar el programa en varias partes y utilizarlo como querramos.

# Hay tres tipos de módulos:
#   * Python Modules: Son los módulos que vienen creados con python que los traen 
#                       incorporados. Estos módulos estan escritos en C.
#   * Third-Party Modules (módulos de terceros): Un programador crea su propio módulo
#                       con funciones específicas que a otros programadores 
#                       de la comunidad le pueden servir son compartidos en 
#                       internet y otros programadores lo pueden descargar y utilizarlo.
#   * Own Modules (módulos propios): Son los modulos creados por nosotros.

#  Para importar un módulo solo con el nombre y no con la extension
# import modulo_saludar
# import math

# para acceder a una funcion se hace como si fuera un método 
# "importado.método" este método es la funcion del modulo
# namespace es el modulo que importo

# print(modulo_saludar.saludar('Pepe Argento'))
# print(f'modulo_saludar: {type(modulo_saludar)}')  # modulo_saludar: <class 'module'>
# print(f'modulo_saludar.saludar(): {type(modulo_saludar.saludar('Pepe'))}')   # modulo_saludar.saludar(): <class 'str'>
# print(math.sqrt(9))

# cuando se ejecuta un programa que tiene un modulo importado hecho por terceros
# secrea una carpeta llamada __pycache__
# para acelerar los procesos y que el acceso a los modulos sea más rápido

# puede pasar que modulo_saludar este en otra intancia del programa
# por ejemplo un modulo que importamos tiene una funcion con el nombre A
# y en mi codigo local tambien tengo otra funcion con el nombre A.
# Entonces el programa no va a saber cuando invoco A, a que código corresponde
# si a la funcion local o al método del módulo importado.
# Tirará una excepcion / Error.

# Para evitar esto esta la funcion as
# "valor" as "clave"
# funciona al reves que clave: valor

# As permite poder cambiar la denominacion al archivo importado (namespace) 
# asi no tenemos problema

# import modulo_saludar as Saludo
# print(f'Saludo desde el modulo importado y asignado con AS: {Saludo.saludar('Linus')}')






# supongamos que el codigo de modulo_saludar.py tengo diez mil funciones,
# o sea que tendre un namespace con diez mil métodos y solo voy a USAR UN SOLO METODO
# no quiero importar todas las funciones (y tampoco copiar y pegar porque el codigo es
# gigante). La solucion "from import"

# from <modulo> import <método>

# importamos dos funciones y a una le cambio el nombre
# from modulo_saludar import saludar, saludo_raro as saludo_nashe
# saludo1 = saludar('Pepe')
# # saludo2 = saludo_raro('Argento')  # saludo_raro no esta definido porque le asigné saludo_nashe
# saludo2 = saludo_nashe('Argento')  # saludo_raro no esta definido porque le asigné saludo_nashe
# print(f'Saludo con from import: {saludar('FROM-IMPORT')}')
# print(f'saludo normal: {saludo1}')
# print(f'Saludo raro: {saludo2}')

# otra forma de importar seria:
# importar todo si vamos a usar todas los metodos, joya
# si no se sobrecarga todo y es innecesario.

# fijate que si habilito el ejercicio importar varias veces lo mismo trae errores
# el import solo una vez

# from modulo_saludar import *
# print(Saludar('Maria')) # impoto un Método
# print(Saludo_raro('Jose'))
# print(saludar)  # importo una variable


import modulo_saludar as m_saludar

print('Muestro todas las funciones y variables que tiene el modulo')
print('Desde el modulo que llama se ven como métodos')

# puedo ver metodos y propiedades del namespace
print(dir(m_saludar))
# salida:
# ['Saludar', 'Saludo_raro', '__builtins__',
# '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__spec__', 'saludar']

# ['Saludar', 'Saludo_raro',     -->  son funciones
# 'saludar']    --> es una variable

# https://youtu.be/nKPbfIU442g?t=20194


print(m_saludar.__name__)
# me muestra "modulo_saludar" o sea el nombre real del modulo
# porque m_saludar es el módulo 'modulo_saludar'





