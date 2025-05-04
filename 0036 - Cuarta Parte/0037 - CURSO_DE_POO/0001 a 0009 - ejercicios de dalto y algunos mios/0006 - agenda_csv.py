# Agenda en CVS
# Estructura de amigos = {
    # apellido
    # nombre
    # cuit
    # contacto
    # nacionalidad
    # profesion
# }

# para manejo de archivos cvs
import pandas as pd

# para manejo del sistema operativo (si existe el archivo de datos)
import os

# para poder trabajar con archivos csv
import csv

class Clientes:
    def __init__(self, apellido, nombre, dni, cuit, genero, fecha_nac, lugar_nac, domicilio, localidad, profesion, estado_civil):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.cuit = cuit
        self.genero = genero
        self.fecha_nac = fecha_nac
        self.lugar_nac = lugar_nac
        self.domicilio = domicilio
        self.localidad = localidad
        self.profesion = profesion
        self.estado_civil = estado_civil
        
    def agregar(self):
        # modificar clase
        self.apellido = input('Ingrese el apellido del cliente: ')
        self.nombre = input('Ingrese el nombre del cliente: ')
        self.dni = input('Ingrese el DNI del cliente: ')
        self.cuit = input('Ingrese el cuit o cuil del cliente: ')
        self.genero = input('Ingrese el género del cliente: ')
        self.fecha_nac = input('Ingrese la fecha de nacimiento del cliente: ')
        self.lugar_nac = input('Ingrese el lugar de nacimiento del cliente: ')
        self.domicilio = input('Ingrese el domicilio de residencia del cliente: ')
        self.localidad = input('Ingrese la localidad de residencia del cliente: ')
        self.profesion = input('Ingrese la profesión del cliente: ')
        self.estado_civil = input('Ingrese el estado civil del cliente: ')
        # cargo en variable el nombre del archivo
        agenda_cvs = 'agenda.cvs'
        # asigno las columnas (campos) que tendra como titulo
        # el archivo csv
        columnas_df = ['apellido','nombre','dni','cuit','genero','fecha_nac','lugar_nac', 'domicilio','localidad','profesion','estado_civil']
        # preguntar si el archivo agenda.cvs existe
        if not (os.path.exists(agenda_cvs)):
            # si no existe el archivo
            # configurar las columnas en el df (dataFrame)
            df = pd.DataFrame(columns=columnas_df)
            # crear el archivo
            df.to_csv(agenda_cvs, index=False)
            print(f'El archivo {agenda_cvs} fué creado con exito!')
        
        # si ya existe agrego la informacion proporcionada por 
        # el usuario
        
        # leo el archivo
        df = pd.read_csv(agenda_cvs)
        
        nueva_fila = {
            'apellido': self.apellido,
            'nombre': self.nombre,
            'dni': self.dni,
            'cuit': self.cuit,
            'genero': self.genero,
            'fecha_nac': self.fecha_nac,
            'lugar_nac': self.lugar_nac, 
            'domicilio': self.domicilio,
            'localidad': self.localidad,
            'profesion': self.profesion,
            'estado_civil': self.estado_civil            
            }
        # concateno el archivo + lo que se le agrega
        df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
        # ahora guardo el archivo
        df.to_csv(agenda_cvs, index=False)
        print('Cliente agregado exitosamente!')

    def listar(self):
        # cargar el archivo para su lectura
        with open('agenda.cvs') as agenda:
            # devuelve un iterable
            reader = csv.reader(agenda)
            # recorro el iterable con for
            titulo=[]
            for index, fila in enumerate(reader):
                if index == 0:
                    titulo = fila
                    # sale del bucle
                    break 
        
            # vuelvo al inicio del archivo csv
            agenda.seek(0)
        
            # cargo en reader nuevamente la agenda
            reader = csv.reader(agenda)
        
            # saltar la primera fila (titulo)
            next(reader)
        
            # recorro desde la fila 2 hasta el final
            for fila in reader:
                for index in range(len(fila)):
                    print(f'{titulo[index].capitalize()}: {fila[index].upper()}')
                print('\nFin de la fila\n\n')
        
    def borrar_por_dni(self, dni_a_borrar, columna = 'dni'):
        df = pd.read_csv('agenda.csv')
        
        # pregunto si exite el dato a borrar
        if dni_a_borrar in df[columna].values:
            # Guardar el DataFrame backup en el archivo CSV
            df.to_csv('agenda_backup_borrar.csv', index=False)
            # print(f'Antes de borrar {dni_a_borrar}:')
            # print(df)
            # Borrar la fila con el DNI '0' o '1'
            df = df[df[columna] != dni_a_borrar]
            # print(f'Después de borrar {dni_a_borrar}:')
            # print(df)
            # Guardar el DataFrame actualizado en el archivo CSV
            df.to_csv('agenda.csv', index=False)
            print(f'El dni {dni_a_borrar} se borró correctamente!')
        else:
            print(f'El dni {dni_a_borrar} NO existe!')
             
    def modificar_por_dni(self, dni_a_buscar, columna_a_modificar, nuevo_valor):
        
        campo=columna_a_modificar
        agenda = 'agenda.csv'
        # Verificar si el archivo existe
        if os.path.exists('agenda.csv'):
            # print('el archivo existe')
            
            # Leer el archivo CSV
            df = pd.read_csv('agenda.csv')
            
            # Verificar si el dni_a_buscar existe en la columna 'dni'
            if dni_a_buscar in df['dni'].values:
                
                # buscar el indice de la persona del dni seleccionado
                indice = df[df['dni'] == dni_a_buscar].index[0]
                
                # modificar el valor de la columna especificada
                df.at[indice,columna_a_modificar] = nuevo_valor
                
                # guardar el archivo CSV con los cambios
                df.to_csv(agenda, index=False)
                
                print(f'La columna {columna_a_modificar} ha sido modificada para el dni {dni_a_buscar}')
            else:
                print(f'No se encontró ningún registro con el dni {dni_a_buscar}.')
        else:
            print(f'El archivo {agenda} no existe!')

