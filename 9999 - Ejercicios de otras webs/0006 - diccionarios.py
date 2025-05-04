# Ejercicios de Diccionarios
# Ejercicio 1
# Escribir un programa que guarde en una variable 
# el diccionario 
# {'Euro':'€', 
#  'Dollar':'$', 
#  'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo 
# o un mensaje de aviso si la divisa no está en el diccionario.

# divisa = {
#     'Euro':'€',
#     'Dollar':'u$s',
#     'Yen':'¥',
#     'Peso':'$'    
# }

# # print(divisa.keys()) # --> dict_keys(['Euro', 'Dollar', 'Yen', 'Peso'])
# # print(divisa.values()) # --> dict_values(['€', 'u$s', '¥', '$'])
# # print(divisa.items()) # --> dict_items([('Euro', '€'), .... ('Peso', '$')])

# buscar_divisa = input('Ingrese la divisa: ')

# buscarCapitalize = buscar_divisa.capitalize()

# if buscarCapitalize in divisa:
#     simbolo = divisa[buscarCapitalize]
#     print(f'{buscarCapitalize} esta en el diccionario y su simbolo es {simbolo}')
# else:
#     print(f'{buscarCapitalize} no está en el diccionario')




# Ejercicio 2
# Escribir un programa que pregunte al usuario 
# su nombre, edad, dirección y teléfono 
# y lo guarde en un diccionario. 
# Después debe mostrar por pantalla 
# el mensaje <nombre> tiene <edad> años, vive en <dirección> 
# y su número de teléfono es <teléfono>.

# nomb = input('Ingrese su nombre: ')
# edad = int(input('Ingrese la edad en años: '))
# dire = input('Ingrese la dirección (formato calle N° nro): ')
# tele = input('Ingrese el telefono: ')

# datos = dict({
#     'nombre': nomb,
#     'edad': edad,
#     'direccion': dire,
#     'telefono': tele
# })

# print(f'''Los datos ingresados son:
#                                     {datos}''')

# print(f'''{datos['nombre'].capitalize()} 
#                 tiene {datos['edad']} años, 
#                 vive en {datos['direccion']} 
#                 y su número de teléfono es {datos['telefono']}''')


# Ejercicio 3
# Escribir un programa que guarde en un diccionario 
# los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio 
# de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar 
# un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

# verdulería = {
#     'Platano':  1.35,
#     'Manzana':  0.80,
#     'Pera':     0.85,
#     'Naranja':  0.70
# }

# # print(verdulería)
# print(f'Lista de precios: {verdulería}')
# fruta = input('¿Qué fruta quiere comprar?: ')
# kilos = float(input('¿Cuantos kilos desea comprar?: '))

# frutaCapitalizada = fruta.capitalize()

# if frutaCapitalizada in verdulería:
#     print(f'''
#           Usted compró {frutaCapitalizada}, 
#           la cantidad de kilos {verdulería[frutaCapitalizada]:.2f} 
#           por un total de ${float(verdulería[frutaCapitalizada] * kilos):.2f}.''')
# else:
#     print(f'Lo siento no tenemos {fruta}!')

# # mostrar el valor --> diccionario.get[clave]
# print(verdulería.get('Platano'))




# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha en formato 
# dd de <mes> de aaaa donde <mes> es el nombre del mes.

# meses = {
#     1:'Enero',
#     2:'Febrero',
#     3:'Marzo',
#     4:'Abril',
#     5:'Mayo',
#     6: 'Junio',
#     7: 'Julio',
#     8: 'Agosto',
#     9: 'Septiembre',
#     10: 'Octubre',
#     11: 'Noviembre',
#     12: 'Diciembre'
# }

# fecha_input = input('Ingrese una fecha: ')
# fecha_lista = fecha_input.split('/')

# dia = int(fecha_lista[0])
# mes_control = int(fecha_lista[1])
# año_control = 0

# if int(fecha_lista[2]) >=0 and int(fecha_lista[2]) < 100:
#     if int(fecha_lista[2]) >= 30:
#         año_control = 1900 + int(fecha_lista[2])
#     else:
#         año_control = 2000 + int(fecha_lista[2])
# elif int(fecha_lista[2]) >= 100 and int(fecha_lista[2]) <= 999:
#     año_control = 1000 + int(fecha_lista[2])
# elif int(fecha_lista[2]) >= 1000 and int(fecha_lista[2]) <= 9999:
#     año_control = int(fecha_lista[2])

