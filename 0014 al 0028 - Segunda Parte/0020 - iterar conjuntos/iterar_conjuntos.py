# iterar conjuntos

animales = {'pez', 'gato', 'perro'}
numeros = {1,2,3,4,5}


print(f'Con print muestro de un saque a todos los elementos de animales: {animales}')

print('-------------------------------------------------')

print('Ahora voy a iterarlos con for:')
for animal in animales:
    print(f'El valor de animal es : {animal}')
    print(f'El valor de animales es: {animales}')
    

for multiplicado_por_dos in numeros:
    print(f'Multiplico por dos: 2 x {multiplicado_por_dos} =  {multiplicado_por_dos * 2}')
    

# ¿como iterar dos listas a la vez???
for numero, animal in zip(numeros, animales):
    print(f'Iteración con numero {numero}, animal {animal}')

for num in range(0,5):
    print(f'Contando: {num}')


for num in range(5):
    print(f'Contando(0-4): {num}')
    
# NO FUNCIONA CON CONJUNTOS (set())
# recorrer una lista de una manera que no es óptima
# for num in range(len(numeros)):
#     print(numeros[num])     # -->  print(numeros[0]) ==> 1 (el valor del elemento con indice 0)
#     print(f'num devuelve el indice: {num}, numeros: {numeros}')
    

# FORMA CORRECTA DE RECORRER UNA LISTA POR EL INDICE
for num in enumerate(numeros):
    # num es una tupla con dos variables
    # el primero o num[0] es el indice
    # el segundo o num[1] es el valor
    print(type(num))
    print(num)
    print('-------------')
    
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'En el índice {indice} se encuentra el valor {valor}')
    # print(num) # --> (0, 1)

for animal in enumerate(animales):
    indice = animal[0]
    valor = animal[1]
    print(f'En el índice {indice} se encuentra el valor {valor}')
    # print(animal) # --> (0, 'pez')
    

for a,b in enumerate(animales):
    print(f'(a,b) --> En el indice {a} está el valor {b}')


print('----------------------------')
print('For Else')
paises=[]
for pais in paises:
    print(pais)
else:
    print('El bucle for se terminó si hay datos se muestran antes, si no esta linea siempre se ve')


print('----------------------------')
print('For Else')
paises=['Argentina', 'Brasil']
for pais in paises:
    print(pais)
else:
    print('El bucle for se terminó si hay datos se muestran antes, si no esta linea siempre se ve')


# DE ESTA MANERA NO FUNCIONA EN CONJUNTOS NI ES RECOMENDABLE PARA LISTAS
# recorrer una lista de una manera que no es óptima
# for num in range(len(numeros)):
#     print(numeros[num])     # -->  print(numeros[0]) ==> 1 (el valor del elemento con indice 0)
#     print(f'num devuelve el indice: {num}, numeros: {numeros}')

