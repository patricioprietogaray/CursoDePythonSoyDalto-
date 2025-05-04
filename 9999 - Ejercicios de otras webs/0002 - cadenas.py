# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario 
# en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces 
# como el número introducido.

# nombre = input('Escriba su nombre: ')
# repetir_nombre = int(input('Ingrese un numero entero que repita el nombre por pantalla: '))
# print((f'{nombre} \n') * repetir_nombre)
# del nombre, repetir_nombre

# Ejercicio 2
# Escribir un programa que pregunte el nombre 
# completo del usuario en la consola y 
# después muestre por pantalla el nombre completo del usuario 
# tres veces, una con todas las letras minúsculas, 
# otra con todas las letras mayúsculas y 
# otra solo con la primera letra del nombre y 
# de los apellidos en mayúscula. El usuario puede 
# introducir su nombre combinando mayúsculas y 
# minúsculas como quiera.

# nombre_completo = input("Ingrese su nombre completo: ")
# print(nombre_completo.lower())
# print(nombre_completo.upper())
# # print(nombre_completo.capitalize()) # solo la primera letra en mayusculas
# print(nombre_completo.title()) # todas las palabras con la primera letra en mayúsculas

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario 
# en la consola y después de que el usuario lo introduzca 
# muestre por pantalla <NOMBRE> tiene <n> letras, 
# donde <NOMBRE> es el nombre de usuario en mayúsculas 
# y <n> es el número de letras que tienen el nombre.

# nombre = input('Ingrese el nombre del usuario: ')
# print(f'El nombre {nombre.upper()} tiene {len(nombre)} letras')

# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente 
# formato prefijo-número-extension donde el prefijo 
# es el código del país +34, y la extensión tiene dos dígitos 
# (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número 
# de teléfono con este formato y muestre por pantalla 
# el número de teléfono sin el prefijo y la extensión.



# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola 
# y muestre por pantalla la frase invertida.

# frase = input("Ingrese una frase para invertirla: ")
# frase = 'Patricio Prieto'
# print(f'Ingreso una frase: {frase}') #toda la frase
# print(f'frase[0:6] --> {frase[0:6]}')#mustra las letras del indice 0 al 5
# print(f'frase[10:6] --> {frase[10:15]}')#mustra las letras del indice 10 al 15
# print(f'frase[::-1] --> {frase[::-1]}') #toda la frase invertida

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola 
# y una vocal, y después muestre por pantalla la misma frase 
# pero con la vocal introducida en mayúscula.

# frase = input('Una frase: ')
# vocal = input('una vocal: ')
# frase_modif = frase.replace(vocal,vocal.upper())
# print(frase_modif)


# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico 
# del usuario en la consola y muestre por pantalla otro 
# correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio ceu.es.

# email = "pato@gmail.com"
# print(f'En el correo {email} busco y reemplazo')
# print(f"buscar el @ con find('@'): {email.find("@")}")
# print('Devuelve 4')
# print(f'email[:email.find("@")]: {email[:email.find("@")]}')
# print('Es lo mismo que email[0:4] o sin el cero email[:4] que tiene el mismo resultado')
# print(' y le agrego el dominio ceu.es')
# print('''Queda la linea -->  print(email[:email.find('@')] + '@ceu.es')''')
# print(email[:email.find('@')] + '@ceu.es')


# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de 
# un producto en euros con dos decimales y 
# muestre por pantalla el número de euros y 
# el número de céntimos del precio introducido.

# trabajamos con las cadenas de caracteres
# precio = input('Precio: ')
# print(precio[:precio.find('.')], 'pesos y', precio[precio.find('.') +1:], 'centavos' )
#      desde 0 hasta el punto                desde el punto +1 espacio a la derecha hasta 
#                                               que se termine la cadena

# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha 
# de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
# el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione 
# cuando el día o el mes se introduzcan con un solo carácter.

# fecha = input('Ingrese su fecha de nacimiento (dd/mm/aaaa): ')
# primera_separacion = fecha.find('/')
# # segunda_separacion = fecha[:fecha.find('/')] #valor
# segunda_separacion = fecha.find('/',primera_separacion+1)
# dia = fecha[0:primera_separacion]
# mes = fecha[primera_separacion+1:segunda_separacion]
# año = fecha[segunda_separacion+1:len(fecha)]
# print(f'Usted ingresó el dia {dia}, del mes {mes} del año {año}.')


# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos 
# de una cesta de la compra, separados por comas, y muestre por 
# pantalla cada uno de los productos en una línea distinta.

# compras="manzanas, peras, sandias, bananas"
# print(compras.replace(', ','\n'))


# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, 
# su precio y un número de unidades y muestre por pantalla 
# una cadena con el nombre del producto 
# seguido de su precio unitario con 6 dígitos enteros 
# y 2 decimales, 
# el número de unidades con tres dígitos y 
# el coste total con 8 dígitos enteros y 2 decimales.

producto = input('¿Cual es el nombre del producto? ')
precio = float(input('¿Cual es su precio? '))
stock = int(input('¿Cuantas unidades hay en stock? '))
print(f'''El producto "{producto}", 
      tiene un valor unitario de ${precio:09.2f}, 
      su stock es de {stock:03} unidades y 
      su costo total es de ${stock * precio:011.2f}''')

# :010.2f:
# 0: Rellenar con ceros a la izquierda.
# 10: Longitud total del número (incluyendo el punto y los decimales).
# .2f: Mostrar dos decimales y formatear como un número de punto flotante.



# Las secuencias de escape en Python son combinaciones de caracteres que representan caracteres especiales dentro de cadenas de texto. Comienzan con una barra invertida \ seguida de otro carácter. Aquí tienes una lista de las secuencias de escape más comunes en Python:

# \n: Nueva línea. Inserta un salto de línea.
# \t: Tabulación horizontal. Inserta un espacio de tabulación.
# \\: Barra invertida. Inserta una barra invertida literal.
# \': Comilla simple. Inserta una comilla simple.
# \": Comilla doble. Inserta una comilla doble.
# \r: Retorno de carro. Mueve el cursor al inicio de la línea.
# \b: Retroceso. Elimina el carácter anterior.
# \f: Salto de página.
# \a: Campana ASCII (alerta). Produce un sonido de alerta (no siempre compatible).
# \v: Tabulación vertical.
# Secuencias de escape Unicode:

# Python también admite secuencias de escape para caracteres Unicode:

# \uXXXX: Carácter Unicode de 16 bits, donde XXXX es el código hexadecimal del carácter.
# \UXXXXXXXX: Carácter Unicode de 32 bits, donde XXXXXXXX es el código hexadecimal del carácter.
# Secuencias de escape octales y hexadecimales:

# \ooo: Carácter con valor octal ooo.
# \xhh: Carácter con valor hexadecimal hh.
# Ejemplos:

# Python

# print("Hola\nMundo")  # Imprime "Hola" en una línea y "Mundo" en la siguiente
# print("Texto con\ttabulación")  # Imprime texto con un espacio de tabulación
# print("Barra invertida: \\")  # Imprime una barra invertida literal
# print("Comillas: \' y \"")  # Imprime comillas simples y dobles
# print("alerta \a") # emite un sonido de alerta, si el sistema lo soporta.




# Hay varias maneras de escribir una cadena al revés en Python. Aquí te presento algunas de las más comunes:

# 1. Usando slicing (rebanado) con paso negativo:

# Esta es la forma más concisa y eficiente de invertir una cadena en Python.

# Python

# cadena = "Hola Mundo"
# cadena_invertida = cadena[::-1]
# print(cadena_invertida)  # Output: odnuM aloH
# cadena[::-1] crea una nueva cadena que es una copia de la cadena original, pero con los caracteres en orden inverso.
# 2. Usando un bucle for:

# Puedes iterar a través de la cadena original en orden inverso y construir una nueva cadena.

# Python

# cadena = "Python"
# cadena_invertida = ""
# for i in range(len(cadena) - 1, -1, -1):
#     cadena_invertida += cadena[i]
# print(cadena_invertida)  # Output: nohtyP
# range(len(cadena) - 1, -1, -1) genera una secuencia de índices que comienza en el último carácter de la cadena, termina en el primer carácter y se mueve hacia atrás de uno en uno.
# 3. Usando la función reversed() y ''.join():

# Esta forma implica usar la función reversed() para obtener un iterador que recorre la cadena en orden inverso, y luego usar ''.join() para unir los caracteres en una nueva cadena.

# Python

