import os
import subprocess
import time


# OS
def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    limpiar_pantalla()  # Opcional: Limpia la pantalla si se ejecuta este archivo directamente
    print("Pantalla limpiada (si funcionó). Este archivo está diseñado para ser importado.")



# Ejercicio 4: Multimedia, Audio y Video (Complejo)

# Define una clase base llamada Multimedia con atributos como titulo, formato y duracion, 
# y un método para reproducir() que imprima un mensaje genérico de reproducción. 
# Luego, crea dos clases hijas: Audio con un atributo adicional calidad (ej: "mp3", "wav") 
# y un método reproducir() que imprima un mensaje específico para audio, incluyendo la calidad. 
# La segunda clase hija es Video con atributos adicionales como resolucion (ej: "720p", "1080p") 
# y un método reproducir() que imprima un mensaje específico para video, incluyendo la resolución. 
# Considera la posibilidad de agregar un 
# método adicional a Video como pausar() o a Audio como subir_volumen(). Utiliza super() para la inicialización 
# y piensa en cómo especializar el comportamiento en las clases hijas.





# Define una clase base llamada Multimedia con atributos como titulo, formato y duracion, 
# y un método para reproducir() que imprima un mensaje genérico de reproducción.
class Multimedia:
    def __init__(self, titulo, formato, duracion):
        self.titulo = titulo
        self.formato = formato
        self.duracion = duracion
    
    def reproducir_texto(self):
        return f'''Se reproduce el archivo multimedia: 
              Titulo:   {self.titulo}
              Formato:  {self.formato}
              Duración: {self.duracion}
              '''

    def pausa_texto(self):
        return f'Se pone en pausa el archivo multimedia: Titulo: {self.titulo}.'
    
    def para_texto(self):
        return f'Se detiene de forma permanente la reproducción: Titulo {self.titulo}.'

    
    # def reproducir_mp3(self, archivo_mp3):
    #     # usamos una lista para el comando
    #     comando = ['vlc', '--play-and-exit', archivo_mp3]
        
    #     try:
    #         with open(os.devnull, 'w') as devnull:  # Abrir /dev/null o NUL
    #             proceso_separado_vlc = subprocess.Popen(comando, stdout=devnull, stderr=devnull)

    #         # mezcla la salida del vlc con la de nuestra aplicacion. 
    #         # ejecutar vlc en un proceso separado
    #         # proceso_separado_vlc = subprocess.Popen(comando)

    #     except FileNotFoundError:
    #         print('El reproductor vlc no se encontró, asegúrate que este instalado')
    #     except Exception as e:
    #         print(f'Ocurrió un error al reproducir el archivo {e}')
        

        


# Luego, crea dos clases hijas: Audio con un atributo adicional calidad (ej: "mp3", "wav") 
# y un método reproducir() que imprima un mensaje específico para audio, incluyendo la calidad. 
# Considera la posibilidad de agregar un 
# método adicional a Video como pausar(). Utiliza super() para la inicialización 
# y piensa en cómo especializar el comportamiento en las clases hijas.

class Audio(Multimedia):
    def __init__(self, titulo, formato, duracion, calidad):
        super().__init__(titulo, formato, duracion)
        self.calidad = calidad
        
    def reproducir(self):
        return f'Reproduciendo {self.titulo} cuya calidad es {self.calidad}.'




# Luego, crea dos clases hijas: 
# La segunda clase hija es Video con atributos adicionales como resolucion (ej: "720p", "1080p") 
# y un método reproducir() que imprima un mensaje específico para video, incluyendo la resolución. 
# Considera la posibilidad de agregar un 
# método adicional a Audio como subir_volumen(). Utiliza super() para la inicialización 
# y piensa en cómo especializar el comportamiento en las clases hijas.

class Video(Multimedia):
    def __init__(self, titulo, formato, duracion, resolucion):
        super().__init__(titulo, formato, duracion)
        self.resolucion = resolucion

    def reproducir(self):
        return f'Se reproduce el video {self.titulo} con una resolucion de {self.resolucion}'

# aplicacion
limpiar_pantalla()
print(f'\nAplicación multimedia \n')
print('Clase Multimedia\n')
# multimedia = Multimedia('Angel Eléctrico', 'mp3', '2:15')
# multimedia.reproducir_texto()
# multimedia.reproducir_mp3('angelElectrico.mp3')
# multimedia.reproducir_texto()
print('Clase Audio')
aud = Audio('Angel Eléctrico','ArchivoMp3','3:50','MP3')
print(aud.reproducir())
# aud.reproducir_mp3('angelElectrico.mp3')
print(aud.reproducir_texto())
# a = int(input('un numero: '))
# b = int(input('otro numero'))
# print(a+b)
print(aud.pausa_texto())
print(aud.reproducir_texto())
print(aud.para_texto())
print('Clase Video')
vid = Video('Disco Eterno','mp4','3:25','640px x 320px')
print(vid.reproducir())
print(vid.reproducir_texto())
print(vid.pausa_texto())
print(vid.para_texto())


print(f'MRO de Video: {Video.mro()}')