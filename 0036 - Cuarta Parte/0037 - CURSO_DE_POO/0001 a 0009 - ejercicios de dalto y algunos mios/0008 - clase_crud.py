# crud con pandas

import pandas as pd
import os

class Crud:
    def __init__(self, archivo, atributos):
        self.archivo = archivo
        self.atributos = atributos
        self.datos = []
        # no mezclar los tipos    
        # self.df = ''  un str 
        # cuando debe ser un DataFrame
        self.df = pd.DataFrame(columns=self.atributos)
        
    def carga_archivo_csv(self):
        # Intentar cargar el archivo
        if not os.path.exists(self.archivo) or os.stat(self.archivo).st_size == 0:
            # Si el archivo no existe o está vacío, crear el DataFrame con los encabezados
            # self.df = pd.DataFrame(columns=self.atributos)
            # si no hay else el archivo existe sobreescribe 
            # el primer registro
            self.df.to_csv(self.archivo, index=False)
            print(f'El archivo {self.archivo} fue creado con éxito!')
        else:
              # Si el archivo existe y tiene datos, cargarlo
            try:
                print(f'Intentando cargar el archivo {self.archivo}')
                self.df = pd.read_csv(self.archivo, encoding='utf-8')
                print(f'El archivo {self.archivo} fue cargado con éxito!')
                # imprime todo el DataFrame
                print(f'Contenido completo del DataFrame:\n{self.df}')
            except pd.errors.EmptyDataError:
                # En caso de que el archivo esté vacío (sin filas ni columnas)
                self.df = pd.DataFrame(columns=self.atributos)
                self.df.to_csv(self.archivo, index=False)
                print(f'El archivo {self.archivo} estaba vacío, se ha creado un nuevo archivo con los encabezados.')
    
    def ingreso_datos(self, id):
    #     id_a_buscar = int(input('Ingrese el id:'))
    #     print(f'Verificando que el {id_a_buscar} exista en la base de datos.')
    #     cantidad, datos = self.buscar_dato(id_a_buscar)
    #   if cantidad == 0:
        # id = int(input('Ingrese el id: '))
        nombre = input('Ingrese el nombre: ')
        telefono = input('Ingrese el telefono: ')
        
        opc = input('¿Confirma el ingreso de los datos? S-N: ')
        if opc.lower() == 's':
            self.datos.append(id)
            self.datos.append(nombre)
            self.datos.append(telefono)
            self.guardar_datos()
        else:
            print('Se canceló el ingreso de datos!')    
        
    def guardar_datos(self):
        nuevo_df = pd.DataFrame([self.datos], columns=self.atributos)
        self.df = pd.concat([self.df, nuevo_df], ignore_index=True)
        self.df.to_csv(self.archivo, index=False)
        print(f'Datos agregados a {self.archivo} exitosamente!.')
    
    def buscar_dato(self, buscar_id):
        # self.buscar_id = int(input('Ingrese el id a buscar: '))
        # print(f'Lo que estoy buscando: {self.buscar_id}')
        # print(f'df["id"] == buscar   -->   \n{self.df['id'] == self.buscar_id}')
        # print(self.df)
        resultado = self.df[self.df['id'] == buscar_id]
        
        # muestra el resultado
        # Resultado:    id  nombre  telefono
        # 0   4  cuatro      4444
        # indice(iloc[0])   id nomb telef
        

        # print(len(resultado))
        
        # if self.df[self.df["id"] == self.buscar_id]:
        #     print(self.df[self.df["id"] == self.buscar_id])
        # print('Busco un dato y devuelvo T-F si lo encontró')
        # print('Si encontro mostrar_datos(), si no pregunto si quiere agregar nuevo')

        # pregunto si el total de registros es 0 -> agrego datos
        # pregunto si el total de registros es 1 -> modifico
        # pregunto si el total de registros es 2 o mas -> advertencia
        # if len(resultado) == 0:
        #     self.ingreso_datos()
        #     correcto = int(input('¿Los datos ingresados son correctos? (S/N): '))
        #     if correcto.lower() == 's':
        #         self.guardar_datos()
        
        # devuelve un int de cuantos elementos encontró
        # y su resultado
        if len(resultado) == 0:
            return len(resultado), 'sin datos que mostrar'
        elif len(resultado) == 1:
            return len(resultado), resultado
        
        
        # return len(resultado), resultado
                
   
    
    
#     # def read_crud(self):
#     #     self.carga_archivo_csv()
#     #     self.buscar_datos_booleano()
#     #     self.mostrar_datos()

archivo = 'crud.csv'
atributos = ['id','nombre','telefono']

# ejecutar el programa
crud_nueva_clave_valor = Crud(archivo, atributos)
crud_nueva_clave_valor.carga_archivo_csv()
# cargo el dato que se quiere buscar
dato = int(input('Ingrese el id (numero) a buscar: '))
print(f'Verificando que el id {dato} (número) exista en la base de datos.')
# pregunto que hacer segun lo que haya en el dato
cantidad_registros, dato_registro = crud_nueva_clave_valor.buscar_dato(dato)
if cantidad_registros == 0 and dato_registro == 'sin datos que mostrar':
    print(f'La cantidad de registros encontrados es cero')
    crud_nueva_clave_valor.ingreso_datos(dato)
elif cantidad_registros == 1:
    registro_encontrado = dato_registro.iloc[0]
    opc = input(f'''¿Qué desea hacer con el id {dato}? 
                nombre: {registro_encontrado['nombre']};
                telefono: {registro_encontrado['telefono']}.
                ((E)ditar o (B)orrar): ''')
    if opc.lower() == 'e':
        print('edito el dato')
    elif opc.lower() == 'b':
        print('borro el dato')

# crud_nueva_clave_valor.ingreso_datos(dato)


# crud_nueva_clave_valor.ingreso_datos()
# crud_nueva_clave_valor.guardar_datos()

# # print('\n\n\tPresentacion del programa: \n')
# # crud_nueva_clave_valor.presentation_crud()
# # print('\n\tCrud: Alta de datos\n')
# # crud_nueva_clave_valor.create_crud()
# # print('\n\tcRud: Leer todos los datos\n')
# # crud_nueva_clave_valor.read_crud()
# # print('\nVariables:\n')
# # print(crud_nueva_clave_valor.df)



