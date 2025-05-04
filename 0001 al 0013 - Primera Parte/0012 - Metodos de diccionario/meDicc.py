# Métodos de Diccionario

diccionario = {
    'nombre' : 'Patricio',
    'apellido' : 'Prieto Garay',
    'seguidores' : 4
}
print('----------------------------------------------------')
# keys() -> devuelve las claves (también nos sirve para iterar)
claves = diccionario.keys()
print(f'Uso de keys()')

# diccionario = {
#     0 : 'Patricio',
#     1 : 'Prieto Garay',
#     2 : 4
# }
# claves = diccionario[0]    ---> 'Patricio'
# una lista es similar a un diccionario
print(claves)
# las keys son las claves y value o valor es el contenido de dichas claves

print('----------------------------------------------------')
print(f'Uso de get()')
# get() -> devuelve el valor de una clave, si no encuentra por 
# el nombre de la clave devuelve None (no tiene valor. como el undefined de JS)
# el programa continúa
clave1 = diccionario.get("nombre")
print(clave1)
print(f'Hola! Mi nombre es: {diccionario.get('nombre')}')

# otra forma de mostrar los datos, si no encuentra hay excepción 
# (buscar Nombre en vez de nombre) es decir que el programa se para completamente
# y no continua
print(f'Hola! Mi nombre es: {diccionario["apellido"]}')

print('----------------------------------------------------')
print(f'Uso de pop()')
# pop() -> elimina un elemento de uno en uno (no se puede "nombre", "apellido")
print(f'Elimino el nombre y apellido')
diccionario.pop("nombre")
diccionario.pop("apellido")
print(diccionario)

print('----------------------------------------------------')
print(f'Uso de items()')
# items() -> para iterar el diccionario
diccionario_iterable = diccionario.items()
print(f'Muestro el diccionario sin iterar como se hace hasta ahora: {diccionario}')
print(f'Diccionario iterable: {diccionario_iterable}, como si fuera una lista!')


print('----------------------------------------------------')
print(f'Uso de clear()')
# clear() -> elimina todos los elementos terminas con el diccionario vacio
print(f'Diccionario {diccionario}')
print(f'Uso clear y borro todo el diccionario ....')
diccionario.clear()
print(f'Diccionario {diccionario}')