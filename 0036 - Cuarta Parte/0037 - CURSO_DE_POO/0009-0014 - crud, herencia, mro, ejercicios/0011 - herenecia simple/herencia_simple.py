# herencia (inheritance)

# Unos de los pilares fundamentales de la programación orientada a objetos
# permite que la clase hija pueda acceder a todos los metodos y propiedades de la clase padre
# ejemplo clase padre Persona, y clase hija Estudiante. Un estudiante es una persona y 
# la clase Estudiante heredará todo los atributos y métodos de la clase Persona.
# Ademas la clase Estudiante tendrá sus propios métodos (aparte de Persona)

# herencia simple

# ************* #
#    Persona    #   (Padre o superclase)
# ************* #
    # |
    #  |
# *************** #
#     Empleado    # (Hija o subclase)
# *************** #

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def presentacion(self):
        print(f'Hola, soy {self.nombre}, tengo {self.edad} años y soy de {self.nacionalidad}')

# construyendo una clase hija -> class hija(padre):
# class Empleado(Persona):
    # pass   # --> sirve para cuando no deseamos poner codigo
# a empleado voy a agregarle su propios metodos y atributos (ya tiene heredados los de Persona)

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, profesion, salario): # lo mismo que Persona + los atributos del Empleado
        super().__init__(nombre, edad, nacionalidad)  # vas a heredar estos atributos de Persona (clase padre)
        self.profesion = profesion   # Atributos propios de la clase
        self.salario = salario       # Atributos propios de la clase
        
        # sobreescibo el metodo presentacion, cuando invoque empleado ejecutará este metodo
    def presentacion(self):
        print(f'Hola, soy {self.nombre}, tengo {self.edad} años y soy de {self.nacionalidad}, soy {self.profesion} y gano $ {self.salario}')


# Hasta aquí Persona es la SuperClase de Empleado y 
# Empleado es la subclase de Persona




personita = Persona('Patricia',48,'Argentina')
personita.presentacion()


# class Empleado(Persona):
    # pass   # --> sirve para cuando no deseamos poner codigo

# empleadito = Empleado('nombre',edad,'nacionalidad')  --> lo mismo que si pusiera Persona 
# ha heredado todo de persona, 

empleadita = Empleado('Patricia', 48, 'Argentina','Programadora','3000')
empleadita.presentacion()