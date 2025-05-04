# ejercicio 2
# Ejercicio de herencia multiple y mro
# Imagina que estás modelando animales en un zoológico. Crear tres clases: 
# Animal, Mamífero y Ave. La clase animal debe tener un método llamado comer.
# La clase mamífero debe tener un método llamado amamantar y la clase Ave 
# un método llamado volar.
# Ahora crea una clase Murciélago que herede Mamífero y Ave en ese orden
# y por lo tanto debe ser capaz de amamntar y volar, ademas de comer.
# Finalmente juega con el orden de herencia de la clase Murciélago y observa 
# como cambia el MRO y el comportamiento de los métodos al usar super().

# --

class Animal:
    
    def comer(self):
        return f'El animal esta comiendo'

class Mamifero(Animal):
    
    def amamantar(self):
        return f'El mamífero está amamantando a su cría'

class Ave(Animal):
    
    def volar(self):
        return f'El ave está volando'

class Murcielago(Mamifero,Ave):
    pass
        



print('Animales del zoológico')
print('Murciélago')
murcielago = Murcielago()
print(murcielago.comer())
print(murcielago.volar())
print(murcielago.amamantar())
print('Loro')
loro = Ave()
print(loro.comer())
print(loro.volar())
print('Oso')
oso = Mamifero()
print(oso.comer())
print(oso.amamantar())
