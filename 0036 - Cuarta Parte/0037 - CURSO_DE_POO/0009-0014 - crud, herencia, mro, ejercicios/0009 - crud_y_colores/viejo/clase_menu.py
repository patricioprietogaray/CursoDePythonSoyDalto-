from colorama import init, Fore, Back, Style


class Menu:
    def __init__(self, longitud_de_la_linea):
        self.longitud_de_la_linea = longitud_de_la_linea
    
    def texto_a_color(self, texto_titulo, color_letra, color_fondo, estilo):
        self.texto_titulo = texto_titulo
        self.color_letra = color_letra
        self.color_fondo = color_fondo
        self.estilo = estilo
        texto_salida = color_letra + color_fondo + estilo + texto_titulo
        return texto_salida

    def centrar_texto(self, texto, longitud, caracter = ' '):
        longitud_texto = len(texto)
        espacios = longitud - longitud_texto // 2
        resutlado = caracter * espacios + texto + caracter * espacios
        if longitud % 2 == 0 and longitud_texto % 2 == 0:
            resutlado += caracter
        return resutlado
# fin de la clase

init()