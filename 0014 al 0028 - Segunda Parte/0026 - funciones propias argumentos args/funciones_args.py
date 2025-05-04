# # utilizo el parámetro "args" siempre al final
# # nombre es una variable comun al que le paso 'Pepe'
# # numeros precedido por un asterisco (*numeros) son todos los datos
# # que estan al final de los argumentos pasados (5,9,7,8,5)
# # tienen que ser del mismo tipo para luego sumarse
# # si es de otro tipo va a haber error

# def suma(nombre, *numeros):
#     return nombre, sum(numeros)

# print(suma("Pepe",5,9,7,8,5))   # --> ('Pepe', 34)


# forma óptima de sumar valores
def sumar(numeros):
    # print(type(numeros)) # --> <class 'list'>
    # print(type(*numeros)) # --> TypeError: type() takes 1 or 3 arguments
    # print(type([*numeros])) # --> <class 'list'>
    return sum([*numeros])

resultado = sumar([5,9,7,8,5])
print(resultado) # --> 34
# print(type(resultado)) # --> <class 'int'>
# print(type([5,9,7,8,5])) # --> <class 'list'>