# print(f'''En Mar del Tuyú a los {dia:02} días del mes de {meses.get(mes_control)} de {año_control}, 
#       siendo las 10:00, se presenta Juan Perez y concedida la palabra dice ....''') 




# Ejercicio 5
# Escribir un programa que almacene el diccionario 
# con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
# y después muestre por pantalla los créditos 
# de cada asignatura en el 
# formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, 
# y <créditos> son sus créditos. 
# Al final debe mostrar también el número total de créditos del curso.



# creditos = {
#     'Matemáticas': 6,
#     'Fisica': 4,
#     'Química': 5,
#     'Lengua': 8
# }

# diccionario = {'clave' : valor }
# diccionario --->  muestra los datos de todo el diccionario
# for clave in diccionario:
#   f'mostrar la clave {clave}; mostrar el valor {diccionario[clave]}'

# asignatura = ''
# creditos = 0
# creditos_acumulados = 0
# creditos_alumno = {}

# # hacer siempre que sea verdad (o sea siempre hace el bucle)
# while True:
#     asignatura = input('Ingrese la asignatura: (presione z para salir) ')
#     # si presiona z sale del bucle
#     if asignatura.lower() == 'z' or asignatura.lower() == 'Z':
#         break
#     creditos = int(input('Ingrese los creditos (del 1 al 10): '))
#     # agregar un dato (clave: valor) al diccionario
#     # diccionario[clave] = valor
#     creditos_alumno[asignatura] = creditos

# print('Las asignaturas con sus creditos son:')
# print(creditos_alumno)
# for credito in creditos_alumno:
#     print(f'La Asignatura {credito} tiene {creditos_alumno[credito]} créditos.')
#     creditos_acumulados += creditos_alumno[credito]

# print(f'Los créditos acumulados son: {creditos_acumulados}')
# asignatura = input('Ingrese la asignatura que se muestra en el listado: ')

# Ejercicio 6
# Escribir un programa que cree un diccionario vacío 
# y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse 
# el contenido del diccionario.

# datos = {}

# print('Ingrese los datos de una sola persona. Si clave es Z sale del programa.')
# while True:
#     clave = input('Ingrese la denominacion de la clave (por ej. nombre): ')
#     if clave == 'z' or clave == 'Z':
#         print('Final del programa los datos son: ')
#         print(datos)
#         print('-------------------------------------------------------------------')
#         break
#     valor = input('Ingrese su valor (tipo string): ')
#     datos[clave] = valor
#     print(datos)



# Ejercicio 7
# Escribir un programa que cree un diccionario simulando 
# una cesta de la compra. 
# El programa debe preguntar el artículo y su precio 
# y añadir el par al diccionario, hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla la lista de la compra 
# y el coste total, con el siguiente formato

# # Lista de la compra	
# # Artículo 1	Precio
# # Artículo 2	Precio
# # Artículo 3	Precio
# # …	…
# # Total	Coste


# print('Lista de compras, agregar al carrito')
# print('Z o z para salir')
# canasto_compras = {}
# articulo = ''
# precio = 0.0
# total = 0.0
# while True:
#     articulo = input('Ingrese un artículo: ')
#     if articulo == 'Z' or articulo == 'z':
#         break
#     precio = float(input('Ingrese su precio (0.00) $: '))
#     if precio == 0.0:
#         print('Nada es gratis en la vida')
#         continue
#     canasto_compras[articulo] = precio
#     total += precio

# # mostrar los datos
# # Lista de la compra	
# # Artículo 1	Precio
# # Artículo 2	Precio
# # Artículo 3	Precio
# # …	…
# # Total	Coste

# print(' *** Lista de Compras *** ')
# for art in canasto_compras:
#     print(f'Articulo: {art} $ {canasto_compras[art]}')
# print(f'El costo total de la compra es ${total}')



# Ejercicio 8
# Escribir un programa que cree un diccionario 
# de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés 
# separadas por dos puntos, 
# y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# diccionario = {}

# print('Diccionario Ingles - Español')
# print('Presione "Z" para salir')
# while True:
#     ingles = input('Ingrese una palabra en ingles: ')
#     if ingles == 'Z' or ingles == 'z':
#         break
#     español = input('Ingrese su traduccion en español: ')
#     if español == 'Z' or español == 'z':
#         break
#     diccionario[español]=ingles

# # muestro lo que contiene todo el diccionario
# # print(f'En el diccionario: {diccionario}')



# # frase en español a traducir
# frase_en_español = input('Ingrese su frase en español (sin comas ni puntos) que desea traducir: ')

# # separar la frase en palabras
# palabras_de_la_frase_español = frase_en_español.split(' ')

