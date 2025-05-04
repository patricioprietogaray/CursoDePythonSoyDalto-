import pandas as pd
import re
from datetime import datetime
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
        
    # validar que los datos ingresados cumplan
    # con el tipo de dato
        
    def validar_dni(self, dni):
        # el dni debe ser un numero de 8 digitos
        return dni.isdigit() and (len(dni) > 6 and len(dni) <= 8)

    def validar_cuit(self, cuit):
        # el cuit debe tener 11 digitos
        return cuit.isdigit() and len(cuit) == 11
    
    def validar_genero(self, genero):
        # el género debe ser M,F o X
        return genero in ['M', 'F', 'X']
    
    def validar_fecha_nac(self, fecha_nac):
        # validar que la fecha esté en formato
        # DD-MM-AAAA
        try:
            # convierte una cadena en fecha
            datetime.strptime(fecha_nac, "%d-%m-%Y")
            return True
        except ValueError:
            return False
    
    def validar_texto_no_vacio(self, texto):
        # verificar que el texto no esté vacío
        return bool(texto.strip())
        
    def agregar(self):
        # Solicitar datos al usuario
        
        # para validar el apellido
        while True:
            self.apellido = input('Ingrese el apellido del cliente: ').upper()
            if not self.validar_texto_no_vacio(self.apellido):
                print('El apellido no puede estar vacío. Intente nuevamente!\n')
                continue
            break
        
        # para validar el nombre
        while True:
            self.nombre = input('Ingrese el nombre del cliente: ').upper()
            if not self.validar_texto_no_vacio(self.nombre):
                print('El nombre no puede estar vacío. Intente nuevamente!\n')
                continue
            break
        
        # pedir el dni numero mayor a 7 digitos
        while True:
            self.dni = input('Ingrese el DNI del cliente: ')
            if not self.validar_dni(self.dni):
                print('El dni debe tener 7 u 8 dígitos.\n')
                continue
            break
        
        while True:
            self.cuit = input('Ingrese el cuit o cuil del cliente: ')
            if not self.validar_cuit(self.cuit):
                print('El cuit debe tener 11 dígitos.\n')
                continue
            break
        
        while True:
            self.genero = input('Ingrese el género del cliente (M-F-X): ').upper()
            if not self.validar_genero(self.genero):
                print('El género debe ser M, F o X. Intente nuevamente!\n')
                continue
            break
        
        while True:
            self.fecha_nac = input('Ingrese la fecha de nacimiento del cliente (DD-MM-AAAA): ')
            if not self.validar_fecha_nac(self.fecha_nac):
                print('La fecha de nacimiento debe tener el formato DD-MM-AAAA. Intente nuevamente.')
                continue
            break
        
        while True:
            self.lugar_nac = input('Ingrese el lugar de nacimiento del cliente (Localidad - Provincia): ')
            if not self.validar_texto_no_vacio(self.lugar_nac):
                print("El lugar de nacimiento no puede estar vacío. Intente nuevamente.")
                continue
            break
        
        while True:
            self.domicilio = input('Ingrese el domicilio de residencia del cliente: ')
            if not self.validar_texto_no_vacio(self.domicilio):
                print("El domicilio no puede estar vacío. Intente nuevamente.")
                continue
            break
        
        while True:
            self.localidad = input('Ingrese la localidad de residencia del cliente: ')
            if not self.validar_texto_no_vacio(self.localidad):
                print("La localidad no puede estar vacío. Intente nuevamente.")
                continue
            break
        
        while True:
            self.profesion = input('Ingrese la profesión del cliente: ')
            if not self.validar_texto_no_vacio(self.profesion):
                print("La profesión no puede estar vacío. Intente nuevamente.")
                continue
            break
        
        while True:
            self.estado_civil = input('Ingrese el estado civil del cliente: ')
            if not self.validar_texto_no_vacio(self.estado_civil):
                print("El estado civil no puede estar vacío. Intente nuevamente.")
                continue
            break
        
        
        
        

        # Cargar archivo CSV o crear uno nuevo
        agenda_cvs = 'agenda.csv'
        columnas_df = ['apellido', 'nombre', 'dni', 'cuit', 'genero', 'fecha_nac', 'lugar_nac', 'domicilio', 'localidad', 'profesion', 'estado_civil']
        
        # Leer el archivo CSV, si existe
        try:
            df = pd.read_csv(agenda_cvs)
        except FileNotFoundError:
            df = pd.DataFrame(columns=columnas_df)
            print(f'El archivo {agenda_cvs} fue creado con éxito!')
        
        # Crear nueva fila
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
        
        # Agregar la nueva fila al DataFrame
        df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
        
        # Guardar el archivo CSV con los cambios
        df.to_csv(agenda_cvs, index=False)
        print('Cliente agregado exitosamente!')

    def listar(self):
        # Leer el archivo CSV
        try:
            df = pd.read_csv('agenda.csv')
            print(df.to_string(index=False))  # Mostrar todo el contenido del DataFrame
        except FileNotFoundError:
            print('No se encontró el archivo agenda.csv.')

    def borrar_por_dni(self, dni_a_borrar):
        try:
            df = pd.read_csv('agenda.csv')
            
            # Verificar si el DNI está en el DataFrame
            if dni_a_borrar in df['dni'].values:
                # Eliminar la fila con el DNI especificado
                df = df[df['dni'] != dni_a_borrar]
                df.to_csv('agenda.csv', index=False)
                print(f'El cliente con DNI {dni_a_borrar} fue eliminado correctamente.')
            else:
                print(f'No se encontró el cliente con DNI {dni_a_borrar}.')
        except FileNotFoundError:
            print('No se encontró el archivo agenda.csv.')

    def modificar_por_dni(self, dni_a_buscar, columna_a_modificar, nuevo_valor):
        try:
            df = pd.read_csv('agenda.csv')
            
            # Verificar si el DNI está en el DataFrame
            if dni_a_buscar in df['dni'].values:
                # Buscar la fila correspondiente al DNI y modificar la columna
                df.loc[df['dni'] == dni_a_buscar, columna_a_modificar] = nuevo_valor
                df.to_csv('agenda.csv', index=False)
                print(f'El cliente con DNI {dni_a_buscar} ha sido modificado correctamente en la columna {columna_a_modificar}.')
            else:
                print(f'No se encontró el cliente con DNI {dni_a_buscar}.')
        except FileNotFoundError:
            print('No se encontró el archivo agenda.csv.')

# Crear una nueva instancia de la clase Clientes
persona = Clientes('','','','','','','','','','','')

# Ejemplo de uso:
persona.agregar()  # Para agregar un cliente
# persona.listar()   # Para listar todos los clientes

# persona.modificar_por_dni('3', 'nombre', 'Juan')  # Para modificar el nombre de un cliente

# persona.borrar_por_dni('3')  # Para borrar un cliente por DNI
