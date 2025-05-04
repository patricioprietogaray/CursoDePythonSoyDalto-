# https://youtu.be/nKPbfIU442g?t=22054

# Escribir un archivo
ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt"
codificacion = 'UTF-8'
escritura = "w"  #--> permiso de escritura para el archivo (r, w)
# si no encuentra el archivo lo crea....
                # (ruta, escritura, codificacion)

lista_de_lineas_txt = ['\nlinea uno\n', 'linea dos\n', 'linea tres\n']

with open(ruta, escritura, encoding=codificacion) as Archivo:
    # Archivo es como la variable archivo
    print('Archivo abierto optimamente')
    # sobreescribiendo el archivo
    Archivo.write('sobre escribo todo el archivo, si no lo encuentra se crea y se sobrescribe')
    # de una lista cargo el archivo y agrego al final las lineas, pero sin espacio
    # entre los elementos, con '\n' agrego un salto de linea
    Archivo.writelines(lista_de_lineas_txt)
# aca el archivo se cerro (fuera del with)
