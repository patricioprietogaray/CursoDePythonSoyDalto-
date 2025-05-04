# Ejercicio de Clases 4: Jerarquía de Animales
#
# 1. Define una clase base llamada Animal.
#    - Debe tener un atributo 'nombre' (string) inicializado en el constructor.
#    - Debe tener un método 'emitir_sonido()' que imprima un sonido genérico como "El animal emite un sonido."
#
# 2. Define dos clases derivadas de Animal: Perro y Gato.
#    - La clase Perro debe sobrescribir el método 'emitir_sonido()' para imprimir "¡Guau!".
#    - La clase Gato debe sobrescribir el método 'emitir_sonido()' para imprimir "¡Miau!".
#
# 3. Define una clase derivada de Perro llamada Labrador.
#    - No necesita atributos adicionales en su constructor (puede llamar al constructor de la clase padre).
#    - Puede sobrescribir el método 'emitir_sonido()' para imprimir "¡Guau, guau!".
#
# 4. Define una clase derivada de Gato llamada Siamés.
#    - No necesita atributos adicionales en su constructor.
#    - Puede sobrescribir el método 'emitir_sonido()' para imprimir "¡Miau, miau!".
#
# 5. Crea instancias de cada una de las clases: Animal, Perro, Gato, Labrador y Siamés.
# 6. Llama al método 'emitir_sonido()' en cada instancia y observa los resultados.
# 7. Adicionalmente, crea una función que tome un objeto Animal como argumento y llame a su método 'emitir_sonido()'.
#    Luego, llama a esta función pasando las instancias de las diferentes clases. Observa cómo funciona el polimorfismo.

# Aquí va tu código:

# clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def emitir_sonido(self):
        print('El animal emite sonido')

# clase hijo
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def emitir_sonido(self):
        # super().emitir_sonido() # 'El animal emite sonido'
        print('Guau')

# clase hijo
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def emitir_sonido(self):
        # super().emitir_sonido() # 'El animal emite sonido'
        print('Miau')

# subclase de Perro
class Labrador(Perro):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def emitir_sonido(self):
        # super().emitir_sonido()
        print('¡Guau, guau!')


# subclase de Gato
class Siames(Gato):
    def __init__(self, nombre):
        super().__init__(nombre)

    def emitir_sonido(self):
        # super().emitir_sonido()
        print('¡Miau, miau!')

print('Clase Padre: ProtoAnimal')
animalito = Animal('ProtoAnimal') 
animalito.emitir_sonido()

print('\nClase Hijo: Perro')
perrito = Perro('Perro Genérico')
perrito.emitir_sonido()

print('\nClase Hijo: Gato')
gatito = Gato('Gato Genérico')
gatito.emitir_sonido()

print('\nSubClase de Perro: Labrador')
labradorcito = Labrador('Perro Labrador')
labradorcito.emitir_sonido()

print('\nSubClase de Gato: Siamés')
siamecito = Siames('Gato Genérico')
siamecito.emitir_sonido()

