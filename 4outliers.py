import pandas as pd

# Leer el archivo CSV limpio
df = pd.read_csv("C:/Users/Camilo/Desktop/Marvel_Movies.csv")

# Calcular IQR y encontrar outliers
outliers = {}
for columna in df.select_dtypes(include=['number']).columns:
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    outliers[columna] = df[(df[columna] < (Q1 - 1.5 * IQR)) | (df[columna] > (Q3 + 1.5 * IQR))]

# Mostrar información de outliers por consola
for columna, outliers_df in outliers.items():
    print(f'Outliers en la columna {columna}:')
    print(outliers_df)
    print('\n')
