# Complejo: Sistema de ProcesadorDeArchivos

## Crea una clase base ProcesadorDeArchivos con un método procesar(contenido) 
## que debe ser implementado por las subclases (puede usar raise NotImplementedError).

## Crea clases derivadas: ProcesadorTexto, ProcesadorCSV y ProcesadorJSON.

## ProcesadorTexto: el método procesar(contenido_texto) 
## contará el número de palabras en el contenido_texto y 
## devolverá "Texto procesado: {numero_palabras} palabras."
# ProcesadorCSV: el método procesar(contenido_csv) 
# (asume que contenido_csv es una lista de listas, 
# donde la primera es el encabezado) 
# contará el número de filas de datos 
# (excluyendo el encabezado) y 
# devolverá "CSV procesado: {numero_filas_datos} filas de datos."

# ProcesadorJSON: el método procesar(contenido_json) 
# (asume que contenido_json es un diccionario) 
# contará el número de claves de primer nivel 
# y devolverá "JSON procesado: {numero_claves} claves principales."
# Crea una función procesar_varios_archivos(lista_procesadores, lista_contenidos) que itere sobre una lista de procesadores y sus respectivos contenidos, llamando al método procesar de cada uno.
# Crea instancias de cada procesador y datos de ejemplo para cada tipo de archivo, luego prueba procesar_varios_archivos.
import json

class ProcesadorDeArchivos:
    def procesar(self,contenido):
        raise NotImplementedError(f'Procesar el contenido ({contenido}) en las clases hijas')


class ProcesadorTexto(ProcesadorDeArchivos):
    def procesar(self,contenido):
        contar_palabras = contenido.split(' ')
        return f'Procesando el contenido: [{contenido}] la frase tiene {len(contar_palabras)} palabras.'
    
class ProcesadorCSV(ProcesadorDeArchivos):
    def procesar(self, contenido):
        contar_lineas = len(contenido)-1
        return f'Procesando el contenido: [{contenido}] el archivo cvs tiene {contar_lineas} lineas de datos.'
        
# class ProcesadorJSON(ProcesadorDeArchivos):
#     def procesar(self, contenido):
#         try:
#             # datos = json.loads(contenido)
#             # utilizo el json puro (una lista), no se lee porque no es un archivo
#             # print(type(contenido))
#             # return contenido
#             numero_claves = len(contenido)
#             return f'JSON procesado: {numero_claves} claves principales.'
#         except json.JSONDecodeError as e:
#             print(f'Error al decodificar la cadena JSON: {e}')

class ProcesadorJSON(ProcesadorDeArchivos):
    def procesar(self, contenido):
        if isinstance(contenido, dict):
            numero_claves = len(contenido)
            return f'JSON procesado: {numero_claves} claves principales.'
        elif isinstance(contenido, list):
            # Si el "JSON" es una lista de objetos, contamos la cantidad de elementos
            return f'JSON procesado: {len(contenido)} elementos.'
        else:
            return 'Error: El contenido JSON no es un diccionario ni una lista.'



mensaje = 'Hola Pepe tenes 48 años y vos María tenes 40 años.'
texto = ProcesadorTexto()
print(texto.procesar(mensaje))

archivo_cvs = [
    ['nombre','edad'],
    ['pepe', 48],
    ['maria', 40]
]
cvs = ProcesadorCSV()
print(cvs.procesar(archivo_cvs))

# json puro
archivo_json = [
    {
        'nombre':'pepe',
        'edad':48
    },
    {
        'nombre':'maria',
        'edad':40
    }
]

JSon = ProcesadorJSON()
print(JSon.procesar(archivo_json))