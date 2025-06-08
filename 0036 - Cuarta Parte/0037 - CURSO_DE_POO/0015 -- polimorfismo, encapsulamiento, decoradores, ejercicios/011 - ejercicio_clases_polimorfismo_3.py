# Medio: Personaje de Videojuego

# Crea una clase base Personaje con un atributo nombre y un método atacar(objetivo) que imprima "{nombre_personaje} realiza un ataque básico a {nombre_objetivo}."
# Crea clases derivadas: Guerrero y Mago.
# El Guerrero sobrescribe atacar(objetivo) para imprimir "{nombre_guerrero} golpea a {nombre_objetivo} con su espada."
# El Mago sobrescribe atacar(objetivo) para imprimir "{nombre_mago} lanza un hechizo a {nombre_objetivo}."
# Crea una función combate(personaje1, personaje2) que haga que cada personaje ataque al otro.
# Prueba la función combate con un Guerrero y un Mago.


# Crea una clase base Personaje con un atributo nombre 
# y un método atacar(objetivo) que imprima 
# "{nombre_personaje} realiza un ataque básico a {nombre_objetivo}."

class Personaje:
    def __init__(self, nombre_personaje):
        self.nombre_personaje = nombre_personaje
        
    def atacar(self, nombre_objetivo):
        return f'{self.nombre_personaje} realiza un ataque básico a {nombre_objetivo}.'

# Crea clases derivadas: Guerrero y Mago.
class Guerrero(Personaje):
    def __init__(self, nombre_personaje):
        super().__init__(nombre_personaje)
# El Guerrero sobrescribe 
# atacar(objetivo) para imprimir "{nombre_guerrero} golpea a 
# {nombre_objetivo} con su espada."
    def atacar(self, nombre_objetivo):
        return f'{self.nombre_personaje} golpea a {nombre_objetivo.nombre_personaje} con su espada.'

class Mago(Personaje):
    def __init__(self, nombre_personaje):
        super().__init__(nombre_personaje)
# El Mago sobrescribe atacar(objetivo) 
# para imprimir "{nombre_mago} lanza un hechizo a {nombre_objetivo}."
    def atacar(self, nombre_objetivo):
        return  f'{self.nombre_personaje} lanza un hechizo a {nombre_objetivo.nombre_personaje}.'

def combate(personaje1, personaje2):
# Crea una función combate(personaje1, personaje2) 
# que haga que cada personaje ataque al otro.
    print(personaje1.atacar(personaje2))
    print(personaje2.atacar(personaje1))


# Prueba la función combate con un Guerrero y un Mago.
guerrero = Guerrero('Tartañan')
mago = Mago('Coperfield')

print(f'El nombre del guerrero es: {guerrero.nombre_personaje}.')
print(f'El nombre del mago es: {mago.nombre_personaje}.')
print('El guerrero ataca al mago y el mago al guerrero: ')
combate(guerrero, mago)