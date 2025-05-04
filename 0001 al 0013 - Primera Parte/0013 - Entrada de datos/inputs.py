# Entrada de datos
# input siempre interpreta la entrada como un texto o string

nombre = input('Ingrese su nombre: ')
print(f'El nombre igresado es: {nombre}')
correcto = input('Es correcto (s/n): ')
if correcto == 'S' or correcto == 's':
    print(f'Hola {nombre}!')
else:
    print('Gracias por usar este software!')

print(type(nombre))
print('---------------------------------------------------')


numero = input('Ingrese un numero entero: ')
print(f'Si no se convierte a integer al multiplicarlo por 2 se concatena: {numero*2}')
print(type(numero))
print('Convirtiendo numero ingresado (string) a entero')
numero_entero=int(numero)
print(f'Número multiplicado por 2: {numero_entero*2}')
print(type(numero_entero))
print('---------------------------------------------------')


numero = input('Ingrese un numero decimal: ')
print(f'Si no se convierte a integer al multiplicarlo por 2 se concatena: {numero*2}')
print(type(numero))
print('Convirtiendo numero ingresado (string) a entero')
numero_decimal=float(numero)
print(f'Número multiplicado por 2: {numero_decimal*2}')
print(type(numero_decimal))
print('---------------------------------------------------')

# 2:47:00