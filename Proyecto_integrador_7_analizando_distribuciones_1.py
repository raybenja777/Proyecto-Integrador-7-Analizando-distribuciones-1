import pandas as pd
import matplotlib.pyplot as plt

# Leer el CSV
data = pd.read_csv('datos_descargados.csv')

# Crear el histograma
plt.hist(data['age'], bins=10, edgecolor='red', color='black')
# Configurar el gráfico con etiquetas y titulo
plt.title('Distribución de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()

# Crear el histograma y leer la columna de sexo
hombres = data[data['sex']==1]
mujeres = data[data['sex']==0]

# Crear los gráficos
bar_width = 0.35
index = [1, 2, 3, 4]  # Índices para posicionar las barras

plt.bar(index, [hombres['anaemia'].sum(), hombres['diabetes'].sum(), hombres['smoking'].sum(), hombres['DEATH_EVENT'].sum()], bar_width, label='Hombres', color='blue')
plt.bar([i + bar_width for i in index], [mujeres['anaemia'].sum(), mujeres['diabetes'].sum(), mujeres['smoking'].sum(), mujeres['DEATH_EVENT'].sum()], bar_width, label='Mujeres', color='red')

# Configurar el eje x
plt.title('Histograma Agrupado por Sexo')
plt.xlabel('Categoría')
plt.xticks([i + bar_width / 2 for i in index], ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos'])

# Configurar el eje y
plt.ylabel('Cantidad')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()







