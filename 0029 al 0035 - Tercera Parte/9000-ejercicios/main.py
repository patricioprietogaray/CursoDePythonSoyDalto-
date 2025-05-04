# Crear un programa que permita hacer una operacion matemática con todas las funciones
# de una calculadora
# contendrá un modulo de suma (2 operandos)
# contendrá un modulo de resta (2 operandos)
# contendrá un modulo de multiplicacion (2 operandos)
# contendrá un modulo de division (2 operandos)
# contendrá un modulo de modulo (2 operandos)
# contendrá un modulo de radicacion (1 operando)
# contendrá un modulo de potenciacion (1 operandos)

# Crear un modulo que me permita mostrar un menu para las operaciones

# import modulos.operaciones_algebraicas

# # muestra las funciones que tiene operaciones algebraicas
# print(dir(modulos.operaciones_algebraicas))
# # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# # '__package__', '__spec__', 
# # 'dividir', 'factorial', 'hypotenusa', 
# # 'math', 'modulo', 
# # 'multiplicar', 'numero_e', 'numero_pi', 'radicacion', 'restar', 'sumar']


#    carpeta.archivo.py (sin .py)
# from modulos.operaciones_algebraicas import sumar, restar, multiplicar, dividir, modulo
# from modulos.menu_principal import presentacion_menu

# para ver el namespace de este modulo
# cuando es llamado por otro archivo
print(f'{__name__} de main.py')

# con import
import modulos.operaciones_algebraicas
import modulos.menu_principal
# a cada acceso debo poner
# modulos.menu_principal.presentacion_menu()
# y asi con todos


opcion, a, b = modulos.menu_principal.presentacion_menu()

if opcion == 0 and a == 0 and b == 0:
    print('Fin del programa')

if opcion == 1:
    print(f'La suma entre {a} y {b} = {sumar(a,b)}')
elif opcion == 2:
    print(f'La resta entre {a} y {b} = {restar(a,b)}')
elif opcion == 3:
    print(f'La multiplicacion entre {a} y {b} = {multiplicar(a,b)}')
elif opcion == 4:
    print(f'La división entre {a} y {b} = {dividir(a,b)}')
elif opcion == 5:
    print(f'La módulo (resto de la división) entre {a} y {b} = {modulo(a,b)}')
    
    



# luego de hacer el ejercicio continuar 
# https://youtu.be/nKPbfIU442g?t=20812