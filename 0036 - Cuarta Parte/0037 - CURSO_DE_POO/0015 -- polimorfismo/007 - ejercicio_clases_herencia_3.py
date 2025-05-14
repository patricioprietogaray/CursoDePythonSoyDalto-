# Complejo: FiguraGeometrica, Circulo y Rectangulo (Heredando de FiguraGeometrica)

# Crea una clase base FiguraGeometrica con un constructor que reciba color y un método describir_figura() que imprima "Esta figura es de color {color}."
# Esta clase también debe tener métodos abstractos (puedes usar pass por ahora o raise NotImplementedError) llamados calcular_area() y calcular_perimetro().
# Crea una clase Circulo que herede de FiguraGeometrica.
# Su constructor recibirá color y radio.
# Implementa calcular_area() ($ \pi \cdot radio^2 $) y calcular_perimetro() ($ 2 \cdot \pi \cdot radio $).
# Sobrescribe describir_figura() para añadir información sobre el radio.
# Crea una clase Rectangulo (diferente a la del ejercicio anterior de solo clases) que herede de FiguraGeometrica.
# Su constructor recibirá color, longitud y ancho.
# Implementa calcular_area() y calcular_perimetro().
# Sobrescribe describir_figura() para añadir información sobre la longitud y el ancho.
# Crea instancias de Circulo y Rectangulo, y prueba todos sus métodos.




import math
# Crea una clase base FiguraGeometrica con un 
# constructor que reciba color y un método describir_figura() 
# que imprima "Esta figura es de color {color}."
class FiguraGeometrica:
    def __init__(self, color):
        self.color = color
        
    def describir_figura(self):
        return f'Esta figura es de color {self.color}.'

# Esta clase también debe tener métodos abstractos 
# (puedes usar pass por ahora o raise NotImplementedError) 
# llamados calcular_area() y calcular_perimetro().
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        raise NotImplementedError()


# Crea una clase Circulo que herede de FiguraGeometrica.
class Circulo(FiguraGeometrica):
# Su constructor recibirá color y radio.
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
# Implementa calcular_area() ($ \pi \cdot radio^2 $) 
    def calcular_area(self):
        return f'El área del circulo es de {math.pi * self.radio ** 2} unidades cuadradas.'
# calcular_perimetro() ($ 2 \cdot \pi \cdot radio $).    
    def calcular_perimetro(self):
        return f'El perímetro del circulo es de {2 * math.pi * self.radio} unidades.'
# Sobrescribe describir_figura() para añadir información sobre el radio.
    def describir_figura(self):
        return f'Esta figura es de color {self.color} y tiene un radio {self.radio} unidades.'


# Crea una clase Rectangulo (diferente a la del ejercicio anterior 
# de solo clases) que herede de FiguraGeometrica.
# Su constructor recibirá color, longitud y ancho.
class Rectangulo(FiguraGeometrica):
    def __init__(self, color, longitud, ancho):
        super().__init__(color)
        self.longitud = longitud
        self.ancho = ancho
# Implementa calcular_area() y calcular_perimetro().
    def calcular_area(self):
        return f'El area del rectángulo es de {self.ancho * self.longitud} unidades cuadradas.'
    def calcular_perimetro(self):
        return f'El perímetro del rectángulo es de {2 * (self.ancho + self.longitud)} unidades.'
# Sobrescribe describir_figura() para añadir información sobre la longitud y el ancho.
    def describir_figura(self):
        return f'Esta figura es de color {self.color} y tiene un ancho {self.ancho} unidades y longitud {self.longitud} unidades.'
# Crea instancias de Circulo y Rectangulo, y prueba todos sus métodos.

circulo = Circulo('Verde', 23)
rectangulo = Rectangulo('Rojo', 12, 22)

print(circulo.describir_figura())
print(circulo.calcular_area())
print(circulo.calcular_perimetro())

print(rectangulo.describir_figura())
print(rectangulo.calcular_area())
print(rectangulo.calcular_perimetro())

