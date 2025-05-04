# Teoría de conjuntos (parte de ella)

# Tengo dos conjuntos
#  A = {2,4,6}
#  B = {1,2,3,4,5,6}

# Si se analizan los elementos desde la perspectiva del conjunto A, 
# se puede decir que A es un conjunto y que B es un superconjunto. 
# B es un superconjuto porque contiene al conjunto A en su totalidad.

# Si se analizan los elementos desde la perspectiva del conjunto B,
# se puede decir que B es un conjunto y que A es un subconjunto.
# A es un subconjunto porque a es contenido en su totalidad por B.

# Vamos al código
conjunto_A = {2,4,5,6}
conjunto_B = {1,3,5}
print(f'Conjunto A = {conjunto_A}')
print(f'Conjunto B = {conjunto_B}')

# verificamos si el conjunto A es un subconjunto de B
# ..todo lo que esta en A, ¿Esta en B?
resultado_B_es_un_subconj_de_A = conjunto_B.issubset(conjunto_A)
#                                conjunto_b <= conjunto_A   misma forma de verificarlo
print(f'Verificar si B es subconjunto de A: {resultado_B_es_un_subconj_de_A}')

# ..todo lo que esta en B, ¿Esta en A?
resultado_A_es_un_subconj_de_B = conjunto_A.issubset(conjunto_B)
print(f'Verificar si A es subconjunto de B: {resultado_A_es_un_subconj_de_B}')

resultado_B_es_un_superconj_de_A = conjunto_B.issuperset(conjunto_A)
print(f'Verificar si B es superconjunto de A: {resultado_B_es_un_superconj_de_A}')
#                                conjunto_b > conjunto_A   misma forma de verificarlo

resultado_A_es_un_superconj_de_B = conjunto_A.issuperset(conjunto_B)
print(f'Verificar si A es superconjunto de B: {resultado_A_es_un_superconj_de_B}')


# para verificar si algun elemento en comun (en este caso nros en comun)
# es true cuando no coinciden, es false cuando al menos un elemento tienen en comun
# los conjuntos evaluados.
resultado=conjunto_A.isdisjoint(conjunto_B)
print(f'El conjunto A tiene algún elemento en comun con B?: {resultado} (True: no hay coincidencias)')

# https://youtu.be/nKPbfIU442g?t=12253