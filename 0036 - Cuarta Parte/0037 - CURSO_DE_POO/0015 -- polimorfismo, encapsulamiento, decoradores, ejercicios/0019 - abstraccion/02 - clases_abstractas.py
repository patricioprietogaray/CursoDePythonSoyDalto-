# CLASES ABSTRACTAS

# UNA CLASE ABSTRACTA: es una clase que no podemos instanciar, es como una receta
# es una plantilla que podemos crear clases a partir de dicha plantilla.
# por ejemplo creo una clase persona (defino atributos nombre, edad, etc 
# y metodos basicos caminar, hablar, etc)
# es como la HERENCIA MAS COMPLEJA puede crear una instancia de jefe (hereda de persona)
# pero no directamente una instancia de persona.

# IMPLEMENTAR UN METODO significa de como va a funcionar. 
# para implementar un metodo "hacer_sonido()" debo crear un codigo que haga sonido
# para un gato hacer sonido sera miau y para un perro guau.
# 
# en el codigo from abc (modulo de python) 
# import ABC (es una clase), 
# abstractclassmethod (decorador para usar un metodo abstracto).
# ABC es una clase auxiliar que tiene una metaclase (clase de la clase, define como se comporta
# una clase)
# UN METODO ABASTRACTO es un metodo que esta declarado en esta plantilla (clase abstracta)
# solo que no tiene ninguna implementacion.
# por ejemplo creo el método hacer_sonido() pero no lo implemento, 
# .
# .

# from abc import ABC, abstractclassmethod
from abc import ABC, abstractmethod, abstractclassmethod

# creo la clase Persona y heredo ABC 
# ahora Persona es una clase abstracta
class Persona(ABC):
    # crear un metodo abstracto usando el decorador abstractclassmethod
    @abstractclassmethod
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    @abstractmethod
    def hacer_actividad(self):
        pass  #hay muchas tareas segun el trabajo, esto se sobreescribe luego

    def presentarse(self):
        print(f'Hola me llamo: {self.nombre} y tengo {self.edad} años.')


# heredo y creo una clase desde la plantilla
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    # SE DEBE IMPLEMENTAR LOS METODOS ABSTRACTOS DE MANERA OBLIGATORIA
    def hacer_actividad(self):
        print(f'Mi actividad es: {self.actividad}')
    


# heredo y creo una clase desde la plantilla
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    # SE DEBE IMPLEMENTAR LOS METODOS ABSTRACTOS DE MANERA OBLIGATORIA
    def hacer_actividad(self):
        print(f'Trabajo de: {self.actividad}')
    




#  no se puede porque al heredar ABC es un metodo abstracto es una plantilla
# que no se puede instanciar.....
# prieto = Persona('prieto', 89, 'masculino', 'analista de sistemas')   TIRA ERROR!

prieto = Estudiante('Prieto Garay', 75, 'masculino', 'analista de sistemas')
prieto.presentarse()
prieto.hacer_actividad()

garay = Trabajador('Garay', 150, 'masculino', 'vendedor')
garay.presentarse()
garay.hacer_actividad()



