# Consigna del Ejercicio: "Arena de Combate de Héroes"
# Objetivo:

# El objetivo de este ejercicio es diseñar y programar un sistema modular 
# para simular combates por turnos entre diferentes tipos de héroes en una arena. 
# Deberás aplicar los principios de la Programación Orientada a Objetos (POO) 
# para crear una estructura de clases clara, reutilizable y fácil de extender.

# Contexto:

# Imagina que estás creando un pequeño juego de rol. 
# En este mundo, existen diferentes clases de personajes 
# (Guerreros, Magos, Arqueros, etc.), 
# cada uno con sus propias estadísticas y habilidades. 
# Tu tarea es modelar este sistema.

# Parte 1: La Clase Base - Personaje
# Primero, debes crear una clase base llamada Personaje. 
# Todo personaje en nuestro juego, 
# sin importar su especialización, 
# compartirá estas características y acciones.

# Atributos:

# nombre (str): El nombre del personaje.
# salud (int): Los puntos de vida actuales del personaje.
# salud_max (int): Los puntos de vida máximos 
# que puede tener el personaje.
# poder_ataque (int): La cantidad de daño base 
# que inflige el personaje.
# esta_vivo (bool): Un booleano que indica 
# si el personaje sigue en combate.
# Métodos:

# __init__(self, nombre, salud, poder_ataque): 
# El constructor de la clase. 
# Debe inicializar todos los atributos. 
# La salud_max debe ser igual a la salud inicial. 
# esta_vivo debe ser True.

# atacar(self, oponente): 
# Este método debe reducir la salud del oponente 
# en una cantidad igual al poder_ataque del 
# personaje actual. 
# Después de atacar, debe imprimir un mensaje que 
# describa la acción (ej: "¡Aragorn ataca a Saruman 
# y le causa 15 puntos de daño!").

# recibir_daño(self, cantidad_daño): 
# Reduce la salud del personaje. 
# Si la salud llega a 0 o menos, 
# el atributo esta_vivo debe cambiar a False. 
# Imprime un mensaje informando el daño recibido 
# y la salud restante.


# mostrar_estado(self): Muestra el nombre y 
# la salud actual del personaje 
# (ej: "Gandalf - Salud: 80/100 HP").


# Parte 2: Las Clases Especializadas - Herencia
# Ahora, crearás al menos 
# dos clases de personajes que hereden de la 
# clase Personaje. 
# Estas clases tendrán atributos y/o métodos únicos.

# 1. Clase Guerrero (Hereda de Personaje)

# Atributo adicional:
# furia (int): Un recurso que el guerrero 
# acumula para usar su habilidad especial. Comienza en 0.
# Método sobreescrito (atacar):
# El atacar del Guerrero debe ser diferente. 
# Además de hacer daño, 
# cada vez que ataca, 
# su furia debe aumentar en 10.
# Nuevo método (ataque_furioso):
# Este método solo se puede usar si el Guerrero 
# tiene al menos 40 de furia.
# Realiza un ataque que inflige el doble del 
# poder_ataque normal (poder_ataque * 2).
# Después de usarlo, la furia del 
# Guerrero se reinicia a 0.
# Si no tiene suficiente furia, 
# debe imprimir un mensaje indicándolo.


# 2. Clase Mago (Hereda de Personaje)

# Atributo adicional:
# mana (int): El recurso que el mago 
# usa para sus hechizos.
# mana_max (int): La cantidad máxima de maná.
# Método sobreescrito (atacar):
# El atacar del Mago es un ataque básico 
# que no consume maná, 
# pero es más débil. 
# Para simular esto, 
# puedes hacer que su poder_ataque inicial sea bajo.
# Nuevo método (lanzar_hechizo):
# Este método consume 25 de mana.
# Inflige un daño mágico igual a poder_ataque + 30.
# Si el Mago no tiene suficiente mana, 
# debe imprimir un mensaje y no realizar el ataque. 
# En su lugar, podría regenerar 10 de maná ese turno.

# Parte 3: La Simulación - Arena
# Crea una clase Arena que se encargue 
# de gestionar el combate entre dos personajes.

# Atributos:

# heroe1 (Objeto de tipo Personaje o subclase).
# heroe2 (Objeto de tipo Personaje o subclase).
# Métodos:

# __init__(self, heroe1, heroe2): 
# Constructor que recibe los dos combatientes.
# combatir(self):
# Este es el método principal. 
# Debe simular un combate por turnos 
# hasta que uno de los dos personajes 
# ya no esté vivo (esta_vivo == False).

# En cada turno, un personaje ataca al otro. 
# Puedes decidir el orden de ataque 
# (por ejemplo, heroe1 siempre ataca primero, 
# o puede ser aleatorio).

