# METODOS DUNDER O METODOS ESPECIALES

# https://youtu.be/HtKqSJX7VoM?t=9481
# 2.38.00

class Persona:
    # método espacial: constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo especial: modo de texto
    # devuelve un texto cuando invoco solo a la clase
    # ej: Persona(nombre = Pato, edad = 25)
    def __str__(self):
        return f'Persona(nombre = {self.nombre}, edad = {self.edad})'
    
    
    # Si str no existe el resultado por pantalla es: 
    # # <__main__.Persona object at 0x7f38230136d0>
    # def __str__(self):
    #     return f'Persona(nombre = {self.nombre}, edad = {self.edad})'

class Es_Tupla:
    def __init__(self, dato1str, dato2int):
        self.dato1str = dato1str
        self.dato2int = dato2int
    
    def __str__(self):
        return (f'("Es tupla: Str:{self.dato1str}", Int:{self.dato2int})')

    # reconstruir un objeto
    def __repr__(self):
        return (f'("{self.dato1str}", {self.dato2int})')



pato = Persona('Pato', 25)
print(pato)

tupla = Es_Tupla('Pato', 25)
print(tupla)

representacion = repr(tupla)
resultado = eval(representacion)
print(resultado[1])

# 2.43.00