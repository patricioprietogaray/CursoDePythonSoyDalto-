# crud version 2

# importar la libreria de los colores
from colorama import init, Fore, Back, Style
class Crud:
    def __init__(self, archivo, atributos):
        self.archivo = archivo
        self.atributos = atributos
    
    def crud_listado(self, clave='total', valor=0):
        print(f'ingreso clave: {clave} con su valor {valor}')
        if clave.lower() == 'total' and valor == 0:
            print('\n\nMostrar todos los datos de la base de datos!!!!\n\n')
    # def crud_buscar(self, id_a_buscar):
        






# para inicializar colorama
init()

archivo = 'crud.csv'
atributos = ['id','nombre','telefono']
instancia_crud = Crud(archivo,atributos)
ancho_de_linea = 60


while True:
    # es igual que print sin end, salta de linea
    # print(Fore.RED + "Texto en rojo", end="\n")
    
    # el proximo print esta en la misma linea
    # print(Fore.GREEN + "Texto en verde", end=" ")
    # print(Fore.BLUE + "Texto en azul")
    print(Fore.BLACK + Back.GREEN)    
    print(centrarEntre('Definición de la clase CRUD', ancho_de_linea))
    print(Fore.GREEN + Back.BLACK)
    print(centrarEntre('Ingrese el id para buscar en la base de datos.',ancho_de_linea))
    print(centrarEntre('Si existe se muestra el dato y luego se edita o borra el mismo.',ancho_de_linea))
    print(centrarEntre('si no existe se crea uno nuevo.',ancho_de_linea))
    print(centrarEntre('Para ver la base de datos ingrese el número cero',ancho_de_linea) + Style.RESET_ALL)
    opc_menu = int(input('Ingrese el número de id a buscar (0 para listar los datos, -1 para salir): '))
    if opc_menu == -1:
        break
    elif opc_menu == 0:
        opc = input('Ingrese la forma que quiere que los datos se muestren: (T)otal o (P)arcial: ')
        if opc.lower() == 't':
            instancia_crud.crud_listado()
        
        
        
        
        
        # atrib = input('Ingrese el atributo (clave) que utlizará para realizar la búsqueda: ')
        # valor = input('Ingrese el valor que tendrá el atributo {atrib}: ')
        # instancia_crud.crud_listado(atrib,valor)
        
        
        
    
