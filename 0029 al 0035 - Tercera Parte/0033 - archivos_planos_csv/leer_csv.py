# https://youtu.be/nKPbfIU442g?t=22513

ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0033 - archivos_planos_csv/datos.csv"
codificacion = "UTF-8"
escritura = "r"


# # de esta manera lee el archivo como si se tratase de un txt
# with open(ruta, escritura, -1, encoding=codificacion) as Archivo:
#     print("Data leida correctamente!")
#     print(Archivo.read())
    

# # Utilizando la librería csv 
import csv
with open(ruta, escritura, encoding=codificacion) as Archivo:
    reader = csv.reader(Archivo)
    print(reader)  # --> <_csv.reader object at 0x71600df494d0>
    # reader es un iterable, como lo recorro? con un for
    for i in reader:
        print(i) # --> ['nombre', 'apellido', 'edad']   ['Patricio Sebastian', 'Prieto Garay', ' 48']  ['Maria de las Mercedes', ' "Rimoli Echarren"', ' 44']
        # print(i[0]) #  -> muestra la primera columna   nombre, patricio .., maria ..
        # print(i[1]) #  -> muestra la segunda columna   apellido, ... ,  ....
        # print(i[2]) # --> tercer columna : edad


# como con OPEN que no es lo óptimo y con WITH OPEN que Si es lo óptimo
# Lo mismo sucede con la libreria csv, pandas es lo optimo!


