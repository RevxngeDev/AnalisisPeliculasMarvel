import pandas as pd
from scipy import stats

# Leer el archivo CSV limpio
df = pd.read_csv("C:/Users/Camilo/Desktop/Marvel_Movies.csv")

# Ejemplo de prueba de hipótesis: prueba de normalidad de Shapiro-Wilk
hipotesis_resultados = {}
for columna in df.select_dtypes(include=['number']).columns:
    stat, p_value = stats.shapiro(df[columna])
    hipotesis_resultados[columna] = {'stat': stat, 'p_value': p_value}

# Mostrar resultados de la prueba de hipótesis por consola
for columna, resultados in hipotesis_resultados.items():
    print(f'Prueba de Shapiro-Wilk para {columna}:')
    print(f'Estadístico: {resultados["stat"]}, Valor p: {resultados["p_value"]}\n')
