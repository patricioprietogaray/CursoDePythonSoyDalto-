ruta = "/home/patricio/Escritorio/CURSO PYTHON DALTO/0029 al ---- - Tercera Parte/0032 - archivos_planos/texto.txt"
codificacion = 'UTF-8'
escritura = "a"  #--> permiso de escritura para el archivo (r, w, a)
# APPEND agrega texto al final del archivo
# si no encuentra el archivo lo crea....
                # (ruta, escritura, codificacion)

lista_de_lineas_txt = ['Usando Append','linea uno', 'linea dos', 'linea tres']

with open(ruta, escritura, encoding=codificacion) as Archivo:
    Archivo.write('\n Utilizando un bucle for: \n')
    for a in range(len(lista_de_lineas_txt)):Archivo.write(f'Linea {a}: {lista_de_lineas_txt[a]}\n')
# aca el archivo se cerro (fuera del with)

# https://youtu.be/nKPbfIU442g?t=22451