# genero una nueva instancia de la clase con todos los datos vacios
persona = Clientes('','','','','','','','','','','')
# print(f'El apellido es {persona.apellido}')
# persona.agregar()
# print(f'Luego de agregar el apellido es {persona.apellido}')
# persona.listar()
# persona.borrar_por_dni(0)
# persona.borrar_por_dni(1)
# persona.modificar_por_dni(3,'nombre', 'Juan Manuel Del Sagrado Corazón')

# def mostrar_menu():
#     print('Agenda de Clientes\n')
#     print('1. Nuevo Cliente')
#     print('2. Modificar Cliente')
#     print('3. Ver todos los Clientes')
#     print('4. Borrar un Cliente')
#     print('5. Salir')
#     opcion = int(input('Ingrese una opción válida: '))
#     return opcion

# def agregar_clientes_a_la_clase():
#     # el usuario carga el apellido
#     apellido = input('Ingrese el apellido del cliente: ')
#     # se instancia cliente que deviene de la clase Clientes
#     cliente = Clientes(apellido)
#     # retorno la instancia
#     return cliente





# def mostrar_cliente_de_la_clase(cliente):
#     # por parámetro cardo la instancia de Clientes
    
#     # muestro el apellido del cliente
#     print(f'El cliente es {cliente.apellido}')

# while True:
#     opcion = mostrar_menu()
#     print(type(opcion))
#     if opcion >= 5 or opcion < 1:
#         break
#     elif opcion == 1:
#         apellido = agregar_clientes_a_la_clase()
#     elif opcion == 2:
#         pass
#     elif opcion == 3:
#         mostrar_cliente_de_la_clase(apellido)
#     elif opcion == 4:
#         pass
        