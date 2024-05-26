import pandas as pd

# Leer el archivo CSV limpio
df = pd.read_csv("C:/Users/Camilo/Desktop/Marvel_Movies.csv")

# Seleccionar solo las columnas numéricas
df_numerico = df.select_dtypes(include=['number'])

# Calcular estadísticas descriptivas
estadisticas_descriptivas = df_numerico.describe()

# Calcular correlaciones
correlaciones = df_numerico.corr()

# Calcular varianzas
varianzas = df_numerico.var()

# Mostrar estadísticas por consola
print('Estadísticas Descriptivas:')
print(estadisticas_descriptivas)
print('\nCorrelaciones:')
print(correlaciones)
print('\nVarianzas:')
print(varianzas)

