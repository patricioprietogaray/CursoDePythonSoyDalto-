# Fácil: Animal y Gato

# Crea una clase Animal con un constructor que reciba nombre 
# y un método comer() que imprima "{nombre} está comiendo."

# Crea una clase Gato que herede de Animal.

# El constructor de Gato debe recibir nombre y raza. 
# Debe llamar al constructor de Animal.

# Añade un método maullar() a Gato que imprima "¡Miau!".
# Crea una instancia de Gato, hazlo comer y maullar.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def comer(self):
        return f'{self.nombre} está comiendo.'
    
class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        
    def maullar(self):
        return ('¡Miau!')

gatito = Gato('Micha', 'Tigre')
print(gatito.comer())
print(gatito.maullar())

