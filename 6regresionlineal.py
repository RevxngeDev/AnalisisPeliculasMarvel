import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Leer el archivo CSV limpio
df = pd.read_csv("C:/Users/Camilo/Desktop/Marvel_Movies.csv")

# Seleccionar dos características (cambiar 'feature1' y 'feature2' por los nombres reales de las columnas)
col1 = 'worldwide gross ($m)'
col2 = 'budget'

X = df[[col1]]
y = df[col2]

# Ajustar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Predicciones
y_pred = modelo.predict(X)

# Graficar la regresión
plt.figure()
sns.scatterplot(x=col1, y=col2, data=df)
plt.plot(df[col1], y_pred, color='red')
plt.title(f'Regresión Lineal entre {col1} y {col2}')
plt.show()

# Mostrar los resultados por consola
print(f'Coeficiente: {modelo.coef_[0]}')
print(f'Intercepto: {modelo.intercept_}')
