# Fácil: Estudiante

# Crea una clase Estudiante con 
# un atributo "privado" __calificacion (inicializado en 0).

# Crea un método get_calificacion() 
# para obtener el valor de __calificacion.

# Crea un método set_calificacion(nueva_calificacion) 
# que solo permita establecer la calificación 
# si está entre 0 y 10. 
# Si no, debe imprimir un mensaje de error y 
# no cambiar la calificación.

# Prueba creando un estudiante y usando los métodos 
# para obtener y establecer su calificación 
# (con valores válidos e inválidos).

class Estudiante:
    def __init__(self):
        self.__calificacion = 0.0 #atributo privado
    
    def get_calificacion(self):
        return self.__calificacion
    
    def set_calificacion(self, cali):
        if 0.0 <= cali <= 10.0:
            self.__calificacion = cali
            # print(f'{self.__calificacion}')
        else:
            return 'La calificación debe ser entre 0.0 y 10.0!'

estudiante1 = Estudiante()
print(f'\nMostrar la calificación del estudiante: {estudiante1.get_calificacion()}')
print('\nLa calificación del estudiante es 7.9')
estudiante1.set_calificacion(7.9)
print(f'\nMostrar la calificación del estudiante: {estudiante1.get_calificacion()}')

print('\nLa calificación del estudiante es 17.9')
estudiante1.set_calificacion(17.9)
print(f'\nMostrar la calificación del estudiante: {estudiante1.get_calificacion()}')
