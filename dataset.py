import pandas as pd

# Definir los nombres de las columnas
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

# Leer el archivo bezdekIris.data y almacenar en un dataframe
df = pd.read_csv("bezdekIris.data", header=None, names=column_names)

# Mostrar las primeras filas del dataframe
print(df.head())
