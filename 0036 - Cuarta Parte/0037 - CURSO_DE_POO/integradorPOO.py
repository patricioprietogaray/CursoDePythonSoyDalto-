# # personajes de un juego
# # mago, caballero, rey, curandero, bufon
# # todos los personajes tienen nombre, habilidad y salud
# # infringen daño y reciben daño de otro jugador
# # si la salud llega a cero se muere
# # el curandero puede curar a otro jugador y este recupera la salud
# # el curandero puede recibir daño (defensa) y puede dañar (ataque) igual que el resto
# # de los personajes

# from random import *

# class Personaje:
#     # constructor
#     def __init__(self, nombPers, salud = 100, vidas = 3):
#         self.__nombre_personaje = nombPers
#         self.__salud = salud
#         self.__vidas = vidas
#         # llamar al metodo para que incie el juego
#         self.iniciar_el_juego()
    
#     def iniciar_el_juego(self):
#         print(f'''
#         HA INICIADO EL JUEGO!!!!!
#         TU PERSONAJE ES: {self.__nombre_personaje}
#         TIENES {self.__vidas} VIDAS POR JUGAR,
#         SALUD {self.__salud}%.
#         BUENA SUERTE Y...
#         QUE COMIENCE EL JUEGO
#     ''')
        
#     def __recibe_daño(self, porcentaje_daño = 0):
#         self.__porcentaje_daño = porcentaje_daño
#         self.__salud -= self.__porcentaje_daño
#         if self.__salud < 0:
#             self.__vidas -= 1
#             self.__salud = 100
        
#         if self.__porcentaje_daño > 0:
#             return f'{self.__nombre_personaje} lo han atacado ({self.__porcentaje_daño}% de daño) y ahora tiene {self.__salud}% de salud.'
#         else:
#             return f'{self.__nombre_personaje} lo han atacado y ha muerto.'

#     def get_salud(self):
#         return self.__salud
    
#     def get_nombre_personaje(self):
#         return self.__nombre_personaje
    
    
# class Arma:
#     def __init__(self, nombrArma, infrDaño = 0):
#         self.__nombre_arma = nombrArma
#         self.__infringe_daño = infrDaño
    
#     def hace_daño(self):
#         return self.__infringe_daño


# class PersonajeArmado(Personaje, Arma):
#     def __init__(self, nombPers, nombrArma, salud = 100, vidas = 3, infrDaño = 0):
#         Personaje.__init__(self, nombPers, salud, vidas)
#         Arma.__init__(self, nombrArma, infrDaño)
        
#     def ataque(self, personaje_atacado):
#         self.__personaje_atacado = personaje_atacado
#         self.__salud -= self.__infringe_daño
#         if self.__salud <= 0:
#             return f'Ha muerto {self.__personaje_atacado}.'
#         return f'El personaje atacado es: {self.__personaje_atacado} y le queda {self.__salud}% de salud.' 

# class Pelea:
#     def __init__(self, personaje1, personaje2):
#         self.__personaje1 = personaje1
#         self.__personaje2 = personaje2
        
#     def batalla(self):
#         while True:
#             if self.__personaje1.get_salud() > 0 or self.__personaje2.get_salud() > 0:
#                 eleccion = randint(0,1)
#                 if eleccion == 0:
#                     respuesta = self.__personaje1.ataque(self.__personaje2.get_nombre_personaje())
#                     print(f'{self.__personaje1.get_nombre_personaje()} ataca a {self.__personaje2.get_nombre_personaje()}: \n{respuesta}')
#                 else:
#                     respuesta = self.__personaje2.ataque(self.__personaje1.get_nombre_personaje())
#                     print(f'{self.__personaje2.get_nombre_personaje()} ataca a {self.__personaje1.get_nombre_personaje()}: \n{respuesta}')
                
#                 if respuesta[0:9] == 'Ha muerto':
#                     break
#                 else:
#                     print('La batalla ha terminado!')
#                     break
                
# # terminal
# print('Primer personaje')
# nombre1 = input('Personaje 1 --> Ingrese el nombre del personaje: ')
# arma1 = input(f'Ingrese el arma que utilizará {nombre1} como ataque: ')
# daño1 = int(input(f'Ingrese el daño que el arma {arma1} le hará a su contrincante: '))
# salud1 = 100
# vidas1 = int(input(f'Ingrese la cantidad de vidas que tendra el personaje {nombre1}: '))

# personaje1 = PersonajeArmado(nombre1, arma1, salud1, vidas1, daño1)
# personaje1.iniciar_el_juego()

