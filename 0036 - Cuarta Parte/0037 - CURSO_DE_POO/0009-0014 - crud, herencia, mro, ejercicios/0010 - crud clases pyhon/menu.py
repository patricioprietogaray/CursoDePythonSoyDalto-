# from archivo import Archivo

# class Menu:
#     def __init__(self, ancho_en_caracteres, titulo, opciones):
#         self.ancho_en_caracteres = ancho_en_caracteres
#         self.titulo = titulo
#         self.opciones = opciones
#         self.eleccion = 0
    
#     def imprimir_linea(self, caracter, ancho_en_caracteres):
#         # primero el caracter y luego el ancho -> '.' * 4 -> ....
#         # print(ancho_en_caracteres * caracter)
#         print(caracter * ancho_en_caracteres)
    
#     def imprimir_titulo(self):
#         print(self.titulo.center(self.ancho_en_caracteres))
    
    
        
#     def imprimir_menu(self):
#         manejo_archivo = Archivo('crud.csv')
#         # manejo_archivo.leer_archivo()
#         while True:
#             self.imprimir_linea('*', self.ancho_en_caracteres)
#             self.imprimir_titulo()
#             self.imprimir_linea('*', self.ancho_en_caracteres)
#             for opc in self.opciones:
#                 print(opc.center(self.ancho_en_caracteres))
#             self.imprimir_linea('*', self.ancho_en_caracteres)
#             try:
#                 self.eleccion = int(input('Ingrese una opcion (0 al 4): '))
#                 # esta mal NO HACER ASI
#                 # if self.eleccion > 4:
#                 #     break
#                 # elif self.eleccion == 1:
#                 #     manejo_archivo.crear()
#                 # elif self.eleccion == 2:
#                 #     manejo_archivo.leer()
#                 # elif self.eleccion == 3:
#                 #     manejo_archivo.actualizar()
#                 # elif self.eleccion == 4:
#                 #     manejo_archivo.borrar()
#                 # else:
#                 #     print('Sale del sistema!')
                
                
#                 if self.eleccion == 0:
#                     print('🚪Saliendo del sistema!')
#                     break
#                 # ESTO ES LO CORRECTO ATENTI CON EL IF
#                 if 1 <= self.eleccion <= 4:
#                     # eleccion mayor o igual a 1 y 
#                     # eleccion menor o igual a 4
#                     if self.eleccion == 1:
#                         manejo_archivo.crear()
#                     elif self.eleccion == 2:
#                         manejo_archivo.leer()
#                     elif self.eleccion == 3:
#                         manejo_archivo.actualizar()
#                     elif self.eleccion == 4:
#                         manejo_archivo.borrar()
#                     else:
#                         print('Debe seleccionar una opción entre el 0 y el 4!')
                    
#             except ValueError:
#                 print('Debe seleccionar una opción válida (numeros del 0 al 4)!\n')
                
    
# 📦 Importamos la clase Archivo desde archivo.py
from archivo import Archivo

class Menu:
    def __init__(self, ancho_en_caracteres, titulo, opciones):
        # 📐 Ancho total del menú en la terminal
        self.ancho_en_caracteres = ancho_en_caracteres
        # 🏷️ Título del menú (ej: 'CRUD')
        self.titulo = titulo
        # 📋 Lista de opciones del menú
        self.opciones = opciones
        # 🔢 Almacena la opción elegida por el usuario
        self.eleccion = 0

    def imprimir_linea(self, caracter, ancho_en_caracteres):
        # 📏 Imprime una línea horizontal con un carácter repetido
        print(caracter * ancho_en_caracteres)

    def imprimir_titulo(self):
        # 🧷 Centra el título del menú en el ancho dado
        print(self.titulo.center(self.ancho_en_caracteres))

    def imprimir_menu(self):
        # 📂 Instancia del manejador de archivos CSV
        manejo_archivo = Archivo('crud.csv')

        # 🔁 Bucle principal del menú
        while True:
            # 🖼️ Dibuja el marco del menú
            self.imprimir_linea('*', self.ancho_en_caracteres)
            self.imprimir_titulo()
            self.imprimir_linea('*', self.ancho_en_caracteres)

            # 📝 Imprime las opciones del menú, centradas
            for opc in self.opciones:
                print(opc.center(self.ancho_en_caracteres))
            self.imprimir_linea('*', self.ancho_en_caracteres)

            try:
                # 🎮 Captura la elección del usuario
                self.eleccion = int(input('🔽 Ingrese una opción (0 al 4): '))

                # 🚪 Salir del sistema
                if self.eleccion == 0:
                    print('🚪 ¡Saliendo del sistema! Hasta la próxima. 👋')
                    break

                # ✅ Validación de elección correcta
                if 1 <= self.eleccion <= 4:
                    if self.eleccion == 1:
                        print('✍️ Opción: Crear')
                        manejo_archivo.crear()
                    elif self.eleccion == 2:
                        print('📄 Opción: Leer')
                        manejo_archivo.leer()
                    elif self.eleccion == 3:
                        print('✏️ Opción: Actualizar')
                        manejo_archivo.actualizar()
                    elif self.eleccion == 4:
                        print('🗑️ Opción: Borrar')
                        manejo_archivo.borrar()
                else:
                    print('⚠️ Debe seleccionar una opción entre 0 y 4.')
            except ValueError:
                print('❌ Entrada inválida: debe ingresar un número del 0 al 4.\n')
