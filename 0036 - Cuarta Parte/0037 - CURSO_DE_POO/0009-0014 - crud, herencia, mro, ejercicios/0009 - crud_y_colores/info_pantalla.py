# este modulo contiene una clase que devolverá los colores
# mostrará por pantalla un menu prinicipal
# mostrará el texto a color
# centrará el texto
# presentará la información

from colorama import Fore, Back, Style, init

class Info_pantalla:
    def __init__(self, texto_a_imprimir, colorFuente, colorFondo, estilo, longitud_total, caracter_relleno = ' ', bool_color = True, bool_centrado = True):
        self.texto_a_imprimir = texto_a_imprimir
        self.colorFuente = colorFuente
        self.colorFondo = colorFondo
        self.estilo = estilo
        self.longitud_texto = len(self.texto_a_imprimir)
        self.longitud_total = longitud_total
        self.caracter_relleno = caracter_relleno
        self.bool_color = bool_color
        self.bool_centrado = bool_centrado
    
    def imprimir_por_pantalla(self):
        if self.bool_color and self.bool_centrado:
            texto = self.centrar_texto_a_color(self.texto_a_color())
            return texto
    
    def texto_a_color(self):
        return self.colorFuente + self.colorFondo + self.estilo + self.texto_a_imprimir
    
    def centrar_texto(self):
        self.longitud_texto = len(self.texto_a_imprimir)
        espacios = self.longitud_total - self.longitud_texto // 2
        # / /    devuelve un entero
        return self.caracter_relleno * espacios + self.texto_a_imprimir + self.caracter_relleno * espacios
        
    def centrar_texto_a_color(self, texto_a_color):
        self.longitud_texto = len(texto_a_color)
        espacios = self.longitud_total - self.longitud_texto // 2    
        # / /    devuelve un entero
        return self.caracter_relleno * espacios + texto_a_color + self.caracter_relleno * espacios
    
    
    
    def presentacion_menu_principal(self):
        pass
    
    init()
    