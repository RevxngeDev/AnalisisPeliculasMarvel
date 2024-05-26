import pandas as pd

# Ruta del archivo CSV
ruta_del_archivo = "C:/Users/Camilo/Desktop/Marvel_Movies.csv"

# Leer el archivo CSV
df = pd.read_csv(ruta_del_archivo)

# Obtener número de observaciones y variables
num_observaciones = df.shape[0]
num_variables = df.shape[1]

# Obtener tipos de datos
tipos_de_datos = df.dtypes

# Contar valores faltantes
valores_faltantes = df.isnull().sum()

# Manejo de valores faltantes
# Llenar solo las columnas numéricas con la media
for columna in df.columns:
    if pd.api.types.is_numeric_dtype(df[columna]):
        df[columna] = df[columna].fillna(df[columna].mean())
    else:
        # Para columnas no numéricas, llenamos con un valor constante o podemos optar por eliminar
        df[columna] = df[columna].fillna('Desconocido')

# Mostrar información básica por consola
print(f'Número de observaciones: {num_observaciones}')
print(f'Número de variables: {num_variables}\n')
print('Tipos de datos:')
print(tipos_de_datos)
print('\nValores faltantes antes de la limpieza:')
print(valores_faltantes)
print('\nValores faltantes después de la limpieza:')
print(df.isnull().sum())

# Mostrar DataFrame con valores llenados (primeras filas)
print('\nDataFrame con valores faltantes llenados (primeras filas):')
print(df.head())