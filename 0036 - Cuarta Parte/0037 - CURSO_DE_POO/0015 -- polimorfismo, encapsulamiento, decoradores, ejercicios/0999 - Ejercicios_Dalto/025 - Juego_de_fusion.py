# CREAR UN JUEGO DE FUSION

# El juego consiste en crear personajes de un juego y 
# que esos personajes se puedan fusionar para formar personajes 
# más poderosos que tengan más poder...

# Para ello deberemos cambiar el comportamiento del operador "+" 
# para que cuando los personajes se fusionen, 
# salga un nuevo personaje con habilidades mejoradas.

# Una posible fórmula es: el promedio de las habilidades de ambos, al cuadrado!

class Personaje:
    # constructor carga el nombre y la habilidad del personajes (objeto)
    def __init__(self, nombre, habilidades):
        self.habilidades = habilidades
        self.nombre = nombre

    # El objeto inicial es el primer ojeto que se pasa (arturo)
    # en la adicion queda como arturo, merlin
    #  nue_valor = habilidad de arturo + habilidad de merlin
    # retorna al resultado (shrek) las habilidades sumadas

    # Una posible fórmula es: el promedio de las habilidades de ambos, al cuadrado!
    def __add__(self, otro_personaje):
        nuevo_nombre = self.nombre + otro_personaje.nombre
        nuevo_valor_habilidades = ((self.habilidades + otro_personaje.habilidades)/2)**2 
        return Personaje(nuevo_nombre, nuevo_valor_habilidades)

    # representacion
    def __repr__(self):
        return f'{self.nombre}: (habilidades: {self.habilidades}.)'


arturo = Personaje('Arturo', 23)
print(arturo)
# print(f'Nombre: {arturo.nombre}, habilidades: {arturo.habilidades}')
merlin = Personaje('Merlin', 33)  
print(merlin)
# print(f'Nombre: {merlin.nombre}, habilidades: {merlin.habilidades}')
shrek = arturo + merlin
print(shrek)
# print(f'Nombre: {shrek.nombre}, habilidades: {shrek.habilidades}')


# 2.53.49

