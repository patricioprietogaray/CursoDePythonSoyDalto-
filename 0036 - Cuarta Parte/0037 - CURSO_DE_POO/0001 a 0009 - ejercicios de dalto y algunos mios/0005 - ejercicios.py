# https://youtu.be/HtKqSJX7VoM?t=2810

# ejercicios de todo lo visto hasta ahora

# Crear una clase Estudiante, que tenga los atributos 
# nombre, edad y grado.
# Además hay que agregar un método que se llame estudiar()
# y que imprima el mensaje: "El estudiante (nombre) está estudiando".
# Crear una instancia de esta clase y usar el método.
# Para esto hay que generar una interaccion con el usuario, o 
# sea que debe ser un requerimiento. 
# Se debe pedir los atributos e instanciar la clase creada.
# Al escribir estudiar (indistinto si es mayusculas o minusculas)
# usar el metodo estudiar.

# class Estudiante:
#     def __init__(self, nombre, edad, grado):
#         self.nombre = nombre
#         self.edad = edad
#         self.grado = grado
    
#     def estudiar(self):
#         print(f"El alumno {nombre} esta estudiando....")


# nombre = input("Ingrese el nombre del estudiante: ")
# edad = int(input("Ingrese la edad del estudiante: "))
# grado = int(input("Ingrese el grado que asiste el estudiante: "))

# estudiante = Estudiante(nombre, edad, grado)

# print(f'DATOS DEL ESTUDIANTE:\n\nNOMBRE DEL ESTUDIANTE: {estudiante.nombre}\nEDAD DEL ESTUDIANTE: {estudiante.edad}\nAÑO A QUE ASISTE EL ESTUDIANTE: {estudiante.grado}\n')


# while True:

# # con este input espera a que el usuario escriba una palabra
# # sin rotulos
#     estudiar = input()

# # si el usuario escribe estudiar no importa 
# # si es con mayúsculas o minúsculas lo toma igual 
# # porque se pasa todo a minúsculas
#     if estudiar.lower() == 'estudiar':
#         estudiante.estudiar()
    
#     if estudiar.lower() == 'q':
#         break



# # 

# agenda de amigos
# guardar los datos en un archivo cvs

import pandas as pd

class Amigos:
    def __init__(self, apellido, nombre, contacto):
        self.apellido = apellido
        self.nombre = nombre
        self.contacto = contacto
    
    def mostar_amigos(self):
        pass
    
    def guardar_amigos(self):
        pass
    
    def borrar_amigos(self):
        pass

    def modificar_amigo(self):
        pass
    

def mostrar_menu():
    print('AGENDA DE AMIGOS:')
    print('1. Nuevo amigo')
    print('2. Modificar amigo')
    print('3. Ver todos los amigos')
    print('4. Borrar amigo')
    print('5. Salir')
    opcion = int(input('Ingrese una opcion (1-5): '))
    return opcion


ruta = "0005-datos.csv"
codificacion = "UTF-8"
escritura = "a"
df = pd.read_csv(ruta)
print(type(df))

while True:
    opcion = mostrar_menu()
    if opcion == 1:
        print('Nuevo amigo')
        apellido = input('Ingrese el apellido: ')
        nombre = input('Ingrese el nombre: ')
        contacto = input('Ingrese el contacto: ')
        amigo = Amigos(apellido, nombre, contacto)
        opcion = input(f'¿Desea agregar a {apellido}, {nombre}: {contacto} (s/n)?')
        if opcion.lower() == 's':
            # si no existe el archivo
                # crearlo y agregar la primera linea
            # se existe
                # agregar el dato
            with open(ruta, 'w', encoding=codificacion) as arch:
                arch.writelines()
            
            print('Se agregó el contacto...')
        else:
            print('no hago nada')
        
    elif opcion == 2:
        print('Modificar amigo')
    elif opcion == 3:
        print('Ver todos los amigos')
    elif opcion == 4:
        print('Borrar amigo')
    elif opcion == 5:
        print('Saliendo del programa ... ')
        break
    else:
        print('Ingrese una opcion del 1 al 5')
    


