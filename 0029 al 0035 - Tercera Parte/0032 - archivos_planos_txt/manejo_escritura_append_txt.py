# Escribir un archivo con append

ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt"
codificacion = 'UTF-8'
escritura = "a"  #--> permiso de escritura para el archivo (r, w, a)
# APPEND agrega texto al final del archivo
# si no encuentra el archivo lo crea....
                # (ruta, escritura, codificacion)

lista_de_lineas_txt = ['\nUsando Append\n','\nlinea uno\n', 'linea dos\n', 'linea tres\n']

with open(ruta, escritura, encoding=codificacion) as Archivo:
    # Archivo es como la variable archivo
    print('Archivo abierto optimamente y se agrega texto al final')
    print('Si el archivo no existe lo crea')
    # sobreescribiendo el archivo
    Archivo.write('\nNo sobreescribo todo el archivo sino que agrego lineas al final: ')
    # de una lista cargo el archivo y agrego al final las lineas, pero sin espacio
    # entre los elementos, con '\n' agrego un salto de linea
    Archivo.writelines(lista_de_lineas_txt)
# aca el archivo se cerro (fuera del with)