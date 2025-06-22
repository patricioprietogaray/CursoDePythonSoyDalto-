# Ejercicio: Sistema de Cálculo para Figuras Geométricas
# Contexto:
# Necesitas diseñar un sistema simple para manejar diferentes 
# figuras geométricas. 
# Todas las figuras tienen propiedades en común, 
# como un área y un perímetro, 
# pero la fórmula para calcularlas es específica para cada figura. 
# Este es un caso de uso perfecto para una clase abstracta.

# Tu Misión:

# Crear la Clase Abstracta FiguraGeometrica:

# Esta clase debe heredar de ABC.
# Debe tener un método __init__ que acepte 
# un nombre para la figura (ej: "Círculo", "Rectángulo").
# Debe declarar dos métodos abstractos 
# (¡recuerda el decorador!):
# calcular_area()
# calcular_perimetro()
# Ambos métodos abstractos deben quedar 
# sin implementación (puedes usar pass).

from abc import abstractmethod, ABC
from math import pi

class FiguraGeometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass



# Crear las Clases Concretas:

# Clase Circulo:

# Debe heredar de FiguraGeometrica.
# Su método __init__ debe recibir el radio. 
# Además, debe llamar al __init__ de la clase padre 
# para establecer el nombre como "Círculo".
# Debes implementar los métodos calcular_area() 
# y calcular_perimetro() con las fórmulas correspondientes al círculo.
# Área del círculo: π⋅radio 
# 2
 
# Perímetro (circunferencia) del círculo: 2⋅π⋅radio

class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        # self.nombre = nombre   --> lo hace la linea anterior
        self.__radio = radio

    def calcular_area(self):
        return pi * (self.__radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * pi * self.__radio

    # def set_radio(self, radio):
    #     self.__radio = radio
    
    def get_radio(self):
        return self.__radio

# Clase Rectangulo:

# Debe heredar de FiguraGeometrica.
# Su método __init__ debe recibir la base y la altura. 
# También debe llamar al __init__ del padre para darle el nombre "Rectángulo".
# Debes implementar calcular_area() y calcular_perimetro() con las fórmulas para un rectángulo.
# Área del rectángulo: base⋅altura
# Perímetro del rectángulo: 2⋅(base+altura)


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__('Rectángulo') #--> elimino nombre y le paso el valor directamente a la clase padre
        # self.nombre = nombre  --> lo hace la linea anterior
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura
    
    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)
    
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura



# Demostración:
# Crea una instancia de Circulo con un radio de 10.
circulito = Circulo('Circulo',10.0)
print(f'El calculo será en base a un radio de {circulito.get_radio()} unidades.')
print(f'El perímetro del {circulito.nombre} es de: {circulito.calcular_perimetro():.2f} unidades.')
print(f'El área del {circulito.nombre} es de: {circulito.calcular_area():.2f} unidades cuadradas.')

# Crea una instancia de Rectangulo con una base de 5 y una altura de 8.
# Para cada objeto, llama a sus métodos para calcular el área y el perímetro, 
# y muestra los resultados en la consola de una forma clara.
print()
rectangulito = Rectangulo(5,8)
print(f'El calculo será por la base ({rectangulito.get_base()} unidades), y la altura ({rectangulito.get_altura()} unidades).')
print(f'El perímetro del {rectangulito.nombre} es de: {rectangulito.calcular_perimetro():.2f} unidades.')
print(f'El área del {rectangulito.nombre} es de: {rectangulito.calcular_area():.2f} unidades cuadradas.')

# (Opcional, para verificar) Intenta crear una instancia de FiguraGeometrica directamente y comprueba que Python te lanza un TypeError.
# figu = FiguraGeometrica('pepe')


# Pistas:

# No te olvides de: from abc import ABC, abstractmethod.
# Para el valor de π, puedes importar el módulo math y usar math.pi.
# ¡Mucho éxito con el desafío! Tómate tu tiempo, analiza el problema y, cuando estés listo, muéstrame tu código para que lo revisemos juntos. ¡Tú puedes!