# Operadores Lógicos
print('--------------------------------------------------------------')
print('Operadores lógicos tabla de verdad (lógica de Boole)')


# and - &
resultado_true_and_true = True & True # True and True (también es válido)
resultado_true_and_false = True & False # True and False (también es válido)
resultado_false_and_true = False and True # False & True
resultado_false_and_false = False and False # False & False

# or
resultado_true_or_true = True | True # True or True (también es válido)
resultado_true_or_false = True | False # True or False (también es válido)
resultado_false_or_true = False or True # False | True
resultado_false_or_false = False or False # False | False

# not
resultado_not_false = not False # el operador ~False no es válido en este ejercicio
resultado_not_true = not True

print('--------------------------------------------------------------')
print('AND o & - Y lógico funciona con and o con & para bits')
print('Para que se cumpla (TRUE) los dos operadores deben ser true, caso contrario es false')
print(f'resultado true and true: {resultado_true_and_true}')
print(f'resultado true and false: {resultado_true_and_false}')
print(f'resultado false and true: {resultado_false_and_true}')
print(f'resultado false and false: {resultado_false_and_false}')
print('--------------------------------------------------------------')
print('OR o | - Y lógico funciona con or o con | (altGR 1) para bits')
print(f'resultado true or true: {resultado_true_and_true}')
print(f'resultado true or false: {resultado_true_and_false}')
print(f'resultado false or true: {resultado_false_and_true}')
print(f'resultado false or false: {resultado_false_and_false}')
print('--------------------------------------------------------------')
print('NOT o ~ - No lógico funciona con not o con ~ (altGR + ) solo para bits')
print(f'resultado not true: {resultado_not_true}')
print(f'resultado not false: {resultado_not_false}')
print('--------------------------------------------------------------')