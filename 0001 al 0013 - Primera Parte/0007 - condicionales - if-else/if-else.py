# condicionales if-else
#  if condicion:    
    # accion (código a ejecutar)
    
edad = 19
print(f'Entrada al Bar (tiene {edad} años de edad)')
if edad >= 18:
    print('Es mayor o igual a 18 años de edad')
    print('forma parte del if (True)')
else:
    print('Es menor de edad')
    print('Forma parte del else (False)')

print('Fuera del IF (condicional)') 


# comparar usuarios
contraseña_almacenada="PatoMaestro"
usuario_logueado='''PatoMaestro'''
if contraseña_almacenada == usuario_logueado:
    print('Iniciando la sesión...')
else:
    print('Contraseña equivocada, intentelo de nuevo...')

# acceso=contraseña_almacenada==usuario_logueado
# print(acceso)