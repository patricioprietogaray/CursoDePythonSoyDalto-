# Ejercicio de Herencia Múltiple (Sin Resolver): Dispositivo Híbrido

# 1. Define una clase llamada ReproductorMP3 con los siguientes atributos:
#    - capacidad (int) - en GB
#    - canciones_reproducidas (list) - lista de nombres de canciones
#    - Un método 'reproducir_cancion(cancion)' que agregue la canción a la lista de reproducidas e imprima un mensaje.

class ReproductorMP3:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.canciones_reproducidas = []
    
    def reproducir_cancion(self, cancion):
        self.canciones_reproducidas.append(cancion)
        print(f'Reproduciendo: {cancion}')
    

# 2. Define una clase llamada CamaraFotografica con los siguientes atributos:
#    - megapixeles (float)
#    - fotos_tomadas (int)
#    - Un método 'tomar_foto()' que incremente el contador de fotos tomadas e imprima un mensaje.

class CamaraFotográfica:
    def __init__(self, megapixeles):
        self.megapixeles = megapixeles
        self.fotos_tomadas = 0    # interno para usar con el método
        
    def tomar_foto(self):
        self.fotos_tomadas += 1
        print(f'Se ha tomado una nueva foto! (Ya se sacaron {self.fotos_tomadas} fotos, con {self.megapixeles} megapixeles.)')


# 3. Define una clase llamada GrabadoraDeVoz con los siguientes atributos:
#    - tiempo_maximo_grabacion (int) - en minutos
#    - grabaciones_realizadas (int)
#    - Un método 'grabar_audio(tiempo)' que incremente el contador de grabaciones e imprima un mensaje sobre el tiempo grabado.

class GrabadoraDeVoz:
    def __init__(self, tiempo_maximo_grabacion):
        self.tiempo_maximo_grabacion = tiempo_maximo_grabacion
        self.grabaciones_realizadas = 0
    
    def grabar_audio(self, tiempo):
        self.grabaciones_realizadas += 1
        print(f'El tiempo de grabación es {self.tiempo_maximo_grabacion} minutos, con un total de graciones realizadas de {self.grabaciones_realizadas}.')


# 4. Define una clase llamada DispositivoHibrido que herede de las tres clases anteriores:
#    ReproductorMP3, CamaraFotografica y GrabadoraDeVoz.
#    - Su constructor debe recibir argumentos para inicializar los atributos de todas las clases padre.
#    - Debe tener un método 'mostrar_funcionalidades()' que imprima un mensaje listando las funcionalidades del dispositivo.
#    - Debe tener un método 'realizar_accion(accion, *args)' que permita al usuario realizar una acción
#      (reproducir, tomar foto, grabar) pasando los argumentos necesarios a los métodos correspondientes.

class DispositivoHibrido(ReproductorMP3, CamaraFotográfica, GrabadoraDeVoz):
    def __init__(self, capacidad, megapixeles, tiempo_maximo_grabacion):
        ReproductorMP3.__init__(self, capacidad)
        CamaraFotográfica.__init__(self, megapixeles)
        GrabadoraDeVoz.__init__(self, tiempo_maximo_grabacion)
        
    def mostrar_funcionalidades(self):
        print("Este dispositivo híbrido puede:")
        print("- Reproducir música.")
        print("- Tomar fotografías.")
        print("- Grabar audio.")
        
    def realizar_accion(self, accion, *args):
        if accion == 'reproducir':
            cancion = 'De musica ligera'
            self.reproducir_cancion(cancion)
        elif accion == 'foto':
            self.tomar_foto()
        elif accion == 'grabar':
            self.grabar_audio(args)
        else:
            print('Acción no válida')

# 5. Crea una instancia de la clase DispositivoHibrido y prueba sus funcionalidades.

mi = DispositivoHibrido(5,10,500)
mi.mostrar_funcionalidades()
mi.realizar_accion('reproducir','De musica ligera',"Bohemian Rhapsody")
mi.realizar_accion('foto')
mi.realizar_accion('foto')
mi.realizar_accion('grabar',5)
mi.realizar_accion('grabar',5)
mi.realizar_accion('otra cosa')
print()
mi_dispositivo = DispositivoHibrido(5,10.0,500)
mi_dispositivo.mostrar_funcionalidades()
mi_dispositivo.realizar_accion("reproducir", "Bohemian Rhapsody")
mi_dispositivo.realizar_accion("foto")
mi_dispositivo.realizar_accion("grabar", 5)
mi_dispositivo.realizar_accion("otra_cosa")


# Tu tarea es:

# Completar el constructor (__init__) de la clase DispositivoHibrido. 

# Deberás llamar a los constructores de ReproductorMP3, CamaraFotografica y GrabadoraDeVoz 
# utilizando la forma adecuada para la herencia múltiple, 
# pasando los argumentos necesarios para inicializar sus atributos.

# Completar el método realizar_accion() de la clase DispositivoHibrido. 
# Deberás implementar la lógica para llamar al método correcto de la clase padre 
# según la accion proporcionada por el usuario, 
# pasando los argumentos adicionales (*args) a ese método.

# Crear una instancia de DispositivoHibrido con valores de ejemplo para sus atributos.
# ¡Este ejercicio te permitirá practicar la inicialización en herencia múltiple y cómo acceder a los métodos de las diferentes clases padre a través de la clase hija! ¡Mucha suerte! ¡Estoy aquí para ayudarte cuando tengas tu intento!