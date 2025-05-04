# # Escribe un programa que muestre por pantalla la cadena "Hola Mundo!"
# print("Hola Mundo!")

# # Escribe un programa que almacena la cadena
# # "Hola Mundo! en una variable y luego muestre 
# # por pantalla el contenido de la variable

# cadena = "Hola Mundo!"
# print(cadena)

# # Escribir un programa que pregunte el nombre del usuario 
# # en la consola y despues de que el usuario introduzca 
# # muestre por pantalla la cadena "Hola <nombre>!", donde 
# # <nombre> es el nombre que el usuario haya introducido.

# nombre = input("Introduzca su nombre: ")
# print(f'Hola {nombre}!')

# # Escribir un programa que muestre por pantalla el resultado 
# # de la siguiente operación aritmética

# #    /  3  +  2 \  2
# #    |  ------- |
# #    |   2 x 5  | 
# #    \          /

# print(((3+2)/(2*5))**2)

# # Escribir un programa que pregunte al usuario por el 
# # número de horas trabajadas y el coste por hora. 
# # Despues debe mostrar por pantalla la paga que le 
# # corresponde

# horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
# coste_hora = float(input("Coste por hora trabajada: "))
# paga = horas_trabajadas * coste_hora
# print(f'La paga que le corresponde es ${paga}')

# # Escribir un programa que lea un entero positivo, n, 
# # introducido  por el usuario y despues muestre en pantalla 
# # la suma de todos los enteros desde 1 hasta n. 
# # La suma de los n primeros enteros positivos puede ser 
# # caluculada de la siguiente forma:

# #         n(n+1)
# # suma = ---------
# #           2

# contador = int(input('Introduzca un numero entero positivo: '))
# suma = float((contador*(contador+1))/2)
# print(f'La suma total es: {suma}')

# # Escribir un programa que pida al usuario su peso (en kg) 
# # y estatura (en metros), calcule el índice de masa corporal 
# # y lo almacene en una variable, 
# # y muestre por pantalla la frase Tu índice de masa corporal 
# # es <imc> donde <imc> es el índice de masa corporal calculado 
# # redondeado con dos decimales.

# kg = float(input('Ingrese su peso en Kg.: '))
# estatura = float(input('Ingrese su estatura en metros: '))
# indice_masa_corporal = kg / estatura **2
# print(f'Tu índice de masa corporal es: {indice_masa_corporal}')
# print('''Bajo: menos de 18.5
# Normal: 18.5 – 24.9
# Sobrepeso: 25.0 – 29.9
# Obesidad I: 30.0 - 34.9
# Obesidad II: 35.0 - 39.9
# Obesidad III: Más de 39.9''')

# # Escribir un programa que pida al usuario dos números enteros 
# # y muestre por pantalla la <n> entre <m> da un cociente <c> 
# # y un resto <r> donde <n> y <m> son los números introducidos 
# # por el usuario, y <c> y <r> son el cociente y el resto de 
# # la división entera respectivamente.

# n = int(input('Ingrese un numero entero (dividendo): '))
# m = int(input('Ingrese un numero entero (divisor): '))
# c = n // m
# r = n % m
# print(f'Se divide {n} por {m}, cuyo cociente es {c} y su resto es {r}')

# # Una juguetería tiene mucho éxito en dos de sus productos: 
# # payasos y muñecas. Suele hacer venta por correo y la empresa de 
# # logística les cobra por peso de cada paquete así que deben calcular 
# # el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# # Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el 
# # número de payasos y muñecas vendidos en el último pedido y 
# # calcule el peso total del paquete que será enviado.

# print('Venta del día')
# cant_payaso = float(input('Ingrese la cantidad de payasos: '))
# cant_muñeca = float(input('Ingrese la cantidad de muñecas: '))
# # peso = (payaso * 0.112)+(muñeca * 0.075)
# peso_payaso = 0.112
# peso_muñeca = 0.075
# peso = ((cant_payaso * peso_payaso)+(cant_muñeca * peso_muñeca))
# print(f'El peso total del pedido es: {peso} Kg.')

# Imagina que acabas de abrir una nueva cuenta de ahorros 
# que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad 
# de dinero depositada en la cuenta de ahorros, 
# introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

# capital = float(input('Ingrese el dinero inicial en la caja de ahorros: $'))
# tasa_interes_anual = float(4/100)

# periodos_tiempo_en_años = 1.0
# intereses_primer_año = capital * tasa_interes_anual * periodos_tiempo_en_años
# capital_finalizar_primer_año = intereses_primer_año + capital

# periodos_tiempo_en_años = 2.0
# intereses_segundo_año = capital_finalizar_primer_año * tasa_interes_anual * periodos_tiempo_en_años
# capital_finalizar_segundo_año = capital_finalizar_primer_año + intereses_segundo_año

# periodos_tiempo_en_años = 3.0
# intereses_tercer_año = capital_finalizar_segundo_año * tasa_interes_anual * periodos_tiempo_en_años
# capital_finalizar_tercer_año = capital_finalizar_segundo_año + intereses_tercer_año



# print(f'''
#       En la caja de ahorro hay un capital inicial de ${capital:.2f}.
#       Dejará el dinero inmobil en la caja de ahorro durante {periodos_tiempo_en_años} años.
#       Los intereses anuales serán del {tasa_interes_anual * 100} %.
#       Los intereses generados durante el primer año es de ${intereses_primer_año:.2f}
#       El capital acumulado al finalizar el primer año es de ${capital_finalizar_primer_año:.2f}
#       Los intereses generados durante el segundo año es de ${intereses_segundo_año:.2f}
#       El capital acumulado al finalizar el segundo año es de ${capital_finalizar_segundo_año:.2f}
#       Los intereses generados durante el tercer año es de ${intereses_tercer_año:.2f}
#       El capital acumulado al finalizar el tercer año es de ${capital_finalizar_tercer_año:.2f}
#       ''')

# # interes_anual = float(0.04)

# # intereses_generados = capital * tasa_de_interes_periodico * numero_periodos_tiempo

# # print(f'Los intereses generados por {numero_periodos_tiempo} años son $ {intereses_generados}:.2f')


