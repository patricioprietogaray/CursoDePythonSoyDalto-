# Un dato compuesto comprende varios tipos de datos simples.
# lista es un tipo de matriz
compras_lista=["galletitas","bagley","surtidas",1502.22, True]

# lista[indice]---> comienza por el indice 0
print(compras_lista[2])
print(compras_lista)
print("modifico el primer elemento de compras_lista")

# las listas se pueden modificar
compras_lista[0]="Galletitas"
print(compras_lista)

# borro la lista
# del compras_lista
# print(compras_lista)   # Error lista is not defined


# para mostrar el valor de un indice sea tupla o lista 
# el indice se lo visualiza entre corchetes
compras_tupla=("galletitas","bagley","surtidas",1502.22, True)
print(compras_tupla[0])

# puedo redefinir una tupla
compras_tupla=("Carne", "Coto", "Asado", 12000, True)
print(compras_tupla)

# modifico una tupla ya definida   TypeError: 'tuple' object does not support item assignment                          
# compras_tupla[0]="Galletitas"

# comentar codigo para que no se ejecute
# tupla=("leche","pan","aceitunas","galletitas","carne","fideos")
# print(tupla(0))

# Otro tipo de dato es conjuntos (set)
# no se puede acceder por el índice muestra los datos en forma aleatoria
# se declaran con {} no muestra datos duplicados (en tupla y lista se muestran)
compra_conjunto={"Fideos", "Matarazo", "Tallarines", 1800, False}
print(compra_conjunto)


# diccionario es similar al Json de JS, en vez de indices y dato
# la estructura es key:value (clave: valor) y se usan llaves
# no tiene un orden (índice)

compra_diccionario={
    'Producto':'Fideos',
    'Marca': 'Matarazo',
    'Tipo': 'Tallarines',
    'Precio': 1800,
    'Stock': False
}

print(compra_diccionario)

# El diccionario no se maneja con índices
# print(compra_diccionario[0]) ERROR keyError

# El diccionario se maneja con clave
print(compra_diccionario["Marca"])