# print('Segundo personaje')
# nombre2 = input('Personaje 2 --> Ingrese el nombre del personaje: ')
# arma2 = input(f'Ingrese el arma que utilizará {nombre2} como ataque: ')
# daño2 = int(input(f'Ingrese el daño que el arma {arma2} le hará a su contrincante: '))
# salud2 = 100
# vidas2 = int(input(f'Ingrese la cantidad de vidas que tendra el personaje {nombre2}: '))


# personaje2 = PersonajeArmado(nombre2, arma2, salud2, vidas2, daño2)
# personaje2.iniciar_el_juego()
# input('Presione la tecla Enter para continuar.....')

# if personaje1.get_salud() > 0 and personaje2.get_salud() > 0:
#     pelea = Pelea(personaje1, personaje2)
#     pelea.batalla()




# # print(f'Personaje ---> Ver los atributos y metodos públicos con DIR: {dir(Personaje)}')
# # print(f'Arma ---> Ver los atributos y metodos públicos con DIR: {dir(Arma)}')
# # print(f'PersonajeArmado ---> Ver los atributos y metodos públicos con DIR: {dir(PersonajeArmado)}')








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


# from random import *

# class Personaje:
#     # constructor
#     def __init__(self, nombPers, salud = 100, vidas = 3):
#         self.__nombre_personaje = nombPers
#         self.__salud = salud
#         self.__vidas = vidas
#         # llamar al metodo para que incie el juego
#         self.iniciar_el_juego()

#     def iniciar_el_juego(self):
#         print(f'''
#         HA INICIADO EL JUEGO!!!!!
#         TU PERSONAJE ES: {self.__nombre_personaje}
#         TIENES {self.__vidas} VIDAS POR JUGAR,
#         SALUD {self.__salud}%.
#         BUENA SUERTE Y...
#         QUE COMIENCE EL JUEGO
#     ''')

#     def recibir_ataque(self, daño):
#         self.__salud -= daño
#         if self.__salud < 0:
#             self.__vidas -= 1
#             self.__salud = 100
#         return f'{self.__nombre_personaje} ha recibido {daño}% de daño y ahora tiene {self.__salud}% de salud y {self.__vidas} vidas.'

#     def get_salud(self):
#         return self.__salud

#     def get_nombre_personaje(self):
#         return self.__nombre_personaje


# class Arma:
#     def __init__(self, nombrArma, infrDaño = 0):
#         self.__nombre_arma = nombrArma
#         self.__infringe_daño = infrDaño

#     def hace_daño(self):
#         return self.__infringe_daño


# class PersonajeArmado(Personaje, Arma):
#     def __init__(self, nombPers, nombrArma, salud = 100, vidas = 3, infrDaño = 0):
#         Personaje.__init__(self, nombPers, salud, vidas)
#         Arma.__init__(self, nombrArma, infrDaño)

#     def ataque(self, nombre_personaje_atacado, personaje_atacado_objeto): # Recibimos el objeto Personaje
#         self.__personaje_atacado_nombre = nombre_personaje_atacado
#         daño_infringido = self.hace_daño() # Usamos el método para obtener el daño del arma
#         resultado_ataque = personaje_atacado_objeto.recibir_ataque(daño_infringido)
#         if personaje_atacado_objeto.get_salud() <= 0:
#             return f'Ha muerto {nombre_personaje_atacado}.'
#         return f'El personaje atacado es: {nombre_personaje_atacado} y ahora tiene {personaje_atacado_objeto.get_salud()}% de salud; tiene {Personaje._Personaje__vidas} vidas.'


# class Pelea:
#     def __init__(self, personaje1, personaje2):
#         self.__personaje1 = personaje1
#         self.__personaje2 = personaje2

#     def batalla(self):
#         while self.__personaje1.get_salud() > 0 and self.__personaje2.get_salud() > 0:
#             eleccion = randint(0,1)
#             if eleccion == 0:
#                 respuesta = self.__personaje1.ataque(self.__personaje2.get_nombre_personaje(), self.__personaje2)
#                 print(f'{self.__personaje1.get_nombre_personaje()} ataca a {self.__personaje2.get_nombre_personaje()}: \n{respuesta}')
#             else:
#                 respuesta = self.__personaje2.ataque(self.__personaje1.get_nombre_personaje(), self.__personaje1)
#                 print(f'{self.__personaje2.get_nombre_personaje()} ataca a {self.__personaje1.get_nombre_personaje()}: \n{respuesta}')

#             if respuesta[0:9] == 'Ha muerto':
#                 break
#         else:
#             print("¡La batalla ha terminado!")

