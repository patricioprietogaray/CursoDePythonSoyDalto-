#  Ejercicio 2

# Suponiendo que una persona promedio habla dos palabras por segundo
# a) pedir al usuario cualquier texto real y que diga cuantas palabras dijo y 
#   en cuanto tiempo las dijo       (en 4seg dije 8 palabras)
# b) Si tarda más de un minuto decirle "para flaco tampoco te pido un testamento"
# c) Dalto habla un 30% más rápido, ¿cuanto tardaría dalto en decirlo?

print('Ejercicio 2 - Interacción con el usuario y calculo de palabras dichas en un tiempo determinado')
print('----------------------------------------------------------------------------------------------')
print('''Lea el siguiente texto y grabelo en un audio, de 85 palabras,
      luego vea que tiempo duro la grabación.''')
print('----------------------------------------------------------------------------------------------')
print('''"El jardín de senderos que se bifurcan".

La candente mañana de febrero en que Beatriz Viterbo murió, 
después de una imperiosa agonía que no se rebajó un solo instante ni al sentimentalismo 
ni al miedo, noté que las carteleras de fierro de la Plaza Constitución habían 
renovado no sé qué aviso de cigarrillos rubios; el hecho me dolió, pues comprendí 
que el incesante y vasto universo ya se apartaba de ella y que ese cambio era el 
primero de una serie infinita.

                        Jorge Luis Borges''')
print('----------------------------------------------------------------------------------------------')
palabras=85
promedio_palabras_segundo=0.5
tiempo_en_segundos = input('Ingrese el tiempo de grabación del audio en segundos: ')
palabras_por_segundo = float(tiempo_en_segundos)/float(palabras)
print(f'Usted ha dicho {palabras_por_segundo:.2f} palabras por segundo')
print(f'El promedio son {promedio_palabras_segundo} palabras por segundo!')
print('----------------------------------------------------------------------------------------------')
if int(tiempo_en_segundos) > 60:
    print('Pero pará flaco!!!! tampoco te pido un testamento. :)')
    print('----------------------------------------------------------------------------------------------')
dalto_tardaría = ((float(palabras)*float(promedio_palabras_segundo))*0.70)
print(f'Dalto hubiera tardado un 30% menos, unos {dalto_tardaría:.2f} segundos!')
print('----------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------')
print('Me fui a la bosta, jajajaja')

# La candente mañana de febrero en que Beatriz Viterbo murió, después de una imperiosa agonía que no se rebajó un solo instante ni al sentimentalismo ni al miedo, noté que las carteleras de fierro de la Plaza Constitución habían renovado no sé qué aviso de cigarrillos rubios; el hecho me dolió, pues comprendí que el incesante y vasto universo ya se apartaba de ella y que ese cambio era el primero de una serie infinita.



mensaje=input('Ingrese una frase para calcular el tiempo que tardaría en promedio decirla: ')
lista_mensajes = mensaje.split(' ')
# print({mensaje})
# print([lista_mensajes])
palabras = len(lista_mensajes)
print(f'Usted ha escrito {palabras} palabras.')
tiempo_en_segundos = palabras * promedio_palabras_segundo
print(f'Usted ha escrito el equivalente de {tiempo_en_segundos:.2f} segundo a un ritmo promedio.')
print('----------------------------------------------------------------------------------------------')
if float(tiempo_en_segundos) > 60.0:  # palabras > 120
    print('Pero pará flaco!!!! tampoco te pido un testamento. :)')
    print('----------------------------------------------------------------------------------------------')
dalto_tardaría = ((float(palabras)*float(promedio_palabras_segundo))*0.70)
print(f'Dalto hubiera tardado un 30% menos, unos {dalto_tardaría:.2f} segundos!')
print('----------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------')