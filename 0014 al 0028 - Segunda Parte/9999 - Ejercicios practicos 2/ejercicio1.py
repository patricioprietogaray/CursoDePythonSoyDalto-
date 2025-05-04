# https://youtu.be/nKPbfIU442g?t=17719

# falto el profe y los pibes van a armar la clase
# pedir los nombres y la edad de los compañeros que vinieron a clases
# de los compañeros 1 sera el profesor y otro el asistente
# a) pedir el nombre y la edad de los compañeros que vinieron a clases y ordenar
#     los datos de mayor a menor
# b) el mayor de la clase es el profesor y el menor es el asistente
# ¿Quién es quien?

# funcion para obtener el profesor y el asistente segun la edad
def obtener_compañeros(cantidad):

    # creando una lista de los compañeros
    compañeros = []
    
    # manejando un for para pedir informacion de cada compañero
    for i in range(cantidad):
        nombre = input('Ingrese el nombre: ')
        edad = int(input('Ingrese la edad: '))
        compañero = (nombre, edad)
        # agregar informacion a la lista
        compañeros.append(compañero)
    # ordenar compañeros por la edad   key [1]
    # de mayor a menor
    compañeros.sort(key=lambda x: x[1], reverse=True)
    
    # definir asistente (ultimo menor) y profesor (1° mayor)
    profesor = compañeros[0][0]
    asistente = compañeros[-1][0]
    print(f'La lista de compañeros es: {compañeros}')
    
    # retornar una tupla
    return profesor, asistente

# desempaquetamos lo que retorna la funcion y mostramos el resultado
profe, asistente = obtener_compañeros(3)
print(f'El profesor es {profe} y el asistente es {asistente}')


# https://youtu.be/nKPbfIU442g?t=18101