# # inicializar la frase y las palabras en ingles
# frase_en_ingles = ''
# palabra_en_ingles = ''

# # recorrer cada palabra de la frase en español
# for palabra_en_español in palabras_de_la_frase_español:
    
#     # si la palabra esta en el diccionario traducirla
#     if palabra_en_español in diccionario:
#         palabra_en_ingles = diccionario[palabra_en_español]
#     else:
#         # si no esta en el diccionario mantener la palabra tal como esta
#         palabra_en_ingles = palabra_en_español
    
#     # agregar la palabra traducida (o no traducida) a la frase en ingles
#     frase_en_ingles += palabra_en_ingles + ' '
    
# print(frase_en_ingles)    
    
    

# for español in traductor:
#     print(f'En español (clave): {español}')
#     print(f'En inglés (valor): {traductor[español]}')
    # for ingles in traductor:
        # print(ingles[español])
# falta.....
# solucion con ayuda de ai

# explicacion
# Usar un if en lugar de recorrer todo el diccionario 
# te simplifica mucho el programa.
# ¿Por qué es más sencillo?

#     Verificación directa: El if palabra_en_español in diccionario te permite 
#     verificar de manera sencilla si una palabra está en el diccionario. 
#     No necesitas recorrer cada elemento del diccionario con un bucle interno.

#     Eficiencia: Al usar in, el programa busca rápidamente 
#     si la palabra existe en el diccionario, 
#     lo cual es más eficiente que recorrer todo el diccionario manualmente.

#     Código más limpio: Al reducir el número de bucles anidados 
#     y condiciones, el código es más fácil de leer y entender.

# Es una excelente forma de simplificar y hacer que el código sea más directo.






# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes 
# de cobro de una empresa. Las facturas se almacenarán 
# en un diccionario donde la clave de cada factura será el número de factura 
# y el valor el coste de la factura. 
# El programa debe preguntar al usuario si quiere añadir 
# una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará 
# por el número de factura y su coste y se añadirá al diccionario. 
# Si se desea pagar una factura se preguntará por el número de factura 
# y se eliminará del diccionario. 
# Después de cada operación el programa debe mostrar por pantalla 
# la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

# import os

# def limpiar_consola():
#     # Comando para limpiar la consola según el sistema operativo
#     sistema = os.name
#     if sistema == 'posix':  # Para sistemas Unix (Linux, macOS)
#         os.system('clear')
#     else:  # Para sistemas Windows
#         os.system('cls')


# facturas_pendientes = {} #clave: nro_de_factura    valor: importe_de_la_factura
# nro_de_factura = 0
# importe_de_la_factura = 0.0
# cobrada = 0.00
# pendiente_de_cobro = 0.00

# # bucle infinito hasta que presione salir
# while True:
#     limpiar_consola()
#     pendiente_de_cobro = sum(facturas_pendientes.values())
    
#     print(f'La cantidad de facturas pendiente de cobro: ${pendiente_de_cobro}')
#     print(f'Las facturas pagadas: ${cobrada}')
    
#     print('Las facturas pendientes son:')
#     print(facturas_pendientes)
#     print()
#     print('ᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁ')
#     print('ᐅ Si desea agregar una nueva factura pendiente presione "A".        ᐊ')
#     print('ᐅ Si desea registrar el pago de una factura pendiente presione "P". ᐊ')
#     print('ᐅ Para salir del programa presione "S".                             ᐊ')
#     print('ᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃ')
#     abml = input('Ingrese una opción: ')

#     # paso a mayusculas la opcion
#     abml = abml.upper()

#     if abml == 'S':
#         limpiar_consola()
#         break
#     elif abml == 'A':
#         nro_de_factura = int(input('Ingrese el número de la factura: '))
#         importe_de_la_factura = float(input('Ingrese el importe de la factura: $'))
#         facturas_pendientes[nro_de_factura]=importe_de_la_factura
#     elif abml == 'P':
#         nro_de_factura = int(input('Ingrese el número de la factura: '))
#         if nro_de_factura in facturas_pendientes:
#             print(f'La factura {nro_de_factura} tiene un importe de ${facturas_pendientes[nro_de_factura]}')
#             print('Factura pagada, no está más en las facturas pendientes!')
#             cobrada += facturas_pendientes[nro_de_factura]
#             del facturas_pendientes[nro_de_factura]
#         else:
#             print(f'No se hayó la factura nro: {nro_de_factura}')
#     else:
#         print('Seleccione una opción correcta (A,P o S).')
    



