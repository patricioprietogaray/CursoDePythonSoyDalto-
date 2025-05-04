# ejercicio anterior en 0005

# ejercicio 2

# Herencias
# Ejercicio de herencia y uso de super()

# # Crear un sistema para una escuela. En este sistema vamos a tener
# # dos clases principales: Persona y Estudiante.
# # La clase Persona tendrá atributos nombre y edad y un método que imprima el nombre y la edad de la persona.
# # La clase estudiante heredará de la clase Persona, tambien tendrá un atributo adicional: grado y 
# # un método que imprima el grado del estudiante.

# Deberás utilizar super en el método de inicializacion (init) para reutilizar el código de la 
# clase padre Persona. Luego crea una instancia de la clase Estudiante e imprime sus atributos 
# y utiliza sus métodos para asegurarte que todo funciona correctamente.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimir(self):
        return f'La persona se llama {self.nombre} y tiene {self.edad} años.'

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)     # self no se pasa si usamos super()
        self.grado = grado
    
    def cursa(self):
        return f'El estudiante asiste al {self.grado}° grado.'




# terminal
print("Sistemas para Escuelas")
felipe = Estudiante('Felipe', 10, 4)
mafalda = Estudiante('Mafalda', 10, 4)

print('\nMostramos lo que hace Felipe')
print(felipe.imprimir())
print(felipe.cursa())

print('\nMostramos lo que hace Mafalda')
print(mafalda.imprimir())
print(mafalda.cursa())
