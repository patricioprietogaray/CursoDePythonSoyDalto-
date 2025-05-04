# para crear una clase se utiliza la palabra reservada CLASS y se define con 
# PascalCase (otras son camelCase o snake_case)
class NombreDeLaClase():
    # atributos
    propiedad1 = "valor1" # si los atributos estan definidos de entrada son estáticos
    propiedad2 = "valor2"
    propiedad3 = "valor3"

# creando una clase
class Celular():
    # atributos o características
    marca = "Samsung"
    modelo = "S23"
    camara = "48MPx"
    

# Un objeto es una instancia de una clase, la clase es como una plantilla y 
# el objeto copia esa plantilla y a su vez le da su forma particular, es 
# por ello que a partir de una clase pueden "salir" x objetos distintos.

# creando tres objetos celular
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
print(f'celular1: {celular1}')  # <__main__.Celular object at 0x72dec911b350> 

# si quiero acceder a los datos de los atributos estáticos
print(f'Marca: {celular1.marca}')    # Marca: Samsung
print(f'Modelo: {celular1.modelo}')  # Modelo: S23
print(f'Cámara: {celular1.camara}')  # Cámara: 48MPx

# en comparacion al ejercicio 0001 de POO es mucho mas compacto todo esto
# y no tengo que hacer una definicion kilométrica.

# puedo modificarlos
celular1.marca = "Apple"
print(celular1.marca)  # devuelve Apple

# voy a crear otro objeto; instanciar una clase == objeto
celular4 = Celular()
print(celular4.marca)  # devuelve Samsung

# puedo modificar algo una vez creado pero al instanciarlo asigna los datos
# fijos o estáticos de la clase