# cadena = "Ejemplo"
# cadena_invertida = ''.join(reversed(cadena))
# print(cadena_invertida)  # Output: olpmejE
# reversed(cadena) devuelve un iterador que produce los caracteres de la cadena en orden inverso.
# ''.join(...) concatena los caracteres del iterador en una nueva cadena.
# ¿Cuál método usar?

# El slicing con paso negativo ([::-1]) es generalmente la opción preferida debido a su simplicidad y eficiencia.
# Las otras opciones son más largas y pueden ser menos eficientes, pero pueden ser útiles en situaciones donde necesitas un mayor control sobre el proceso de inversión.
# Ejemplo completo

# Python

# def invertir_cadena(cadena):
#   return cadena[::-1]

# cadena_original = "reconocer"
# cadena_invertida = invertir_cadena(cadena_original)

# print(f"Cadena original: {cadena_original}")
# print(f"Cadena invertida: {cadena_invertida}")

# if cadena_original == cadena_invertida:
#   print("La cadena es un palíndromo")
# else:
#   print("La cadena no es un palíndromo")
# En este ejemplo se muestra una función que revierte una cadena, y luego se utiliza dicha función para determinar si una cadena es un palíndromo o no.






# print(frase[::-1])


# Claro, la línea de código print(frase[::-1]) en Python hace lo siguiente:

# frase: Asume que frase es una variable que contiene una cadena de texto (string).
# [::-1]: Esto es un "slicing" (rebanado) de cadenas con un paso negativo. En Python, el slicing se usa para extraer partes de una secuencia (como una cadena o una lista).
# Cuando se usa [::-1], significa:
# Empieza desde el final de la cadena.
# Termina al principio de la cadena.
# Avanza hacia atrás, un carácter a la vez.
# En efecto, esto invierte la cadena.
# print(): La función print() muestra el resultado en la consola.
# En resumen:

# Esta línea de código toma la cadena almacenada en la variable frase, la invierte y luego imprime la cadena invertida en la consola.







# ejercicio 7
# Claro, vamos a desglosar este código Python línea por línea:

# Línea 1:

# Python

# email = input("Introduce tu correo electrónico: ")
# input(...): Esta es una función incorporada en Python que permite al usuario ingresar texto desde la consola.
# "Introduce tu correo electrónico: ": Este es el mensaje (prompt) que se muestra al usuario, pidiéndole que ingrese su dirección de correo electrónico.
# email = ...: El texto ingresado por el usuario se almacena en la variable email.
# En resumen, esta línea solicita al usuario que ingrese su correo electrónico y guarda esa entrada como una cadena de texto en la variable email.

# Línea 2:

# Python

# print(email[:email.find('@')] + '@ceu.es')
# print(...): Esta función muestra el texto resultante en la consola.
# email[:email.find('@')]: Esto es un ejemplo de "slicing" (rebanado) de cadenas en Python. Permite extraer una parte de la cadena email.
# email.find('@'): Este método busca la posición del carácter @ dentro de la cadena email. Devuelve el índice de la primera aparición de @.
# email[:email.find('@')]: Esto extrae la parte de la cadena email que comienza desde el principio y termina justo antes del carácter @. En otras palabras, extrae el nombre de usuario del correo electrónico.
# + '@ceu.es': Esto concatena (une) la parte extraída del correo electrónico con la cadena '@ceu.es'. Esto reemplaza el dominio original del correo electrónico con '@ceu.es'.
# En resumen:

# Esta línea de código toma el correo electrónico ingresado por el usuario, extrae el nombre de usuario (la parte antes de la @), y luego lo combina con el dominio '@ceu.es', imprimiendo el resultado en la consola.

# Ejemplo de ejecución:

# Si el usuario ingresa el correo electrónico usuario@gmail.com, el código produciría la siguiente salida:

# usuario@ceu.es
# Consideraciones:

# Este código asume que el usuario siempre ingresará una dirección de correo electrónico válida que contenga el carácter @. Si el usuario ingresa una cadena que no contiene @, el método find() devolverá -1, y el slicing podría comportarse de manera inesperada.
# Este código no realiza ninguna validación adicional del formato del correo electrónico.
# Este código asume que se quiere reemplazar el dominio del mail por @ceu.es, sin importar cual sea el dominio ingresado por el usuario.