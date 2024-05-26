import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV limpio
df = pd.read_csv("C:/Users/Camilo/Desktop/Marvel_Movies.csv")

# Crear histogramas con la función de distribución
for columna in df.select_dtypes(include=['number']).columns:
    plt.figure()
    sns.histplot(df[columna], kde=True)
    plt.title(f'Histograma y KDE de {columna}')
    plt.show()

# Crear boxplots
for columna in df.select_dtypes(include=['number']).columns:
    plt.figure()
    sns.boxplot(x=df[columna])
    plt.title(f'Boxplot de {columna}')
    plt.show()

# Crear diagramas de dispersión
columnas_numericas = df.select_dtypes(include=['number']).columns
for i in range(len(columnas_numericas)):
    for j in range(i + 1, len(columnas_numericas)):
        plt.figure()
        sns.scatterplot(x=df[columnas_numericas[i]], y=df[columnas_numericas[j]])
        plt.title(f'Diagrama de dispersión de {columnas_numericas[i]} vs {columnas_numericas[j]}')
        plt.show()
