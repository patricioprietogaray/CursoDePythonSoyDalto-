# atributos de una clase

# https://youtu.be/HtKqSJX7VoM?t=1445

# Los ATRIBUTOS son variables que pertenecen a una clase

# class Celular():
#     # defino los atributos estáticos
#     marca = "Samsung"
#     modelo = "S23"
#     camara = "48Mpx"

# # instancio la clase Celular()
# celu1 = Celular()

# print(celu1.marca)
# print(celu1.modelo) #devuelve S23

# # cambio el modelo de S23 a S45
# celu1.modelo = "S45"

# # muestro el modelo
# print(celu1.modelo) #devuelve S45


# cada vez que ejecuto el programa siempre el modelo es S23 y luego lo cambio a S45

# Para evitar lo anterior se utilizan los ATRIBUTOS DE INSTANCIA!!!
# Los atributos de instancia se definen cuando instanciamos una clase

# class Celular:
    # def __init__():  
    # # constructor de la clase
        # cada vez que se instancia la clase este constructor se ejecuta
        # autmáticamente.

    # al constructor se le pasa el parametro self (hace referencia a la propia clase)
    # luego se le pasa como parametros los datos que voy a modificar 
    # para adaptar los atributos de la clase a las necesidades.

# class Celular:
#     # funcion constructora
#     def __init__(self, marca, modelo, camara):
#         # definir las propiedades
#         # self hace referencia a la propia clase self.atributo es como decir
#         # Celular.atributo
#         self.marca = marca
#         self.modelo = modelo
#         # defino el atributo self.marca y le paso marca de los parametros
#         # no tiene nada que ver marca de los parametros con self.marca que es 
#         # un atributo (self.marca) son dos cosas distintas
#         self.camara = camara

# # no pasamos el parametro self, si todo lo que le sigue a self.
# #         (self, marca, modelo, camara)
# celu1 = Celular("Samsung","S23", "48MPx")
# # cuando instancio Celular se ejecuta el constructor de la clase y 
# # toma los parametros que le estoy pasando, luego creo el objeto celu1
# # que va a tener como atributos marca, modelo y camara en la cual
# # estarán cargados los datos pasados

# # muestro Samsung
# print(celu1.marca)

# class Botella:
#     def __init__(self, material, tapa, capacidad, altura, contenido):
#         self.material = material
#         self.tapa = tapa
#         self.capacidad = capacidad
#         self.altura = altura
#         self.contenido = contenido

# botella_manaos = Botella("Plástico","Una Tapa a Rosca", "3L", "56Cm", "Agua carbonatada + colorantes + saborizantes")
# botella_agua_bidon = Botella("Plástico","Tapón","10L", "78Cm", "Agua")

# print('Botella de Manaos')
# print(f'''La botella de manaos tiene las siguientes propiedades o atributos:
#      Su material es {botella_manaos.material}, su contenido es asegurado con {botella_manaos.tapa}
#      tiene una capacidad de {botella_manaos.capacidad} con una altura de {botella_manaos.altura}
#      y por ultimo contiene {botella_manaos.contenido}.
#      ''')

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
nombre_alumno = input("Ingrese el nombre del alumno: ")
nota_alumno = float(input(f"Ingrese la nota de {nombre_alumno}: "))
estudiante_1 = Estudiante(nombre_alumno, nota_alumno)
print(f'El alumno es: {estudiante_1.nombre}')
print(f'La nota del alumno es: {estudiante_1.nota}')
# estudiante_1.aprobado()

# https://youtu.be/HtKqSJX7VoM?t=1762
