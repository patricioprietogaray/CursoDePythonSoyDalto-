# Ejercicio 3: Producto, Libro y Electronico (Complejo)

# Crea una clase base llamada Producto con atributos como nombre, 
# precio y un método para obtener el precio. Luego, crea dos clases hijas: 
# Libro con atributos adicionales como autor y isbn, y Electronico con 
# atributos como voltaje y garantia_meses. Ambas clases deben usar super() 
# en su __init__. Además, la clase Libro debería tener un método para 
# mostrar la información bibliográfica completa, y la clase 
# Electronico un método para indicar el tiempo de garantía.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def obtener_precio(self):
        return f'Obteniendo el precio'

class Libro(Producto):
    def __init__(self, nombre, precio, autor, isbn):
        super().__init__(nombre, precio)
        self.autor = autor
        self.isbn = isbn
        
    def info(self):
        return f'Info: nombre: {self.nombre}, ${self.precio} - Author: {self.autor} - ISBN: {self.isbn}'


class Electronico(Producto):
    def __init__(self, nombre, precio, voltaje, garantia_meses):
        super().__init__(nombre, precio)
        self.voltaje = voltaje
        self.garantia_meses = garantia_meses
        
    def queda_garantia(self):
        return f'Info: Tiempo de garantía: {self.garantia_meses}.'


codigo = Libro('Codigo Da Vinci',100,'Dan Brown',123456789012345)
linux = Electronico('Linux a fondo',100,8,10)

print(codigo.info())
print(codigo.obtener_precio())

print(linux.queda_garantia())
