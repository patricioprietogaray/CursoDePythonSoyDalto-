# Medio: Clase Rectangulo

# Crea una clase llamada Rectangulo.
# El constructor debe recibir longitud y ancho.
# Crea un método llamado calcular_area que 
# devuelva el área del rectángulo (longitud * ancho).
# Crea un método llamado calcular_perimetro que devuelva el perímetro 
# del rectángulo (2 * (longitud + ancho)).
# Crea un método es_cuadrado que devuelva True si la longitud y el ancho son iguales, 
# y False en caso contrario.
# Crea algunas instancias y prueba todos los métodos.

class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
        
    def calcular_area(self):
        return self.ancho * self.longitud
    
    def calcular_perimetro(self):
        return (2 * (self.ancho + self.longitud))
    
    def es_cuadrado(self):
        if self.longitud == self.ancho:
            return True
        return False

cuadrado = Rectangulo(2.3,2.3)
print(f'El área del cuadrado es: {cuadrado.calcular_area()} unidades cuadradas.')
print(f'El perímetro del cuadrado es: {cuadrado.calcular_perimetro()} unidades.')
print(f'Este cuadrado es realmente un cuadrado?: {cuadrado.es_cuadrado()}.')
    
rectangulo = Rectangulo(2,2.3)
print(f'El área del rectángulo es: {rectangulo.calcular_area()} unidades cuadradas.')
print(f'El perímetro del rectángulo es: {rectangulo.calcular_perimetro()} unidades.')
print(f'Este rectángulo es realmente un cuadrado?: {rectangulo.es_cuadrado()}.')
    