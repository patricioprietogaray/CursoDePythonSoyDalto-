# Diagrama de Caja y Bigotes
# Los diagramas de Caja-Bigotes 
# (boxplots o box and whiskers) 
# son una presentación visual que describe 
# varias características importantes, 
# al mismo tiempo, tales como la dispersión y simetría.

# Para su realización se representan 
# los tres cuartiles y los valores mínimo y máximo de los datos, 
# sobre un rectángulo, alineado horizontal o verticalmente.

# Construcción:
# Comparar distribuciones
# Diagrama de Caja a través de Excel
# Construcción:
# Una gráfica de este tipo consiste en una caja rectangular, 
# donde los lados más largos muestran el recorrido intercuartílico. 
# Este rectángulo está dividido por un segmento vertical 
# que indica donde se posiciona la mediana y 
# por lo tanto su relación con los cuartiles primero y 
# tercero(recordemos que el segundo cuartil coincide con la mediana).
# Esta caja se ubica a escala sobre un segmento que 
# tiene como extremos los valores mínimo y máximo 
# de la variable. Las lineas que sobresalen de 
# la caja se llaman bigotes. 
# Estos bigotes tienen tienen un límite de prolongación, 
# de modo que cualquier dato o caso 
# que no se encuentre dentro de este rango es marcado 
# e identificado individualmente


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# cargo los datos
df = pd.read_csv('datos_barra_bigotes.csv')
# print(df)

# cargo el grafico
sns.boxplot(x='categoria', y='valor', data=df)

# muestro el grafico
plt.show()
