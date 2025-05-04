# Tenemos dos listas con nombre y apellido es decir 
# una tiene nombre y otra apellido.
# Tenemos que escribir los datos en un archivo de textos de forma 
# óptima con un for.

nombres = ['Pepe', 'Pepa', 'Pepita', 'Don Pepito']
apellidos = ['Argento','Pigg','Pistolera','Del Kiosco']

# ruta_absoluta = '/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0034 - Trabajando_con_archivos_problemas/problemas_txt_datos.txt'
ruta_relativa = 'problemas_txt_datos.txt'
codificacion = 'UTF-8'
escritura = 'w'

# with open(ruta,escritura,encoding=codificacion) as df:
#     for a in range(len(nombres)):
#         df.write(f'{nombres[a]} {apellidos[a]}\n')

# forma optima usando zip y con un for todo en la misma linea
with open(ruta_relativa,escritura) as arch:
    # escribo una linea entera en el archivo
    arch.writelines('Los datos son:\n\n')
    # optimizo
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n------------------\n') for n,a in zip(nombres, apellidos)]
    
    # # es lo mismo poner lo siguiente dentro de una lista []
    # for n,a in zip(nombres, apellidos):
    #     arch.writelines(f'Nombre: {n}\nApellido: {a}\n------------------\n')
    