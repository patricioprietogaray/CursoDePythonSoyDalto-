# # creando el grafico
# ¿por que un grafico de barras?
# Los gráficos de barras son una herramienta 
# que se usa para comparar y resumir datos categóricos. 
# Sirven para representar valores mediante barras 
# rectangulares de longitud proporcional a los valores que representan. 
# Compara cantidades o frecuencias entre diferentes
# grupos o categorías.

import pandas as pd

# libreria para visualizar los datos
import matplotlib.pyplot as plt

# libreria para armar gráficos estadísticos
import seaborn as sns

# leer el archivo
df = pd.read_csv('fuente_de_ingresos.csv')

# verificar las columnas disponibles
print("Columnas del DataFrame: ",df.columns.tolist())
# A tener en cuenta Columnas del DataFrame:  ['Fuente', 'Ingresos'] 

# muestro en el terminal el total de los ingresos
print(f'Su ingreso total es de ${df["Ingresos"].sum()}')





# para que muestre el gráfico de barras:
sns.barplot(x='Fuente', y='Ingresos', data=df)
# # mostrar el grafico
plt.show()