# # Ejercicio 10
# # Escribir un programa que permita gestionar la base de datos 
# # de clientes de una empresa. Los clientes se guardarán en un 
# # diccionario en el que la clave de cada cliente será su DNI, 
# # y el valor será otro diccionario con los datos del 
# # cliente (nombre, dirección, teléfono, correo, preferente), 
# # donde preferente tendrá el valor True si se trata de 
# # un cliente preferente. El programa debe preguntar al 
# # usuario por una opción del siguiente menú: 
# # (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
# # (4) Listar todos los clientes, (5) Listar clientes preferentes, 
# # (6) Terminar. 
# # En función de la opción elegida el programa tendrá que hacer lo siguiente:

# # Preguntar los datos del cliente, crear un diccionario 
# # con los datos y añadirlo a la base de datos.
# # Preguntar por el DNI del cliente y eliminar sus datos de la base de datos.
# # Preguntar por el DNI del cliente y mostrar sus datos.
# # Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# # Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# # Terminar el programa.

# clientes = {
#     25000000: {
#         'nombre':'Patricio',
#         'domicilio_calle':'Francisco',
#         'domicilio_numero':600,
#         'ciudad':'Mar',
#         'telefono':'150000000',
#         'preferente':True
#     },
#     26000000: {
#         'nombre':'María',
#         'domicilio_calle':'Francisco',
#         'domicilio_numero':2588725,
#         'ciudad':'Mar',
#         'telefono':'150000000',
#         'preferente':True
#     }, 
#     27000000:{
#         'nombre':'Lucia',
#         'domicilio_calle':'Manuel',
#         'domicilio_numero':100,
#         'ciudad':'San',
#         'telefono':'1500000000',
#         'preferente':False
#     }
# }
# # muestra todo el diccionario
# # print(clientes)

# # muestra las claves del diccionario principal
# # print(clientes.keys())

# # muestra los valores del diccionario anidado a 25000000
# # print(clientes[25000000])

# # muestra los valores que tiene diccionario 25000000 una clave en particular
# # print(clientes[25000000]['nombre'])

# # modifico nombre y lo muestro
# # clientes[25000000]['nombre'] = 'Pepe'
# # print(clientes[25000000]['nombre'])

# # borro nombre del cliente
# # print(clientes[25000000])
# # del clientes[25000000]['nombre']
# # print(clientes[25000000])

# # agrego una nueva denominacion 'como le dicen'
# # clientes[25000000]['como le dicen'] = 'Javier'
# # print(clientes[25000000])


# # el programa debe estar en un bucle que siempre se ejecute
# while True:
#     print('ᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁᐁ')
#     print('ᐅ                   Diccionarios de los Clientes                    ᐊ')
#     print('ᐅ                                                                   ᐊ')
#     print('ᐅ        Seleccione una opción:                                     ᐊ')
#     print('ᐅ                        (1) Añadir un cliente                      ᐊ')
#     print('ᐅ                        (2) Eliminar un cliente                    ᐊ')
#     print('ᐅ                        (3) Mostrar un cliente                     ᐊ')
#     print('ᐅ                        (4) Listar todos los clientes              ᐊ')
#     print('ᐅ                        (5) Listar los clientes preferentes        ᐊ')
#     print('ᐅ                        (6) Terminar                               ᐊ')
#     print('ᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃᐃ')

# # manejo de excepciones con try - except ValueError
#     try:
#         opcion = int(input('Ingrese una opción: '))

#         if opcion == 1:
#             # print('Añadir un cliente')
#             nro_documento = int(input('Ingrese su Nro de D.N.I.: '))
#             # pregunto si el cliente existe
#             if nro_documento in clientes:
#                 print(f'Error el {nro_documento} ya se encuentra registrado.')
#             else:
#                 nombre = input('Ingrese su nombre completo como figura en su D.N.I.: ')
#                 domicilio_calle = input('Ingrese del domicilio el nombre de la calle: ')
#                 domicilio_numero = int(input('Ingrese del domcilio el número de la casa: '))
#                 ciudad = input('Ingrese el nombre de la ciudad de residencia: ')
#                 telefono = input('Ingrese el numero de telefono (cadena de caracteres): ')
#                 preferente_texto = input('¿Es cliente preferencial? (S/N): ')
#                 preferente_texto = preferente_texto.upper()
#                 # if preferente_texto == 'S':
#                 #     preferente_booleano = True
#                 # else:
#                 #     preferente_booleano = False
#                 # el bloque if se reemplaza con una sola linea que devuelve True o False
#                 preferente_booleano = preferente_texto == 'S'
        
