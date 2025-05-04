# ITERAR DICCIONARIOS

# https://youtu.be/nKPbfIU442g?t=13715

animales = {
    'pez': 'nada',
    'gato': 'maulla',
    'perro': 'ladra',
    'leon': 'ruge',
    'lechuza': 'ulula'
}

numeros = {
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco'
}

print(f'Utilizo print para mostrar los Animales: {animales}')

# clave : valor
# pez : nada

# cuando se itera un diccionario, se itera por defecto las claves

for loquesea in animales:
    print(loquesea)

# para iterar los valores, se debe hacer de la siguiente manera 
# (que no es la forma correcta o es la mas larga)
for loquesea in animales:
    clave = loquesea[0]
    valor = loquesea[1]
    print(f'la clave es {clave} y el valor es {valor}')

# resultado (cualquier cosa):
# la clave es p y el valor es e
# la clave es g y el valor es a
# la clave es p y el valor es e
# la clave es l y el valor es e
# la clave es l y el valor es e

for loquesea in animales.items():
    clave = loquesea[0]
    valor = loquesea[1]
    print(f'la clave es {clave} y el valor es {valor}')


# resultado (correcto DICCIONARIO.ITEMS()):
# la clave es pez y el valor es nada
# la clave es gato y el valor es maulla
# la clave es perro y el valor es ladra
# la clave es leon y el valor es ruge
# la clave es lechuza y el valor es ulula


# recorriendo un diccionario para obtener la clave y el valor
# vamos a simplificar el codigo del bucle anterior
# defino dos variables clave y valor y las asigno en la misma linea
for key, value in numeros.items():
    print(f'la clave es {key} y el valor es {value}')





# for animal, sonido in animales.items():
    # print(f'{animal} hace {sonido}')

