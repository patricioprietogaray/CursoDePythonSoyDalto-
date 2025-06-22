# si en python todo es un objeto
# significa que los objetos pertenecen a una clase
# o sea que hay una clase que define cada comportamiento
# o sea que un numero es una clase
# que si sumo un numero a otro es que alguien difinió
# como ese "más" se debe comportar.
# que pasaría si intento sumar dos elementos de mi clase???
# apareceria un nuevo objeto con una propiedad sumada????
# que sucederia??? 
# Esto es muy interesante, 
# ESTO SE DEFINE CON LA SOBRECARGA DE OPERADORES


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre = "{self.nombre}", edad = {self.edad}: suma de las edades!)'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    # SOBRECARGA DE OPERADORES: DEFINO LA SUMA COMO CONCATENADOR
    # definimos como se comportan los objetos de la clase Persona cuando se suman
    # los nombres se concatenan y las edades se suman.
    def __add__(self, otro):   # otro hace referencia al que queremos sumar
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)


# instancia
pato = Persona("Patricio", 32)
pepe = Persona("Marcelo", 45)
maria = Persona('Maria', 18)

# llama a __add__ nombres concatenados y le agrega la suma del valor total
resultado = pato + pepe + maria  

# llama a __str__
print(resultado)


# llama a __repr__
print(repr(resultado.nombre[0:5]))

# 2:47:23