#                 # agrego los datos de la variable al diccionario
#                 clientes[nro_documento] = {
#                     'nombre' : nombre,
#                     'domicilio_calle' : domicilio_calle,
#                     'domicilio_numero' : domicilio_numero,
#                     'ciudad' : ciudad,
#                     'telefono' : telefono,
#                     'preferente' : preferente_booleano                
#                 }
#                 print(f'Cliente con DNI: {nro_documento} fue agregado correctamente.')
            
#         elif opcion == 2:
#             # print('Eliminar un cliente')
#             nro_documento = int(input('Ingrese el Nro de D.N.I. que desea eliminar: '))
#             # pregunto si el cliente existe
#             if nro_documento in clientes:
#                 del clientes[nro_documento]
#             else:
#                 print(f'Error el {nro_documento} no se encuentra registrado.')
                
#         elif opcion == 3:
#             print('*****************************')
#             # print('Mostrar un cliente')
#             nro_documento = int(input('Ingrese el Nro de D.N.I. que desea mostrar: '))
#             if nro_documento in clientes:
#                 # si lo encontró cargo el cliente
#                 cliente = clientes[nro_documento]
#                 print('Exibir un Cliente')
#                 print(f'D.N.I.: {nro_documento}')
                
#                 # camino largo  
#                 # print(f'Nombre: {clientes[nro_documento]['nombre']}')
#                 # ......
                
#                 # camino corto
#                 # muestro datos de cliente = clientes[nro_documento]
#                 for clave, valor in cliente.items():
#                     print(f'{clave} : {valor}')
                
#             else:
#                 print(f'Error: No existe el cliente con DNI {nro_documento}.')
#             print('***************')
#         elif opcion == 4:
#             # print('Listar todos los clientes')
#             # Listar todos los clientes
#             print('Lista de todos los clientes:')
#             for dni, cliente in clientes.items():
#                 print(f'{dni} - {cliente["nombre"]}')
#         elif opcion == 5:
#             print('Listar los clientes preferentes')
#             for dni, cliente in clientes.items():
#                 # if cliente['preferente'] == True:
#                 if cliente['preferente']:  #igual que el anterior por defecto evalua True
#                     print(f'{dni} - {cliente["nombre"]}')
#         elif opcion == 6:
#             print('Terminar')
#             break
        
#     except ValueError:
#         print('Elija una opción numérica')


# Ejercicio 11
# El directorio de los clientes de una empresa 
# está organizado en una cadena de # texto como la de más abajo, 
# donde cada línea contiene la información 
# del nombre, email, teléfono, dni, y el descuento que se le aplica. 
# Las líneas se separan con el carácter de cambio de línea \n 
# y la primera línea contiene los nombres de los campos 
# con la información contenida en el directorio.

# "dni;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# Escribir un programa que genere un diccionario con la información del directorio, 
# donde cada elemento corresponda a un cliente 
# y tenga por clave su dni y por valor otro diccionario con el resto 
# de la información del cliente. 
# Los diccionarios con la información de cada cliente 
# tendrán como claves los nombres de los campos 
# y como valores la información de cada cliente correspondientes a los campos. 
# Es decir, un diccionario como el siguiente

# {'01234567L': 
# {'nombre': 'Luis González', 
# 'email': 'luisgonzalez@mail.com', 
# 'teléfono': '656343576', 
# 'descuento': 12.5
# }, 
# '71476342J': 
# {'nombre': 'Macarena Ramírez', 
# 'email': 'macarena@mail.com', 
# 'teléfono': '692839321', 
# 'descuento': 8.0
# }, 
# '63823376M': 
# {'nombre': 'Juan José Martínez', 
# 'email': 'juanjo@mail.com', 
# 'teléfono': '664888233', 
# 'descuento': 5.2}, 
# '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
clientes = {}
atributos = []
registros = []
datos_en_cadena = "dni;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# cada salto de linea creo un elemento que contendra el titulo y c/u de los registros
datos_en_lista = datos_en_cadena.split('\n')
# obtengo los atributos
atributos = datos_en_lista[0].split(';')
# print(atributos)
for index in range(0,len(datos_en_lista)):
    # print(datos_en_lista[index].split(';'))
    registros.append(datos_en_lista[index].split(';'))

print(registros)

# agrego a clientes
for index in range(1,len(datos_en_lista)):
    clientes[registros[index][0]] = {
        'nombre' : registros[index][1],
        'email' : registros[index][2],
        'telefono' : registros[index][3],
        'descuento' : registros[index][4]        
    }
    # print(index)

print(clientes)
