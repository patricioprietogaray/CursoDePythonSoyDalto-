# def frase(nombre, apellido, adjetivo):
#     return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

# # debo respetar el orden nombre (Pepe) apellido (Argento) adjetivo (sufrido)
# print(frase('Pepe', 'Argento', 'sufrido')) # --> Hola Pepe Argento, sos muy sufrido

# # cambio de lugar los parametros a ver que onda
# print(frase('Argento', 'sufrido', 'Pepe')) # --> Hola Argento sufrido, sos muy Pepe
# #  lo que pasa es que el primer parámetro se va a nombre, el segundo a apellido
# # siempre respeta el orden de los argumentos cuando se llama a la funcion

# print(frase(adjetivo='sufrido', apellido='Argento', nombre='Pepe')) 
# # ahora si funciona --> Hola Pepe Argento, sos muy sufrido

# # print(frase(adjetivo='sufrido', apellido='Argento', 'Pepe')) 
# # SyntaxError: positional argument follows keyword argument 
# # El argumento posicional no puede aparecer después de los argumentos de palabras clave
# # una vez que se asigna un argumento posicional se debe hacer en los demas (Pepe no tiene)



# PARAMETRO POR DEFECTO nacionalidad, si lo omito queda como Argentina
# si paso el parametro queda como el texto que le envio (Boliviana)
def frase(nombre, nacionalidad='Argentina'):
    print(f'Hola {nombre} tu país de origen es {nacionalidad}')
    
mensaje = frase('Horacio Quiroga')
print(mensaje)  # --> Hola Horacio Quiroga tu país de origen es Argentina

mensaje = frase('Roberto del Cuarteto de Nos', 'Uruguaya')
print(mensaje)  # --> Hola Roberto del Cuarteto de Nos tu país de origen es Uruguaya

mensaje = frase('Marciano Cantero')
print(mensaje)