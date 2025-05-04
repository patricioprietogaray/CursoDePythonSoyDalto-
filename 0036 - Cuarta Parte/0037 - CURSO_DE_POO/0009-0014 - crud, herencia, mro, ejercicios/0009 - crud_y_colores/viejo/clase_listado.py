import pandas as pd
import os

class Listados:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv



# class Listados:
#     def __init__(self, archivo_csv, atributos, total=True, parcial=False):
#         self.archivo_csv = archivo_csv
#         self.atributos = atributos
#         self.total = total
#         self.parcial = parcial
#         self.df = pd.DataFrame(columns=self.atributos)

#     def cargar_csv(self):
#         if not os.path.exists(self.archivo_csv): #  and os.stat(self.archivo_csv).st_size == 0:
#             self.df.to_csv(self.archivo_csv, index=False)
#             print(f'El archivo {self.archivo_csv} fué creado exitosamente.')
#         elif os.stat(self.archivo_csv).st_size == 0:
#             self.df = pd.DataFrame(columns=self.atributos)
#             self.df.to_csv(self.archivo_csv, index=False)
#             print(f'El archivo {self.archivo_csv} estaba vacío. Se ha creado uno nuevo.')
#         else:
#             try:
#                 print(f'Intentando cargar el archivo {self.archivo_csv}!')
#                 self.df = pd.read_csv(self.archivo_csv, encoding='utf-8')
#                 print(f'El archivo {self.archivo_csv} fué cargado exitosamente.')
#             except pd.errors.EmptyDataError:
#                 self.df = pd.DataFrame(columns=self.atributos)
#                 self.df.to_csv(self.archivo_csv, index=False)
#                 print(f'El archivo {self.archivo_csv} estaba vacío. Se ha creado uno nuevo.')
    
#     def mostrar_listado(self):
#         if self.total and not self.parcial:
#             if self.df.empty:
#                 print("La base de datos está vacía.")
#                 return
#             print('\n\nListado total de la base de datos\n')
#             print(f'Se encontraron {len(self.df)} registros.\n')
#             for index, row in self.df.iterrows():
#                 print(row.to_string(), end='\n\n')

            
#         # elif self.total == False and self.parcial == True:
#         #     print('\n\nListado parcial de la base de datos\n')
#         #     print('Ingrese la clave y su valor\n')
#         # else:
#         #     print('Error en la asignación de tareas)')
        
#         print('Presione una tecla para continuar...')
#         input()
            


