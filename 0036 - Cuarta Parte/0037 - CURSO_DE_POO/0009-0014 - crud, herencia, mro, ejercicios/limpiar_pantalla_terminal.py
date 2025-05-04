import os

def limpiar_pantalla():
    """Limpia la pantalla del terminal."""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux, macOS, etc.
        os.system('clear')
