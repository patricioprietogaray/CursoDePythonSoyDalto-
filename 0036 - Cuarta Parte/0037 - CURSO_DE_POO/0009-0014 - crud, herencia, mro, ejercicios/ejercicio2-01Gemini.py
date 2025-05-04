# Ejercicio 1: Figura y Rectángulo (Simple)

# Crea una clase base llamada Figura que tenga un atributo nombre. 
# Luego, crea una clase hija llamada Rectangulo que herede de Figura y 
# tenga atributos adicionales base y altura. La clase Figura debe tener 
# un método para describir la figura. La clase Rectangulo debe tener 
# su propio método para calcular su área, utilizando super() 
# para llamar al método de descripción de la figura padre y 
# luego añadir la información de sus dimensiones.

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def descripcion(self):
        return f'La figura es un {self.nombre}!'
        

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def calculo(self):
        print(super().descripcion())
        print(f'El área es: {self.base * self.altura}')


# presentacion del programa en el terminal
print('Clases con Figuras, Rectangulos y sus dimensiones')
rectangulo = Rectangulo('Rectangulo', 2,3)
# print(rectangulo.descripcion())
rectangulo.calculo()
