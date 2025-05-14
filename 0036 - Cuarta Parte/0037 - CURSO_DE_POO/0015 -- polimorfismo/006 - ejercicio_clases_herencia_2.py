# Medio: Empleado y Gerente

# Crea una clase Empleado con atributos nombre, salario y 
# un método mostrar_informacion() que imprima el nombre y salario.

# Crea una clase Gerente que herede de Empleado.

# Añade un atributo departamento al Gerente.

# Sobrescribe el método mostrar_informacion() en Gerente para que también 
# muestre el departamento.

# Añade un método asignar_tarea(empleado, tarea) 
# a Gerente que imprima "El gerente {nombre_gerente} 
# asignó la tarea '{tarea}' a {nombre_empleado}."
# Crea un Empleado y un Gerente, muestra su información y prueba el método asignar_tarea.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
    def mostrar_información(self):
        return f'Mi nombre es {self.nombre} y mi salario es ${self.salario}.'
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
        
    def mostrar_información(self):
        return f'\nGerencia:\nTrabajo en el departamento de {self.departamento}.\nMi nombre es {self.nombre} y mi salario es ${self.salario}.'
    
    def asignar_tarea(self, empleado, tarea):
        return f"El gerente {self.nombre} asignó la tarea '{tarea}' a {empleado.nombre}."

bacari = Gerente('Baccari',100000, 'ventas')
prieto = Empleado('Prieto', 20000)
print(prieto.mostrar_información())
print(bacari.mostrar_información())
print(bacari.asignar_tarea(prieto,'Cadete'))
