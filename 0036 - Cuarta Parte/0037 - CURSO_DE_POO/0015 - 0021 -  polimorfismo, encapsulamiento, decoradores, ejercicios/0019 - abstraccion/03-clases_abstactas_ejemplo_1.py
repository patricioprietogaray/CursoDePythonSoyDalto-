from abc import ABC, abstractmethod

# Ahora Persona es una clase abstracta. Solo necesita heredar de ABC
# y tener al menos un método abstracto.
class Persona(ABC):
    # El constructor no necesita ser abstracto.
    # Se encarga de inicializar los atributos comunes a todas las "Personas".
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    # Este es el método que REALMENTE necesita ser abstracto,
    # porque cada tipo de Persona lo hará de forma diferente.
    # Solo usamos @abstractmethod para un método de instancia.
    @abstractmethod
    def hacer_actividad(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        Describe la actividad principal de la persona.
        """
        pass

    # Este método es concreto y lo heredan todas las clases hijas tal cual.
    def presentarse(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años.')


# Estudiante hereda de Persona e implementa el método abstracto.
class Estudiante(Persona):
    # No es necesario re-definir __init__ si va a hacer exactamente lo mismo
    # que el del padre. Python lo llamará automáticamente.
    # Lo definimos solo si queremos añadir algo más.
    
    # Implementación obligatoria del método abstracto.
    def hacer_actividad(self):
        print(f'Estoy estudiando para ser: {self.actividad}')


# Trabajador hereda de Persona e implementa el método abstracto.
class Trabajador(Persona):
    
    # Implementación obligatoria del método abstracto.
    def hacer_actividad(self):
        print(f'Mi trabajo es: {self.actividad}')


# --- Pruebas ---

# Esto seguirá dando error, ¡lo cual es correcto!
# TypeError: Can't instantiate abstract class Persona with abstract method hacer_actividad
# persona_fantasma = Persona('Fantasma', 99, 'indefinido', 'asustar')

print("--- Datos del Estudiante ---")
prieto = Estudiante('Prieto Garay', 22, 'masculino', 'Ingeniero de Software')
prieto.presentarse()
prieto.hacer_actividad()

print("\n--- Datos del Trabajador ---")
garay = Trabajador('Ana Garay', 35, 'femenino', 'Diseñadora Gráfica')
garay.presentarse()
garay.hacer_actividad()