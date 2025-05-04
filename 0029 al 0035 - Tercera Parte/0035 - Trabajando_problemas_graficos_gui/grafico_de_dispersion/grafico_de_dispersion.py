# # creando el grafico
# ¿por que un grafico de dispersión? 
# Los gráficos de dispersión, también llamados 
# diagramas de dispersión o scatter plots, 
# sirven para mostrar la relación entre dos variables numéricas

# Usos 
# Identificar la intensidad de la relación entre dos variables
# Mostrar la fuerza de la relación lineal entre dos variables
# Visualizar valores extremos en los conjuntos de datos
# Mostrar patrones en grandes conjuntos de datos
# Comparar grandes cantidades de puntos de datos


# Los gráficos de dispersión permiten responder 
# preguntas sobre los datos, como, por ejemplo: 
# ¿cuál es la relación entre dos variables? 
# ¿Cómo se distribuyen los datos? 
# ¿Dónde están los valores atípicos?

import pandas as pd

# libreria para visualizar los datos
import matplotlib.pyplot as plt

# libreria para armar gráficos estadísticos
import seaborn as sns

# leer el archivo
df = pd.read_csv('datos_dispersion.csv')

# verificar las columnas disponibles
print("Columnas del DataFrame: ",df.columns.tolist())
# A tener en cuenta Columnas del DataFrame:  ['tiempo', 'dinero'] 

#  para que muestre el gráfico de dispersion:
sns.scatterplot(x='tiempo', y='dinero', data=df)

# # mostrar el grafico por pantalla
plt.show()
