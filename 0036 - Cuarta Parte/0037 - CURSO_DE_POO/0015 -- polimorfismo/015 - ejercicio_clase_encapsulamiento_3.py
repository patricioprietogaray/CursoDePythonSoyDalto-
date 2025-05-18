# Medio: Producto

# Crea una clase Producto con atributos 
# "privados": __codigo (string), 
# __nombre (string) y 
# __precio (float).
# El constructor debe recibir estos tres valores.
# Implementa un método get_precio() para obtener el precio.
# Implementa un método set_precio(nuevo_precio) que permita cambiar el precio solo si nuevo_precio es positivo. Si no, debe imprimir un error.
# Implementa un método "protegido" _aplicar_descuento(porcentaje) que calcule el precio con descuento, pero no modifique el __precio original del producto. Este método debe ser llamado por un método público obtener_precio_con_descuento(porcentaje). El porcentaje debe estar entre 0 y 100.
# Crea un producto, obtén su precio, intenta cambiarlo a un valor negativo y luego a uno positivo. Prueba el método de descuento.



# Medio: Producto

# Crea una clase Producto con atributos 
# "privados": __codigo (string), 
# __nombre (string) y 
# __precio (float).
# El constructor debe recibir estos tres valores.
class Producto:
    def __init__(self, codigo, nombre, precio):
        # atributoss privados
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    # Implementa un método get_precio() para obtener el precio.
    def get_precio(self):
        return self.__precio
    # Implementa un método set_precio(nuevo_precio) 
    # que permita cambiar el precio solo si nuevo_precio es positivo. 
    # Si no, debe imprimir un error.
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0.0:
            self.__precio = nuevo_precio
            return f'\nSe ha modificado el precio! (${self.__precio})'
        else:
            return f'\nNo se ha modificado el precio!.\nEl precio debe ser positivo'
    # Implementa un método "protegido" _aplicar_descuento(porcentaje) 
    # que calcule el precio con descuento, 
    # pero no modifique el __precio original del producto. 
    # Este método debe ser llamado por un método público 
    # obtener_precio_con_descuento(porcentaje). 
    # El porcentaje debe estar entre 0 y 100.
    
    # metodo protegido
    def _aplicar_descuento(self,porcentaje):
        descuento = self.__precio * porcentaje / 100
        return self.__precio - descuento
    
    # metodo publico
    def obtener_precio_con_descuento(self, porcentaje):
        if 0.0 <= porcentaje <= 100.0:
            return self._aplicar_descuento(porcentaje)
        else:
            return 'El porcentaje de descuento debe estar en el rango de 0.0 a 100.0.'
# Crea un producto, obtén su precio, 
# intenta cambiarlo a un valor negativo 
# y luego a uno positivo. 
# Prueba el método de descuento.


# ejecutar python en terminal dedicado (python3)
producto = Producto('01','Petróleo',123.25)
print(f'El precio del producto es ${producto.get_precio()}')
print('Modifico el precio a 100')
print(producto.set_precio(1000.0))
print(producto.set_precio(-100.0))
print(f'El producto de un valor de ${producto.get_precio()}\ntiene un descuento del 8%\ny su valor final es de ${producto.obtener_precio_con_descuento(8)}!')
