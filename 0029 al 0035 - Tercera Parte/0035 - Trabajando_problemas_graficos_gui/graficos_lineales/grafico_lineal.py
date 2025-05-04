import pandas as pd

# libreria para visualizar los datos
import matplotlib.pyplot as plt

# libreria para armar gráficos estadísticos
import seaborn as sns

# leer el archivo
df = pd.read_csv('problemas_estomacales.csv')
# print(df)

# poner la fecha como lo puede leer bien sns  --> 2025-01-16 formato yyyy-mm-dd
# df['Fecha'] = pd.to_datetime(df['Fecha'], format='%m-%d', yearfirst=False).apply(lambda x: x.replace(year=2025))
# print(df)

# verificar las columnas disponibles
# print("Columnas del DataFrame: ",df.columns.tolist())
# A tener en cuenta Columnas del DataFrame:  ['Fecha', 'Flatos'] 


# # creando el grafico

# para que funcione:
# A tener en cuenta Columnas del DataFrame:  ['Fecha', 'Flatos'] 
# es distinto a Columnas del DataFrame:  ['Fecha', ' Flatos']
# en el archivo csv debe ponerse Fecha,Flatos y no Fecha, Flatos
sns.lineplot(x='Fecha', y='Flatos', data=df) #, marker='D')
# marker='o' son puntos por cada dato en el grafico

# deshabilito marker porque voy a marcar el punto maximo
# fecha 17 con 10 flatos
plt.plot("01-17", 10, "o")

# # mostrar el grafico
plt.show()

