#  para ver el namespace de este modulo
# cuando es llamado por otro archivo
print(f'{__name__} de menu_principal.py')

# crear un menu al estilo
# con una funcion para centrar los titulos

def titulo(texto):
    # titulo = 'Menú Principal'
    lineaTexto = texto.center(60)
    print(lineaTexto.center(64,"*"))

def lineas_divisorias():
    print('*' * 64)

def presentacion_menu():
    lineas_divisorias()
    titulo("Menu")
    lineas_divisorias()
    titulo("1) Suma de a + b")
    titulo("2) Resta de a - b")
    titulo("3) Multiplicación de a * b")
    titulo("4) División de a / b")
    titulo("5) Módulo de a % b")
    titulo("0) Salir")
    lineas_divisorias()
    
    opcion = int(input("Ingrese una opción: "))
    if opcion != 0:
        a = int(input("Inserte el valor de 'a': "))
        b = int(input("Inserte el valor de 'b': "))
        return opcion, a, b
    else:
        return 0,0,0
