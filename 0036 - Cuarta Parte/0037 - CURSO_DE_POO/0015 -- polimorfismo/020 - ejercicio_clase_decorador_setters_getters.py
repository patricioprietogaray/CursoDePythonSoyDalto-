# En Python, @property es un decorador 
# que te permite definir métodos en una clase 
# como si fueran atributos. 
# 
# Esto significa que podés acceder a un método 
# como si fuera una variable, 
# sin necesidad de usar paréntesis (). 
# 
# Su principal objetivo es proporcionar una forma "pythónica" 
# de manejar los getters y setters 
# (métodos para obtener y establecer valores de atributos) 
# sin la necesidad de llamar explícitamente a esos métodos.

class Producto:
    def __init__(self, nombre, precio):
        # ATRIBUTO PRIVADO POR CONVENCION
        self._nombre = nombre
        self._precio = 0.0
        # Usamos el SETTER para inicializar el precio
        self.precio = precio
        
    
    # usando el decorador property (propiedad)
    
    @property
    def precio(self):
        '''El Getter para el atributo precio.'''
        print('Obteniendo el precio')
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        '''El Setter para el atributo precio con validacion'''
        print('Estableciendo el precio ....')
        if nuevo_precio < 0.0:
            raise ValueError('El precio no puede ser negativo.')
        self._precio = nuevo_precio

    @precio.deleter
    def precio(self):
        '''El deleter para el atributo precio'''
        print('Eliminando el precio ....')
        del self._precio

# terminal
# crear una instancia del producto (debe estar definido el getter y el setter)
mi_producto = Producto('Motor',2000)

# Acceso al getter
print(f'Accediendo al precio del producto: {mi_producto.precio}')

# tira error si accedo a precio()

# Modifico el precio con setter
mi_producto.precio=30.52

# Acceso al getter
print(f'Accediendo al precio del producto: {mi_producto.precio}')

# Asigno un número negativo al precio
# # Modifico el precio con setter

try:
    mi_producto.precio=-300.52
except ValueError as e:
    print(f'Error: {e}. Precio -300.52')

# Acceso al getter
print(f'Accediendo al precio del producto: {mi_producto.precio}')

# Eliminar el atributo precio
del mi_producto.precio

# # Acceso al getter
# print(f'Accediendo al precio del producto: {mi_producto.precio}')

# # intentar acceder al precio luego de eliminarlo
try:
#     # Eliminar el precio con deleter
    print(mi_producto.precio)
except AttributeError as e:
    print(f'Error al acceder luego de eliminar: {e}')


# # Acceso al getter
# print(f'Accediendo al precio del producto (después de ser borrado): {mi_producto.precio}')





# # Modifico el precio con setter
# mi_producto.precio=-30.52

# # Acceso al getter
# print(f'Accediendo al precio del producto: {mi_producto.precio}')