# Importante: En el turno de cada personaje, 
# debes darle la opción de realizar una acción especial si es posible (ej: si es un Guerrero con suficiente furia, que use ataque_furioso). Puedes implementar una lógica simple: si la habilidad especial está disponible, la usa; si no, realiza un ataque normal.
# Después de cada acción, se debe mostrar el estado de ambos combatientes usando su método mostrar_estado().
# Al final del combate, el método debe declarar al ganador imprimiendo un mensaje claro (ej: "¡La batalla ha terminado! El ganador es Legolas.").
# Puesta en Práctica (El main de tu programa):
# Para probar tu código, en la sección principal de tu script (if __name__ == "__main__":):

# Crea una instancia de un Guerrero (ej: conan = Guerrero("Conan", 120, 20)).
# Crea una instancia de un Mago (ej: gandalf = Mago("Gandalf", 80, 10, mana=100)).
# Crea una instancia de la Arena con los dos héroes que creaste.
# Llama al método combatir() de la arena para iniciar la simulación.
# ¡Mucha suerte! Este ejercicio te ayudará a afianzar cómo las clases interactúan entre sí y cómo la herencia te permite crear código más limpio y escalable. ¡A programar!

import random

# clase base
class Personaje:
    def __init__(self, nombre, salud, poder_ataque, esta_vivo = True):
        self.nombre = nombre
        self.salud = salud
        self.salud_max = self.salud
        self.poder_ataque = poder_ataque
        self.esta_vivo = esta_vivo

    def atacar(self, oponente):
        # oponente.salud = oponente.salud - self.poder_ataque
        print (f'¡{self.nombre} ataca a {oponente.nombre} y le causa {self.poder_ataque} puntos de daño!')


    def recibir_daño(self, cantidad_daño):
        self.salud = self.salud - cantidad_daño        
        if self.salud <= 0:
            self.esta_vivo = False
            print(f'¡{self.nombre} ha muerto!')
        else:
            print(f'¡{self.nombre} le queda {self.salud} puntos de salud!')

    def mostrar_estado(self):
        print(f'¡{self.nombre} le queda {self.salud} puntos de salud.')

class Guerrero(Personaje):
    def __init__(self, nombre, salud, poder_ataque, furia = 0, esta_vivo=True):
        super().__init__(nombre, salud, poder_ataque, esta_vivo)
        self.furia = furia

    def atacar(self, oponente):
        self.furia += 10
        return super().atacar(oponente)
    
    def ataque_furioso(self):
        if self.furia >= 40:
            self.furia = 0
            return self.poder_ataque * 2
        else:
            return 'El guerrero se comió los mocos (no tiene tanta furia!).'

class Mago(Personaje):
    def __init__(self, nombre, salud, poder_ataque, mana, mana_max, esta_vivo=True):
        super().__init__(nombre, salud, poder_ataque, esta_vivo)
        self.mana = mana
        self.mana_max = mana_max

    def atacar(self, oponente):
        self.poder_ataque = 4
        print (f'¡{self.nombre} ataca a {oponente.nombre} y le causa {self.poder_ataque} puntos de daño!')
    
    def lanzar_hachizo(self, oponente):
        if self.mana >= 25:
            self.mana -= 25
            self.poder_ataque = 30
            super().atacar(self, oponente)
        else:
            print(f'No hay suficiente mana (más de 25): {self.mana}')
            self.mana += 10

class Arena:
    def __init__(self, heroe1, heroe2):
        self.heroe1 = heroe1
        self.heroe2 = heroe2
    
    def combatir(self):
        if self.heroe1.esta_vivo == False:
            print(f'El {self.heroe1.nombre} ha muerto!')
            return 'muerto'
        elif self.heroe2.esta_vivo == False:
            print(f'El {self.heroe2} ha muerto!')
            return 'muerto'
        ataque_aleatorio = random.randint(0,1)
        if ataque_aleatorio == 0:
            personaje = self.heroe1.nombre
            self.heroe2.salud -= self.heroe1.poder_ataque
            if self.heroe2.salud < 1:
                self.heroe2.esta_vivo = False
                return personaje,'muerto'
            else:
                print(f'{self.heroe1.nombre} ataca a {self.heroe2.nombre} y lo deja con {self.heroe2.salud} de salud.')
                return 'heroe2'
        else:
            personaje = self.heroe2.nombre
            self.heroe1.salud -= self.heroe2.poder_ataque
            if self.heroe1.salud < 1:
                self.heroe1.esta_vivo = False
                return personaje,'muerto'
            else:
                print(f'{self.heroe2.nombre} ataca a {self.heroe1.nombre} y lo deja con {self.heroe1.salud} de salud.')
                return 'heroe1'

        

