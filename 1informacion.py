import pandas as pd

ruta_del_archivo = "C:/Users/Camilo/Desktop/Marvel_Movies.csv"

df = pd.read_csv(ruta_del_archivo)

num_observaciones = df.shape[0]
num_variables = df.shape[1]

tipos_de_datos = df.dtypes

valores_faltantes = df.isnull().sum()

for columna in df.columns:
    if pd.api.types.is_numeric_dtype(df[columna]):
        df[columna] = df[columna].fillna(df[columna].mean())
    else:
        df[columna] = df[columna].fillna('Desconocido')

print(f'Número de observaciones: {num_observaciones}')
print(f'Número de variables: {num_variables}\n')
print('Tipos de datos:')
print(tipos_de_datos)
print('\nValores faltantes antes de la limpieza:')
print(valores_faltantes)
print('\nValores faltantes después de la limpieza:')
print(df.isnull().sum())

print('\nDataFrame con valores faltantes llenados (primeras filas):')
print(df.head())
