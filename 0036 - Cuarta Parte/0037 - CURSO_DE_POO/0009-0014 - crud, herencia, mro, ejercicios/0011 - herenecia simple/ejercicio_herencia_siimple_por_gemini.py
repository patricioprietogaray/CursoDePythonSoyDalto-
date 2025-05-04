# Ejercicio de Clases 3: Herencia Simple - Figuras Geométricas
#
# 1. Define una clase base llamada FiguraGeometrica.
#    - Debe tener un atributo llamado 'nombre' (string) que se inicializa en el constructor.
#    - Debe tener un método llamado 'area()' que, por defecto, devuelva 0 (ya que la forma base no tiene un área definida).
#    - Debe tener un método llamado 'descripcion()' que imprima una descripción genérica de la figura,
#      incluyendo su nombre.
#
# 2. Define una clase derivada llamada Rectangulo que herede de FiguraGeometrica.
#    - Debe tener atributos adicionales para 'base' (float) y 'altura' (float), que se inicializan en su constructor.
#    - Debe sobrescribir el método 'area()' para calcular y devolver el área del rectángulo (base * altura).
#    - Debe sobrescribir el método 'descripcion()' para incluir las dimensiones del rectángulo en la descripción.
#
# 3. Define otra clase derivada llamada Circulo que también herede de FiguraGeometrica.
#    - Debe tener un atributo adicional para 'radio' (float), que se inicializa en su constructor.
#    - Debe sobrescribir el método 'area()' para calcular y devolver el área del círculo (pi * radio^2).
#      Puedes usar el valor de pi del módulo 'math'.
#    - Debe sobrescribir el método 'descripcion()' para incluir el radio del círculo en la descripción.
#
# 4. Crea instancias de las clases Rectangulo y Circulo.
# 5. Llama a los métodos 'area()' y 'descripcion()' en cada instancia para mostrar sus propiedades.

import math

# Aquí va tu código:

# clase padre
class FiguraGeometricas:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def area(self):
        return 0
    
    def descripcion(self):
        print(f'Figura geomética: {self.nombre}.')
        print('Definicion:\nUna figura geométrica es una representación visual de una forma compuesta por puntos,\nlíneas, curvas o ángulos. Las figuras geométricas pueden ser bidimensionales o tridimensionales. ')


class Rectangulo(FiguraGeometricas):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = float(base)
        self.altura = float(altura)
    
    def area(self):
        return self.base * self.altura
    
    def descripcion(self):
        super().descripcion()
        print(f'El rectángulo tiene un area de {self.area()} unidades cuadradas.')

class Circulo(FiguraGeometricas):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = float(radio)
            
    def area(self):
        return math.pi * pow(self.radio,2)
    
    def descripcion(self):
        super().descripcion()
        print(f'El circulo tiene un area de {self.area()} unidades cuadradas.')








fiGeo = FiguraGeometricas('figura simple')
rectang = Rectangulo('Rectangulo',20.0, 51.6)
circ = Circulo('Circulo', 25.0)

print('\nEl area de la figura geometrica')
print(f'El area: {fiGeo.area()}')
fiGeo.descripcion()

print(f'\nEl area del rectángulo')
print(f'El area: {rectang.area()}')
rectang.descripcion()

print(f'\nEl area del círculo')
print(f'El area: {circ.area()}')
circ.descripcion()