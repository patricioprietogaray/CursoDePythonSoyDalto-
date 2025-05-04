# manejo optimo de archivos txt que se usa actualmente

# archivo = open("/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt" ,encoding='UTF-8')

ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt"
codificacion = 'UTF-8'

with open(ruta, encoding=codificacion) as Archivo:
    # Archivo es como la variable archivo
    print('Archivo abierto optimamente')
    print(Archivo.read())

# aca el archivo se cerro (fuera del with)
