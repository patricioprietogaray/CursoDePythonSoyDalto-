

frutas = ['Banana', 'Manzana', 'Pera', 'Naranja', 'Mandarina', 'Kiwi']
print('----------------------------------------------------------------')
print('Me voy a comer todas las frutas')
print('Listo todas las frutas que tengo en el frutero')

for fruta in frutas:
    # las frutas que me voy a comer
    print(f' - {fruta}')
# y me como todas las frutas....

print('----------------------------------------------------------------')
print('Me voy a comer todas las frutas menos la mandarina - (continue)')
# supongamos que no me gusta la mandarina
for fruta in frutas:
    if fruta == 'Mandarina':
        # cuando iteramos y llegamos a la mandarina
        # no la comemos y nos saltamos a la siguiente fruta
        continue   # salta a la siguiente iteración
    print(f'Me voy a comer una {fruta}')
    
print('----------------------------------------------------------------')
print('''Me voy a comer todas las frutas, pero cuando llego a la pera
      me la como y tengo dolor de panza''')
print('y no puedo continuar comiendo - (break)')
# supongamos que cuando como una pera me duele la panza y no puedo continuar
for fruta in frutas:
            # cuando llegamos a la pera
        # la comemos y salimos del ciclo
    print(f'Como una {fruta}') # primero como la fruta y luego me duele la panza
    if fruta == 'Pera':

        break   # salimos del ciclo y continuamos con el código que sigue fuera del for
else:
    print('No me comí todas las frutas') # no se ejecuta porque salimos del ciclo con break
print('----------------------------------------------------------------')

# iterar una cadena de texto
print('Iterar una cadena de texto')

texto = 'Hola Patro'
for letra in texto:
    print(letra)

print('----------------------------------------------------------------')

numeros = [1,4,5,8,10]
print('Quiero duplicar la cantidad de bitcoins que tengo')
print(f'Listo los bitcoins que tengo: {numeros}')
# creamos una lista vacia para guardar los numeros duplicados
numeros_duplicados = list()
for numero in numeros:
    # duplicamos la cantidad de bitcoins que tenemos
    # y los guardamos en la lista numeros_duplicados utilizando el método append
    numeros_duplicados.append(numero * 2)
print(f'Dupliqué mi capital: {numeros_duplicados}')

print('----------------------------------------------------------------')
print('Mismo resultaco con dos lineas de código')
numeros = [1,4,5,8,10]
print('Quiero duplicar la cantidad de bitcoins que tengo')
print(f'Listo los bitcoins que tengo: {numeros}')
numeros_duplicados = [num * 2 for num in numeros]
print(f'Dupliqué mi capital: {numeros_duplicados}')
print('----------------------------------------------------------------')

