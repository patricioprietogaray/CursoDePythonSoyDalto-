class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        return 'Hola, estoy hablando un poco!'
        

# ojo que Artista no tiene que heredar a persona, porque el algoritmo se confunde
# al generar la subclase entre personas y artista
class Artista:
    def __init__ (self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'
        
# ¿Se pueden heredar dos cosas???? se toma una u otra???
# Voy a crear una clase que sea un empleado y un artista

class EmpleadoArtista(Persona, Artista):
    # tengo que heredar todo lo de una persona y todo lo de un artista
    # persona nombre, edad, nacionalidad
    # artista habilidad
    # y como es empleado salario y empresa
    def __init__ (self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        # ¿Y ahora de que clase heredamos ??? 
        # super().__init__(self,)  
        # hay que hacer referencia directa a cada clase
        # heredo los atributos de persona
        Persona.__init__(self, nombre, edad, nacionalidad)
        # heredo los atributos de artista
        Artista.__init__(self, habilidad)
        # creo atributos de EmpleadoArtista
        self.salario = salario
        self.empresa = empresa
        
        # con super() siempre accedo a la clase padre
        # con self accedo al metodo propio
        
    def mostrar_habilidad(self):
        return 'La habilidad de Empleado Artista'
        
    def presentacion(self):
        # muestra la funcion propia
        # return self.mostrar_habilidad() # --> 'La habilidad de Empleado Artista' 
        
        # mostrar el método de la clase padre
        return super().mostrar_habilidad() # --> 'Mi habilidad es cantar'

ea = EmpleadoArtista('ART',15,'argentina','cantar', 100, 'Talent')
print(ea.presentacion())

# para saber si una clase es subclase de otra
herencia = issubclass(EmpleadoArtista, Artista)
print(f'la clase EmpleadoArtista es subclase de Artista: {herencia}')


#                      ¿hijo      padre?
herencia = issubclass(Artista, EmpleadoArtista)
print(f'la clase Artista es subclase de EmpleadoArtista: {herencia}')

#                   ¿ instancia, clase?
instancia = isinstance(ea,EmpleadoArtista)
print(f'\nla instancia ea es instancia de la clase EmpleadoArtista: {instancia}')

#                   ¿ instancia, superclase?
instancia = isinstance(ea,Artista)
print(f'la instancia ea es instancia de la clase Artista: {instancia}')


instancia = isinstance(ea,Persona)
print(f'la instancia ea es instancia de la clase Persona: {instancia}')

print('''
si porque 

Persona                 Artista
 |                         |
  --------------------------
             |
     EmpleadoArtista   -----------> ea (instancia)      
      ''')
# si porque 

# Persona                 Artista
#  |                         |
#   --------------------------
#              |
#      EmpleadoArtista

 

