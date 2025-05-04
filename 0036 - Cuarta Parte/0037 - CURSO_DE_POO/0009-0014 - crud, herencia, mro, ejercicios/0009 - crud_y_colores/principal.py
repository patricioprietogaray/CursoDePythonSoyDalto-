# módulo principal
# por este archivo (00_principal.py) se iniciará el programa

from colorama import Fore, Back, Style, init

# from archivo import clase
from info_pantalla import Info_pantalla

longitud_total = 65

formato_titulo = Info_pantalla(
    'CRUD: Create Read Update Delete', 
    Fore.RED, 
    Back.RESET, 
    Style.BRIGHT, 
    longitud_total, 
    '', 
    True, 
    True )
letra_titulo = formato_titulo.imprimir_por_pantalla()
print(formato_titulo.centrar_texto())
print(letra_titulo)





init()

print()