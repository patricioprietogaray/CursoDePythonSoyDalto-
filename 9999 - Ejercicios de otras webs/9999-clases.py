# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
    
#     def hablar(self):
#         print(f'Soy {self.nombre} y estoy hablando!!!')

# class Estudiante(Persona):
#     def __init__(self, nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.grado = grado
    
#     def estudiar(self):
#         print(f'Soy {self.nombre} y estudio en {self.grado}')

# gervacio = Persona('Gervacio', 175)
# gervacio.hablar()

# hector = Estudiante('Hector', 76, 8)
# hector.hablar()
# hector.estudiar()

class Persona:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
    
    def presentar(self):
        print(f'La persona {self.nombre} y dni {self.dni} se presenta')
    
    def caminar(self):
        print(f'La persona {self.nombre} está caminando')
    

class Empleado:
    def __init__(self, salario):
        self.salario = salario
    
    def trabajar(self):
        print(f'El empleado tiene un salario de ${self.salario}.')
        

class Deportista:
    def __init__(self, deporte):
        self.deporte = deporte
    
    def juegar(self):
        print(f'El deportista juega {self.deporte}')
    
    def correr(self):
        print(f'El deportista corre mucho.')

class Atareado(Persona, Empleado, Deportista):
    def __init__(self, dni, nombre, salario, deporte):
        Persona.__init__(self, dni, nombre)
        Empleado.__init__(self, salario)
        Deportista.__init__(self, deporte)
    
    def tiempo(self):
        print(f'El atareado {self.nombre} no tiene tiempo.')
        
    def actividades(self):
        print(f'Nombre: {self.nombre}\nDNI: {self.dni}\nSalario: {self.salario}\nDeporte: {self.deporte}')
        
    def atareadoPresenta(self):
        super().presentar()
    
    
    
    
print('Persona:')
gervacio = Persona(12345678, 'Gervacio Posadas')
gervacio.presentar()
gervacio.caminar()
print('\nEmpleado:')
fernando = Empleado(10000)
fernando.trabajar()
print('\nDeportista:')
rosa = Deportista('Hockey')
rosa.juegar()
print('\nPersona, Empleado y Deportista:')
miguel = Atareado(33222111, 'San Miguel de Tucumán', 2000, 'Futbol')
miguel.atareadoPresenta()
miguel.caminar()
miguel.trabajar()
miguel.juegar()
miguel.tiempo()
miguel.actividades()



        
        