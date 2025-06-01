# personajes de un juego
# mago, caballero, rey, curandero, bufon
# todos los personajes tienen nombre, habilidad y salud
# infringen daño y reciben daño de otro jugador
# si la salud llega a cero se muere
# el curandero puede curar a otro jugador y este recupera la salud
# el curandero puede recibir daño (defensa) y puede dañar (ataque) igual que el resto
# de los personajes

from random import *


class Personaje:
    # constructor
    def __init__(self, nombPers, salud = 100, vidas = 3):
        self.__nombre_personaje = nombPers
        self.__salud = salud
        self.__vidas = vidas
        # llamar al metodo para que incie el juego
        self.iniciar_el_juego
    
    def iniciar_el_juego(self):
        print(f'''
        HA INICIADO EL JUEGO!!!!!
        TU PERSONAJE ES: {self.__nombre_personaje}
        TIENES {self.__vidas} VIDAS POR JUGAR,
        SALUD {self.__salud}%.
        BUENA SUERTE Y...
        QUE COMIENCE EL JUEGO
    ''')

class Arma:
    def __init__(self, nombrArma, infrDaño = 0):
        self.__nombre_arma = nombrArma
        self.__infringe_daño = infrDaño
    





# terminal
print('Primer personaje')
nombre1 = input('Personaje 1 --> Ingrese el nombre del personaje: ')
arma1 = input(f'Ingrese el arma que utilizará {nombre1} como ataque: ')
daño1 = int(input(f'Ingrese el daño que el arma {arma1} le hará a su contrincante: '))
salud1 = 100
vidas1 = int(input(f'Ingrese la cantidad de vidas que tendra el personaje {nombre1}: '))

personaje1 = Personaje(nombre1, salud1, vidas1)
personaje1.iniciar_el_juego()
arma1 = Arma(arma1, daño1)

print(f'Ver los atributos y metodos públicos con DIR: {dir(Personaje)}')
print(f'Ver los atributos y metodos públicos con DIR: {dir(Arma)}')









# class Personaje:
#     # constructor
#     def __init__(self, nombre_personaje, salud = 100, vidas = 3):
#         self.__nombre_personaje = nombre_personaje
#         self.__salud = salud
#         self.__vidas = vidas
        
#         # llamar al iniciar el juego
#         self.iniciar_el_juego()
    
#     # metodos
    
#     def iniciar_el_juego(self):
#         print(f'''
#         HA INICIADO EL JUEGO!!!!!
#         TU PERSONAJE ES: {self.__nombre_personaje}
#         TIENES {self.__vidas} VIDAS POR JUGAR
#         BUENA SUERTE Y...
#         QUE COMIENCE EL JUEGO
#     ''')
    
#     def recibe_daño(self, porcentaje_daño = 0):
#         self.porcentaje_daño = porcentaje_daño
#         self.salud -= self.porcentaje_daño
#         if self.salud < 0:
#             self.salud = 100
#             self.vidas -= 1
            
#         if self.porcentaje_daño > 0:
#             return f'{self.nombre_personaje} lo han atacado ({self.porcentaje_daño}% de daño) y ahora tiene {self.salud}% de salud.'
#         else:
#             return f'{self.nombre_personaje} lo han atacado y ha muerto.'
    
#     # setters getters
#     def set_nombre(self, nombre_personaje):
#         self.__nombre_personaje = nombre_personaje
        

# class Arma:
#     def __init__(self, nombre_arma, infringe_daño = 0):
#         self.nombre_arma = nombre_arma
#         self.infringe_daño = infringe_daño
    
#     def hace_daño(self):
#         return self.infringe_daño
    
# class PersonajeArmado(Personaje, Arma):
#     # se debe instanciar de lo contrario con    pass   solo se instancia personaje
#     def __init__(self, nombre_personaje, nombre_arma, salud=100, vidas=3, infringe_daño = 0):
#         Personaje.__init__(self, nombre_personaje, salud, vidas)
#         Arma.__init__(self, nombre_arma, infringe_daño)

# #     def ataque(self, personaje_atacado):
# #         self.personaje_atacado = personaje_atacado
# #         self.salud -= self.infringe_daño
# #         if self.salud <= 0:
# #             return f'Ha muerto {self.personaje_atacado}.'
# #         return f'El personaje atacado es: {self.personaje_atacado} y le queda {self.salud}% de salud.'
        

