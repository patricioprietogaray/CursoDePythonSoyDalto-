# Metodos de Listas

# LIST crea una nueva lista
# LIST es una funcion: acepta parametros de cualquier tipo y devuelve una lista
# Si no se ponen las [] genera una excepción.

lista = list(["Hola", "Patricio", 48, True, 0, 0])
print(f'El valor de la lista al principio es: {lista}')

# LEN cuanta la cantidad de elementos de una lista
cantidad_elementos = len(lista)
print(f'La cantidad de elementos de lista es: {cantidad_elementos}')

# APPEND agrega un elemento al final de la lista

# en la variable agregando_con_append obtiene el valor "None"
# agregando_con_append = lista.append("15")
# print(f'Veo que devuelve append a la variable "agregando_con_append": {agregando_con_append}')

# no modifica lo anterior de la siguiente manera
lista.append("15")
print(f'Agrego con append otro dato mas: {lista}')

# INSERT agrega un elemento a la lista en el índice especificado
print('-------------------------------------------------------------------')
ind2= "ElementoDelIndice2"
print(f'Muestro la lista antes de modificarla: {lista}')
lista.insert(2, ind2)
print(f'''En el índice 2 que ahora lo ocupa {lista[2]}; 
      voy a agregarle {ind2} y el índice original 
      se desplazara un índice más o sea al 3 ({lista[3]})''')
print(f'Muestro la lista modificada: {lista}')
print('-------------------------------------------------------------------')
# 2:16:00
# EXTEND agrega varios elementos a la lista al final.
# la lista que se agrega es con []
print(f'Utilizo EXTEND para agregar mas elementos al final de la lista [00,75,74,73]')
lista.extend([00,75,74,73])
print(f'Muestro la lista modificada: {lista}')
print('-------------------------------------------------------------------')

# POP elimina un elemento de la lista, pide indice y devuelve el valor
# pop es un metodo cuyo parametro es el indice a eliminar.
print(f'Muestro la lista antes de modificarla: {lista}')
print(f'Elimino el primer elemento (indice 0) con pop')
lista.pop(0)
print(f'Muestro la lista modificada por POP: {lista}')
print(f'''Elimino el último elemento (indice -1) con pop, 
      si quiero eliminar el anteúltimo es -2 y asi sucesivamente...''')
lista.pop(-1)
print(f'Muestro la lista modificada por POP: {lista}')
print('-------------------------------------------------------------------')
# REMOVE remueve un elemento de la lista, pide valor (si hay varios elimina el primero)
# si no lo encuentra lanza una excepcion.
print(f'Muestro la lista antes de modificarla: {lista}')
print('Elimino un elemento de la lista por su valor (el 0 -indice 5)')
lista.remove(0)
print(f'Muestro la lista modificada por REMOVE: {lista}')
print('-------------------------------------------------------------------')

# CLEAR elimina todos los elementos de la lista. Clear es un metodo
print(f'Muestro la lista antes de modificarla: {lista}')
print('Elimino TODOS los elemento de la lista')
lista.clear()
print(f'Muestro la lista despues de usar CLEAR: {lista}')
print('-------------------------------------------------------------------')
# SORT ordena la lista de forma ascendente y descendente
# solo numerico sin cadenas de texto, devuelve none. sort es un metodo
# primero los numeros, luego booleanos (false=0 y true=1)
lista=[0,1,6,3,5,2,4, True, False, 3.14]
print(f'Muestro la lista antes de modificarla: {lista}')
lista.sort()
print(f'Muestro la lista ordenada: {lista}')
# Muestro la lista ordenada: [0, False, 1, True, 2, 3, 3.14, 4, 5, 6]
print('-------------------------------------------------------------------')
# REVERSE invierte los elementos de una lista
# lista.reverse()
# con reverse se ordena al reves de como estaba la lista anteriormente
# si esta desordenada la muestra exactamente al reves de ese desorden.
# Si esta ordenada con sort, hara lo mismo
# Muestro la lista ordenada con lista.reverse(): [6, 5, 4, 3.14, 3, 2, True, 1, False, 0]
# print(f'Muestro la lista ordenada con lista.reverse(): {lista}')
# print(f'Al reves con lista.reverse(): {lista.reverse()}') --> None
lista.sort(reverse=True)
# al contrario de reverse primero ponen el int y luego el bool
# con sort(reverse=true) ordena de mayor a menor.
# Muestro la lista ordenada con lista.sort(reverse=True): [6, 5, 4, 3.14, 3, 2, 1, True, 0, False]
print(f'Muestro la lista ordenada con lista.sort(reverse=True): {lista}')
# print(f'Al reves con lista.sort(reverse=True): {lista} ') --> None
print('-------------------------------------------------------------------')
# print(dir(lista))
# ['__add__', '__class__', '__class_getitem__', '__contains__', 
# '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', 
# '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', 
# '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', 
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
tupla = (12,23,34,45,56,True,"abc", False, False)
# print(dir(tupla))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
#  '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
#  '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
#  '__subclasshook__', 'count', 'index']

# busca el nombre del elemento dentro de la tupla
print(f'tupla.index(False): {tupla.index(False)}')
# contar la cantidad de elementos que coincidan con 12 
print(f'tupla.count(False): {tupla.count(False)}') 

# las tuplas y los conjuntos son inmutables asique para las tuplas solo index y count

conjunto = {11,22,33,"abc", False, True, True}
# print(dir(conjunto))
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', 
# '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', 
# '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', 
# '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
# '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 
# 'difference_update', 'discard', 'intersection', 'intersection_update', 
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
conjunto.add("def")  
conjunto.add(3000)
conjunto.add(True)
print(f'con el metodo add inserte tres elementos al conjunto: {conjunto}')
print(f'len(conjunto): {len(conjunto)}')
print(f'El conjunto contiene: {conjunto}')