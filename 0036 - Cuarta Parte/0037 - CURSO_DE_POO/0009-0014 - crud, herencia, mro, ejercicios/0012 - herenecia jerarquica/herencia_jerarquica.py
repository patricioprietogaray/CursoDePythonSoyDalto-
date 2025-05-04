# herencia (inheritance)

# herencia jerarquica

                        # ************* #
                        #    Persona    #   (Padre o superclase)
                        # ************* #
    #  -------------------------|--------------------------------
    #  |                        |                               |
# *************** #      # ************** #            # *************** #
#    Estudiante   #      #      Jefe      #            #     Empleado    # (Hija o subclase)
# *************** #      # ************** #            # *************** #


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


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad): # lo mismo que Persona + los atributos del Empleado
        super().__init__(nombre, edad, nacionalidad)  # vas a heredar estos atributos de Persona (clase padre)
        self.notas = notas   # Atributos propios de la clase
        self.universidad = universidad       # Atributos propios de la clase
        
        # sobreescibo el metodo presentacion, cuando invoque empleado ejecutará este metodo
    def presentacion(self):
        print(f'Hola, soy {self.nombre}, tengo {self.edad} años y\nsoy de {self.nacionalidad}, estudio en la {self.universidad} y mis notas son {self.notas}')


class Jefe(Persona):
    def __init__(self, nombre, edad, nacionalidad, empresa, utilidades): # lo mismo que Persona + los atributos del Empleado
        super().__init__(nombre, edad, nacionalidad)  # vas a heredar estos atributos de Persona (clase padre)
        self.empresa = empresa   # Atributos propios de la clase
        self.utilidades = utilidades       # Atributos propios de la clase
        
        # sobreescibo el metodo presentacion, cuando invoque empleado ejecutará este metodo
    def presentacion(self):
        print(f'Hola, soy {self.nombre}, tengo {self.edad} años y\nsoy de {self.nacionalidad}, soy gerente en la {self.empresa} y mi utilidad es de ${self.utilidades}')

# Hasta aquí Persona es la SuperClase 
# Empleado, Estudiante y Jefe son subclases de Persona


personita = Persona('Patricia',48,'Argentina')
personita.presentacion()


# class Empleado(Persona):
    # pass   # --> sirve para cuando no deseamos poner codigo

# empleadito = Empleado('nombre',edad,'nacionalidad')  --> lo mismo que si pusiera Persona 
# ha heredado todo de persona, 

empleadita = Empleado('Patricia', 48, 'Argentina','Programadora','3000')
empleadita.presentacion()

estudiantita = Estudiante('Patricia', 48, 'Argentina', [8,9,10], 'UBA')
estudiantita.presentacion()

jefecito = Jefe('Patricio', 48, 'Argentina', 'Paso Cero', 10000)
jefecito.presentacion()