# # terminal
# print('Primer personaje')
# nombre1 = input('Personaje 1 --> Ingrese el nombre del personaje: ')
# arma1 = input(f'Ingrese el arma que utilizará {nombre1} como ataque: ')
# daño1 = int(input(f'Ingrese el daño que el arma {arma1} le hará a su contrincante: '))
# salud1 = 100
# vidas1 = int(input(f'Ingrese la cantidad de vidas que tendra el personaje {nombre1}: '))

# personaje1 = PersonajeArmado(nombre1, arma1, salud1, vidas1, daño1)
# personaje1.iniciar_el_juego()

# print('Segundo personaje')
# nombre2 = input('Personaje 2 --> Ingrese el nombre del personaje: ')
# arma2 = input(f'Ingrese el arma que utilizará {nombre2} como ataque: ')
# daño2 = int(input(f'Ingrese el daño que el arma {arma2} le hará a su contrincante: '))
# salud2 = 100
# vidas2 = int(input(f'Ingrese la cantidad de vidas que tendra el personaje {nombre2}: '))


# personaje2 = PersonajeArmado(nombre2, arma2, salud2, vidas2, daño2)
# personaje2.iniciar_el_juego()
# input('Presione la tecla Enter para continuar.....')

# if personaje1.get_salud() > 0 and personaje2.get_salud() > 0:
#     pelea = Pelea(personaje1, personaje2)
#     pelea.batalla()


from random import *

class Personaje:
    # constructor
    def __init__(self, nombre_personaje, vidas = 3, salud = 100):
        self.__nombre_personaje = nombre_personaje
        self.__vidas = vidas
        self.__salud = salud
    
    # metodo setters (cargar) y getters (obtener) -Encapsulamiento-
    def set_nombre_personaje(self, nomb_pers):
        self.__nombre_personaje = nomb_pers
    
    def get_nombre_personaje(self):
        return self.__nombre_personaje
    
    def set_vidas(self, vidas):
        self.__vidas = vidas
    
    def get_vidas(self):
        return self.__vidas
    
    def set_salud(self, salud):
        self.__salud = salud
        
    def get_salud(self):
        return self.__salud


        
class Arma:
    # constructor
    def __init__(self, nombre_arma, provoca_danio = 0):
        self.__nombre_arma = nombre_arma
        self.__provoca_danio = provoca_danio
    
    # metodo getters y setters
    def get_nombre_arma(self):
        return self.__nombre_arma
    
    def get_provoca_danio(self):
        return self.__provoca_danio
    
    def set_nombre_arma(self, nombre_arm):
        self.__nombre_arma = nombre_arm
    
    def set_provoca_danio(self, prov_danio):
        denom_arma = self.get_nombre_arma()
        if denom_arma == 'cuchillo':
            self.__provoca_danio = 5
        elif denom_arma == 'espada':
            self.__provoca_danio = 10
        elif denom_arma == 'bacula':
            self.__provoca_danio = 8
        else:
            self.__provoca_danio = 0    
    
    

class PersonajeArmado(Personaje, Arma):
    def __init__(self, nombre_personaje, nombre_arma, vidas = 3, salud = 100, danio_provoca = 0 ):
        Personaje.__init__(self, nombre_personaje, vidas, salud)
        Arma.__init__(self, nombre_arma, danio_provoca)
        
        
    def atacar(self, atacado, danio):
        vida_actual = atacado.get_salud()
        queda_vida = vida_actual - danio
        atacado.set_salud(queda_vida)
        return atacado.get_salud()

    # polimorfismo (atacar)
    def pelea(self, retador, retado):
        eleccion = randint(0,1)
        if eleccion == 0:
            return f'El {retador.get_nombre_personaje()} atacó a {retado.get_nombre_personaje()}. {retado.get_nombre_personaje()} tiene {self.atacar(retado,10)} de salud.'
        else:
            return f'El {retado.get_nombre_personaje()} atacó a {retador.get_nombre_personaje()}. {retador.get_nombre_personaje()} tiene {self.atacar(retador,10)} de salud.'

        
        
perso = Personaje('pepe',3,100)
persa = Personaje('pepa',3,100)
perso.set_nombre_personaje('Pepa')
print(perso.get_nombre_personaje())
print(perso.get_vidas())
print(perso.get_salud())
print(perso.pelea(perso, persa))
print(perso.pelea(perso, persa))
print(perso.pelea(perso, persa))
print(perso.pelea(perso, persa))
print(perso.pelea(perso, persa))




# perso.__nombre_personaje = 'Pepe'
# print(perso.__nombre_personaje)
# print(perso.vidas)
# print(perso.salud)
# print(perso.__dir__())