# terminal

arturo = Guerrero('Arturo', 100, 15, 25,True)
merlin = Mago('Merlin', 100, 15, 50, 100, True)

arena = Arena(arturo, merlin)

while True:
    respuesta = arena.combatir()
    if respuesta[1] == 'muerto':
        print(f'El {respuesta[0]} ha {respuesta[1]}!.')
        break
    else:
        print('Ataque')
        input()

dgfsfgdsfgd





# local = Personaje('Local', 100, 15, True)
# visitante = Personaje('Visitante',100,12,True)






# visitante.mostrar_estado()
# local.mostrar_estado()
# print('')


# while local.salud >= 0 or visitante.salud >= 0:
#     local.atacar(visitante)
#     visitante.recibir_daño(local.poder_ataque)
#     local.mostrar_estado()
#     print('')


#     local.mostrar_estado()
#     visitante.mostrar_estado()
#     print('')
#     visitante.atacar(local)
#     local.recibir_daño(visitante.poder_ataque)
#     visitante.mostrar_estado()
#     print('')


#     visitante.mostrar_estado()
#     local.mostrar_estado()
#     print('')

    


    # print(visitante.mostrar_estado())

    # print(visitante.atacar(local))
    # print(local.mostrar_estado())




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


# from random import *

# class Personaje:
#     # constructor
#     def __init__(self, nombre_personaje, vidas = 3, salud = 100):
#         self.__nombre_personaje = nombre_personaje
#         self.__vidas = vidas
#         self.__salud = salud
    
#     # metodo setters (cargar) y getters (obtener) -Encapsulamiento-
#     def set_nombre_personaje(self, nomb_pers):
#         self.__nombre_personaje = nomb_pers
    
#     def get_nombre_personaje(self):
#         return self.__nombre_personaje
    
#     def set_vidas(self, vidas):
#         self.__vidas = vidas
    
#     def get_vidas(self):
#         return self.__vidas
    
#     def set_salud(self, salud):
#         self.__salud = salud
        
#     def get_salud(self):
#         return self.__salud


        
# class Arma:
#     # constructor
#     def __init__(self, nombre_arma, provoca_danio = 0):
#         self.__nombre_arma = nombre_arma
#         self.__provoca_danio = provoca_danio
    
#     # metodo getters y setters
#     def get_nombre_arma(self):
#         return self.__nombre_arma
    
#     def get_provoca_danio(self):
#         return self.__provoca_danio
    
#     def set_nombre_arma(self, nombre_arm):
#         self.__nombre_arma = nombre_arm
    
#     def set_provoca_danio(self, prov_danio):
#         denom_arma = self.get_nombre_arma()
#         if denom_arma == 'cuchillo':
#             self.__provoca_danio = 5
#         elif denom_arma == 'espada':
#             self.__provoca_danio = 10
#         elif denom_arma == 'bacula':
#             self.__provoca_danio = 8
#         else:
#             self.__provoca_danio = 0    
    
    

# class PersonajeArmado(Personaje, Arma):
#     def __init__(self, nombre_personaje, nombre_arma, vidas = 3, salud = 100, danio_provoca = 0 ):
#         Personaje.__init__(self, nombre_personaje, vidas, salud)
#         Arma.__init__(self, nombre_arma, danio_provoca)
        
        
#     def atacar(self, atacado, danio):
#         vida_actual = atacado.get_salud()
#         queda_vida = vida_actual - danio
#         atacado.set_salud(queda_vida)
#         return atacado.get_salud()

#     # polimorfismo (atacar)
#     def pelea(self, retador, retado):
#         eleccion = randint(0,1)
#         if eleccion == 0:
#             return f'El {retador.get_nombre_personaje()} atacó a {retado.get_nombre_personaje()}. {retado.get_nombre_personaje()} tiene {self.atacar(retado,10)} de salud.'
#         else:
#             return f'El {retado.get_nombre_personaje()} atacó a {retador.get_nombre_personaje()}. {retador.get_nombre_personaje()} tiene {self.atacar(retador,10)} de salud.'

        
        
# perso = Personaje('pepe',3,100)
# persa = Personaje('pepa',3,100)
# perso.set_nombre_personaje('Pepa')
# print(perso.get_nombre_personaje())
# print(perso.get_vidas())
# print(perso.get_salud())
# print(perso.pelea(perso, persa))
# print(perso.pelea(perso, persa))
# print(perso.pelea(perso, persa))
# print(perso.pelea(perso, persa))
# print(perso.pelea(perso, persa))




# # perso.__nombre_personaje = 'Pepe'
# # print(perso.__nombre_personaje)
# # print(perso.vidas)
# # print(perso.salud)
# # print(perso.__dir__())