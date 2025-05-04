import pandas as pd

class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.df = pd.DataFrame()
        self.leer_archivo()
        
        
    
    def crear(self):
        while True:
            print('✍️ Crear un nuevo registro\n')
            try:
                nuevo_id = int(input('🔢 Ingrese un número de ID: '))
                
                # Validar que el nombre no esté vacío
                while True:
                    # eliminar los espacios vacios despues del nombre
                    nuevo_nombre = input('🧾 Ingrese el nombre: ').strip()
                    if nuevo_nombre == '':
                        print('⚠️ El nombre no puede estar vacío. Intente de nuevo.')
                    else:
                        break

                nuevo_registro = pd.DataFrame([{
                    'id': nuevo_id,
                    'nombre': nuevo_nombre
                }]) 
                self.df = pd.concat([self.df, nuevo_registro])
                self.df.to_csv(self.nombre_archivo, index=False)
                print('✅ Registro agregado con éxito')
            except ValueError:
                print('❌ ID inválido, debe ser un número.')
            
            continuar = input('🔁 ¿Desea agregar otro registro? (S/N): ').lower()
            if continuar != 's':
                break
    
    
    def leer(self):
        print('📄 Leer los registros\n')
        try:
            print(self.df.to_string(index=False))
        except FileNotFoundError:
            print(f'❌ No se encontró el archivo {self.nombre_archivo}.')
        
        
    
    # def actualizar(self):
    #     print('✏️ Actualizar un registro')
        
    #     try:
    #         id = int(input('🔢 Ingrese un ID para actualizar: '))
    #         resultado = self.df[self.df['id'] == id]
    #         # print(resultado) muestra toda la lista que coincide con id
        
    #         if resultado.empty:
    #             print(f'❌ No se encontró ningún registro con id {id}')
    #             # salir del def
    #             return
        
    #         # verificar que el id no se repita
    #         if len(resultado) > 1:
    #             print(f'⚠️ Se encontraron varios registros con ID {id}:\n')
    #             # recorro el resultado y pregunto que indice va a actualizar
                
    #             # Crear una lista de los índices reales
    #             indices_reales = resultado.index.tolist()
                
                
                
                
    #             for idx, fila in resultado.iterrows():
    #                 print(f"[{idx}] → id: {fila['id']} | nombre: {fila['nombre']}")
    #             seleccion = int(input('🔎 Ingrese el índice del registro a actualizar: '))
    #             if seleccion not in resultado.index:
    #                 print('❌ Índice inválido')
    #                 return
    #             actual = self.df.loc[seleccion, 'nombre']
    #             nuevo_nombre = input(f'✏️ Nombre actual: {actual} → Ingrese el nuevo nombre: ').strip()
    #             self.df.loc[seleccion, 'nombre'] = nuevo_nombre
    #         else:
    #             nombre_anterior = resultado['nombre'].iloc[0]
    #             nuevo_nombre = input(f'✏️ Nombre actual: {nombre_anterior} → Ingrese el nuevo nombre: ').strip()
    #             self.df.loc[self.df['id'] == id, 'nombre'] = nuevo_nombre

    #         self.df.to_csv(self.nombre_archivo, index=False)
    #         print('✅ Registro actualizado con éxito')
    #     except ValueError:
    #         print('❌ Debe ingresar un número válido.')
        
    def actualizar(self):
        print('✏️ Actualizar un registro')
        
        try:
            # Solicitar ID a actualizar
            id = int(input('🔢 Ingrese un ID para actualizar: '))
            resultado = self.df[self.df['id'] == id]

            if resultado.empty:
                print(f'❌ No se encontró ningún registro con id {id}')
                return

            # Si hay más de un registro con el mismo ID
            if len(resultado) > 1:
                print(f'⚠️ Se encontraron varios registros con ID {id}:\n')

                # Obtenemos los índices reales del DataFrame original
                indices_reales = resultado.index.tolist()

                # Mostramos los registros con un índice virtual enumerado
                for i, idx in enumerate(indices_reales):
                    nombre = self.df.loc[idx, 'nombre']
                    print(f"[{i}] → id: {id} | nombre: {nombre}")

                # Selección del usuario
                while True:
                    try:
                        seleccion = int(input('🔎 Ingrese el número [ ] del registro a actualizar: '))
                        if seleccion < 0 or seleccion >= len(indices_reales):
                            print('❌ Número fuera de rango. Intente de nuevo.')
                            continue

                        idx_real = indices_reales[seleccion]
                        actual = self.df.loc[idx_real, 'nombre']

                        nuevo_nombre = input(f'✏️ Nombre actual: {actual} → Ingrese el nuevo nombre: ').strip()
                        if nuevo_nombre == '':
                            print('⚠️ El nuevo nombre no puede estar vacío.')
                            continue

                        self.df.loc[idx_real, 'nombre'] = nuevo_nombre
                        break
                    except ValueError:
                        print('❌ Debe ingresar un número válido.')

            else:
                # Solo hay un registro con ese ID
                nombre_anterior = resultado['nombre'].iloc[0]
                nuevo_nombre = input(f'✏️ Nombre actual: {nombre_anterior} → Ingrese el nuevo nombre: ').strip()
                if nuevo_nombre == '':
                    print('⚠️ El nuevo nombre no puede estar vacío.')
                    return
            
            self.df.loc[self.df['id'] == id, 'nombre'] = nuevo_nombre

            # Guardar cambios
            self.df.to_csv(self.nombre_archivo, index=False)
            print('✅ Registro actualizado con éxito')
        
        except ValueError:
            print('❌ Debe ingresar un número válido.')

    
    # def borrar(self):
    #     print('Borrar un registro')
    #     try:
    #         id = int(input('Ingrese un id para ser borrado: '))
    #         resultado = self.df[self.df['id'] == id]
    #         # print(resultado) # muestra toda la lista que coincide con id
            
    #         # buscar si existe el id
    #         if resultado.empty:
    #             print(f'El id {id} no existe!')
    #             return
            
    #         # verificar si hay más de un registro con el id buscado
    #         cantidad = len(resultado)
    #         if cantidad > 1:
    #             print(f'⚠️ Atención: Se encontraron {cantidad} registros con el mismo id {id}.\n')
    #             confirmar = input('¿Desea eliminar TODOS estos registros? (S/N): ').lower()
    #             if confirmar != 's':
    #                 print('Operación cancelada')
    #                 return            
    #         else:
    #             # el id existe
    #             # mostrar el registro
    #             print(f'Se encontró el siguiente registro:\n{resultado.to_string(index=False)}')
    #             # borrarlo = input(f'\n{resultado.to_string(index=False)}\n¿Desea borrarlo (S/N): ')
    #             # esta seguro de borrarlo?
    #             #       SI -> eliminar del DataFrame
    #             confirmar = input('¿Está seguro que desea borrarlo? (S/N): ').lower()
    #             if confirmar != 's':
    #                 print('Operación cancelada.')
    #                 return
                
    #         # 🔥 Esta línea debe ejecutarse en ambos casos si hay confirmación
    #         # cargo a todos los registros del DataFrame 
    #         # menos el id seleccionado a ser borrado
    #         self.df = self.df[self.df['id'] != id]
    #         # guardo el DataFrame al cvs
    #         self.df.to_csv(self.nombre_archivo, index=False)
    #         print(f'El registro con id {id} eliminado con éxito!')

    #     except ValueError:
    #         print('Debe ingresar un número válido para el ID.')
    
    def borrar(self):
        print('🗑️ Borrar un registro')
        try:
            id = int(input('🔢 Ingrese el ID del registro a borrar: '))
            resultado = self.df[self.df['id'] == id]

            if resultado.empty:
                print(f'❌ El ID {id} no existe.')
                return

            if len(resultado) > 1:
                print(f'⚠️ Se encontraron múltiples registros con ID {id}:')
                for idx, fila in resultado.iterrows():
                    print(f"[{idx}] → id: {fila['id']} | nombre: {fila['nombre']}")
                seleccion = int(input('🧠 Ingrese el número [ ] del registro a eliminar: '))
                if seleccion in resultado.index:
                    self.df = self.df.drop(index=seleccion)
                    print('✅ Registro eliminado con éxito.')
                else:
                    print('❌ Índice inválido.')
            else:
                print(f'📌 Registro encontrado:\n{resultado.to_string(index=False)}')
                confirmar = input('❓ ¿Confirmar borrado? (S/N): ').lower()
                if confirmar == 's':
                    self.df = self.df[self.df['id'] != id]
                    print('✅ Registro eliminado.')
                else:
                    print('❌ Operación cancelada.')

            self.df.to_csv(self.nombre_archivo, index=False)
        except ValueError:
            print('❌ ID inválido.')
            
            
    
    # def leer_archivo(self):
    #     print(f'Leer todo el archivo {self.nombre_archivo}')
    #     atributos_df = ['id','nombre']
    #     # leer el archivo si existe
    #     try:
    #         self.df = pd.read_csv(self.nombre_archivo)
    #         print(f'El archivo {self.nombre_archivo} fue leido con éxito')
    #     except FileNotFoundError:
    #         self.df = pd.DataFrame(columns=atributos_df)
    #         self.df.to_csv(self.nombre_archivo, index=False)
    #         print(f'El archivo {self.nombre_archivo} fue creado con éxito!')

    def leer_archivo(self):
        print(f'📂 Leyendo el archivo {self.nombre_archivo}')
        atributos_df = ['id', 'nombre']
        try:
            self.df = pd.read_csv(self.nombre_archivo)
            print(f'✅ Archivo {self.nombre_archivo} leído con éxito')
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=atributos_df)
            self.df.to_csv(self.nombre_archivo, index=False)
            print(f'🆕 Archivo {self.nombre_archivo} creado con éxito')