# # class Pelea:
# #     def __init__(self, personaje1, personaje2):
# #         self.personaje1 = personaje1
# #         self.personaje2 = personaje2
        
# #     def batalla(self):
# #         while True:
# #             if self.personaje1.salud != 0 or self.personaje2.salud !=0:
# #                 eleccion = randint(0,1)
# #                 if eleccion:
# #                     respuesta = self.personaje1.ataque(self.personaje2.nombre_personaje)
# #                     print(f'{self.personaje1.nombre_personaje} ataca a {self.personaje2.nombre_personaje}: \n{respuesta}')
# #                 else:
# #                     respuesta = self.personaje2.ataque(self.personaje1.nombre_personaje)
# #                     print(f'{self.personaje2.nombre_personaje} ataca a {self.personaje1.nombre_personaje}: \n{respuesta}')
        
# #                 if respuesta[0:9] == 'Ha muerto':
# #                     break
# #                 # print(respuesta[:8])
# #                 # input()                
    
# # jugador1 = Personaje('Merlin')
# # jugador2 = Personaje('Arturo')
# # cuchillo = Arma('Cuchillo', 25)
# # espada = Arma('Espada',35)

# # merlin_bacula = PersonajeArmado('Merlin','Bácula',100,1,15)
# # arturo_espada = PersonajeArmado('Arturo','Espada',100,3,10)
# # pelea_merlin_arturo = Pelea(merlin_bacula, arturo_espada)
# # shrek_grita = PersonajeArmado('Shrek','Grito',100,3,15)
# # pelea_arturo_shrek = Pelea(arturo_espada, shrek_grita)

# print('Primer personaje')
# nombre1 = input('Personaje 1 --> Ingrese el nombre del personaje: ')
# arma1 = input(f'Ingrese el arma que utilizará {nombre1} como ataque: ')
# daño1 = int(input(f'Ingrese el daño que el arma {arma1} le hará a su contrincante: '))
# salud1 = 100
# vidas1 = int(input(f'Ingrese la cantidad de vidas que tendra el personaje {nombre1}: '))

# print('Segundo personaje')
# nombre2 = input('Personaje 2 --> Ingrese el nombre del personaje: ')
# arma2 = input(f'Ingrese el arma que utilizará {nombre2} como ataque: ')
# daño2 = int(input(f'Ingrese el daño que el arma {arma2} le hará a su contrincante: '))
# salud2 = 100
# vidas2 = int(input(f'Ingrese la cantidad de vidas que tendra el personaje {nombre2}: '))

# personaje1 = PersonajeArmado(nombre1, arma1, salud1, vidas1, daño1)
# personaje2 = PersonajeArmado(nombre2, arma2, salud2, vidas2, daño2)

# input('Enter para continuar....')





# print(f'Nombre del personaje1: {merlin_bacula.nombre_personaje}')
# print(f'Arma del personaje: {merlin_bacula.nombre_arma}')

# print('Arturo')
# print(f'Nombre del personaje: {arturo_espada.nombre_personaje}')
# print(f'Arma del personaje: {arturo_espada.nombre_arma}')
# print()
# print('\nQue comience la batalla!!!!\n')
# input()
# # if merlin_bacula.salud > 0 and arturo_espada.salud > 0:
#     # pelea()
    

# pelea_merlin_arturo.batalla()

# print(f'¿PersonajeArmado es sublcase de Pelea?: {issubclass(PersonajeArmado, Pelea)}')
# print(f'¿Pelea es sublcase de PersonajeArmado?: {issubclass(PersonajeArmado, Pelea)}')
# print(f'¿PersonajeArmado es sublcase de Personaje?: {issubclass(PersonajeArmado, Personaje)}')
# print(f'¿PersonajeArmado es sublcase de Arma?: {issubclass(PersonajeArmado, Arma)}')
# print(f'¿PersonajeArmado es un instancia de Personaje?:{isinstance(PersonajeArmado, Personaje)}')
# print(f'¿pelea_merlin_arturo es una intancia de Personaje?:{isinstance(pelea_merlin_arturo, Personaje)}')
# print(f'¿pelea_merlin_arturo es una intancia de PersonajeArmado?:{isinstance(pelea_merlin_arturo, PersonajeArmado)}')
# print(f'¿pelea_merlin_arturo es una intancia de Pelea?:{isinstance(pelea_merlin_arturo, Pelea)}')
# # ver 0:50

# pelea_arturo_shrek.batalla()
# arturo_espada.salud = 10




