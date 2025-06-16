# https://youtu.be/HtKqSJX7VoM?t=7858

# DECORADOR PROPERTY

# no confundir propiedades de atributos con las 
# propiedades de property
# solo son getters y setters....
# tambien deleters eliminar valores, metodos, etc
# usamos una clase ya creada

# class Persona:
#     def __init__(self, nombre, edad):
#         self.__nombre = nombre
#         self.__edad = edad
    
#     # acceder con getters y setters (concepto)
    
#     @property    
#     def get_nombre_propiedad(self):
#         return self.__nombre
    
#     def get_nombre_funcion(self):
#         return self.__nombre
    


# dalto = Persona('Lucas Dalto', 22)
# print(dalto.get_nombre_propiedad)
# print(dalto.get_nombre_funcion())


# ahora utilizo setters con property
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # acceder con getters y setters (concepto)
    
    @property    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter # --> funcion de la property .setter para modificar nombre
    def nombre(self, new_name): # --> se mantiene el mismo nombre de la funcion
        self.__nombre = new_name
    
    # @nombre.deleter
    # def nombre(self):
    #     del self.__nombre

    

dalto = Persona('Lucas Dalto', 22)
print(dalto.nombre)
dalto.nombre = 'Pepito'
print(dalto.nombre)

# si borro el atributo y deseo mostrarlo: error porque no existe
# del dalto.nombre # borro el atributo self.__nombre
# print(dalto.nombre) # --> AttributeError: 'Persona' object has no attribute '_Persona__nombre'


# https://youtu.be/HtKqSJX7VoM?t=8231

# si deseo borrar el atributo y no tengo un metodo de borrado: error porque no lo puedo borrar
# en caso de borrar el metodo deleter
del dalto.nombre #AttributeError: property 'nombre' of 'Persona' object has no deleter




print('hola')