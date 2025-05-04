from clase_menu import Menu
from clase_listado import Listados

from colorama import Fore, Back, Style

longitud_de_linea = 45
menu_principal = Menu(longitud_de_linea)
dibujar_linea_centrada = menu_principal.centrar_texto('',longitud_de_linea,'-')
# titulito = menu_principal.texto_a_color('123456789-12345678901234567890CRUD: Create Read Update Delete12345678901234567890-123456789',Fore.LIGHTGREEN_EX,Back.RESET,Style.BRIGHT)
titulo_centrado = menu_principal.centrar_texto('CRUD: Create Read Update Delete',longitud_de_linea)
# titulito = menu_principal.texto_a_color('CRUD: Create Read Update Delete',Fore.LIGHTGREEN_EX,Back.RESET,Style.BRIGHT)
explicaciones = ['Muchas gracias por elegirnos','Ingrese el número de id para buscarlo en la base de datos','Si existe se muestra el dato y luego se edita o borra el mismo','si no existe se crea uno nuevo','Para listar la base de datos presione el numero cero']
mensaje_ingreso_opcion = menu_principal.texto_a_color('Ingrese el número de id a buscar (0 para listar los datos, -1 para salir): ', Fore.WHITE, Back.RESET, Style.BRIGHT)
db_csv = 'base_de_datos.csv'
atributos_crud = ['id','nombre']

lista = Listados(db_csv, atributos_crud)
lista.cargar_csv()

# # bucle para mostrar el menu
# while True:
#     print(menu_principal.texto_a_color(dibujar_linea_centrada,Fore.GREEN,Back.RESET,Style.BRIGHT))
#     print(titulo_centrado)
#     print(menu_principal.texto_a_color(dibujar_linea_centrada,Fore.GREEN,Back.RESET,Style.BRIGHT))

#     for texto in explicaciones:
#         textito = menu_principal.centrar_texto(texto,longitud_de_linea)
#         formato = menu_principal.texto_a_color(textito, Fore.LIGHTMAGENTA_EX, Back.RESET, Style.NORMAL)
#         print(formato)
    
#     print(menu_principal.texto_a_color(dibujar_linea_centrada,Fore.GREEN,Back.RESET,Style.BRIGHT))
    
#     # manejo de excepcion para evitar errores, como convierte a numero de "123" a 123 esta ok, 
#     # pero si quiero convertir otra cosa que no sea numero "hola" lanza la excepcion
#     try:
#         opc_menu = int(input(mensaje_ingreso_opcion))
#     except ValueError:
#         input('Debe ingresar un numero, presione una tecla para continuar...')
#         continue


#     if opc_menu == -1:
#         break
#     elif opc_menu == 0:
#         print('selecciono cero')
#         clase_listado = Listados(db_csv,atributos_crud)
#         clase_listado.cargar_csv()
#         clase_listado.mostrar_listado()
#         # listadito = Listados(db_csv,True,False)
#         # listadito.mostrar_listado()
#         # opc = input('Ingrese la forma que quiere que los datos se muestren: (T)otal o (P)arcial: ')
#         # if opc.lower() == 't':
#             # instancia_crud.crud_listado()

