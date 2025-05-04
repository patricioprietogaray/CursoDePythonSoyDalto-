# Bucle while
# El bucle while a diferencia del for que se ejecuta siempre 
# mientras recorra la lista, conjunto, diccionario, etc.

# El bucle while se ejecutará mientras se cumpla cierta condicion cada vez que 
# pega la vuelta se revisa dicha condicion.

# Ejemplo: voy a contar desde cero hasta el numero sea menor a 10 
# y deseo que ese numero se muestre por pantalla


contador = 0

while contador < 10:
    print(contador)
    # el codigo se ejecuta infinitas veces porque contador es siempre cero
    # para eso voy a cambiar el contador sumandolo
    contador += 1
    # con el incremento cuando contador sea 9 muestra por pantalla
    # se incrementa y ahora contador vale 10 
    # al comparar 10 < 10?  False y sale del bucle. 



    