import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df_ventas_region = pd.read_csv("ventas_por_region.csv")


print(df_ventas_region )

print(df_ventas_region.info() )


df_ventas_region ["ventas"] = df_ventas_region ["ventas"].str.replace('$','', regex=False) 
df_ventas_region ["ventas"] = df_ventas_region ["ventas"].astype( "float64")

df_ventas_region ["fecha"] = pd.to_datetime( df_ventas_region ["fecha"])
df_ventas_region ["fecha"] = df_ventas_region ["fecha"].dt.strftime("%d/%m/%Y")
df_ventas_region ["fecha"] = pd.to_datetime( df_ventas_region ["fecha"])

print(df_ventas_region.info() )
print(df_ventas_region.head() )


# convertir text fecha a datetime 
# Gráfico de líneas
sns.lineplot(x='fecha', y='ventas', data=df_ventas_region, marker='o', color='green',linewidth=1)
plt.title('Ventas a lo largo del tiempo', fontsize=14)
plt.xlabel('Años', fontsize=12)
plt.ylabel('Ventas', fontsize=12)

plt.show()




#------------------------------------------------------------------------------------

"""
#2. Gráficos de Barras
#Los gráficos de barras son excelentes para comparar diferentes grupos de datos.

# Datos
categorias = ['A', 'B', 'C', 'D']
valores = [5,7,3,8]
data_barras = pd.DataFrame({'Categorías': categorias, 'Valores': valores})

# Gráfico de barras
#sns.barplot(x='Categorías', y='Valores', data=data_barras)
#plt.title('Comparación de categorías')
#plt.ylabel('Valores')
#plt.show()

# Personalización del Gráfico de Barras
# Podemos agregar colores y ajustar el ancho de las barras:
sns.barplot(x='Categorías',y='Valores', data=data_barras, palette='viridis')

plt.title('Comparación de categorías', fontsize=14)
plt.xlabel('Categorías', fontsize=12)
plt.ylabel('Valores', fontsize=12)
plt.show()
"""

#------------------------------------------------------------------------------------

"""
# 3. Gráficos de Dispersión
# Los gráficos de dispersión permiten visualizar la relación entre dos variables.

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 1, 4]

data_dispersion = pd.DataFrame({'Variable X': x, 'Variable Y': y})

#data_dispersion = pd.DataFrame({'Variable X':[1, 2, 3, 4, 5], 'Variable Y':[2, 3, 5, 1, 4]})
#print(data_dispersion)

# Gráfico de dispersión
#sns.scatterplot(x='Variable X', y='Variable Y', data=data_dispersion, color='cyan')
#plt.title('Gráfico de dispersión de variables')
#plt.show()


# Personalización del Gráfico de Dispersión
# Podemos ajustar colores y tamaños de los puntos:

sns.scatterplot(x='Variable X', y='Variable Y', data=data_dispersion, color='cyan', s=[100, 150, 200, 250, 300])
plt.title('Gráfico de dispersión de variables', fontsize=14)
plt.xlabel('Variable X', fontsize=12)
plt.ylabel('Variable Y', fontsize=12)
plt.show()
"""

#------------------------------------------------------------------------------------

"""
# 4. Boxplot (Gráfico de Caja)
# Los boxplots son útiles para mostrar distribución datos y resaltar valores atípicos.

# Datos
data_box = pd.DataFrame({
'Categoría': ['A', 'A', 'B', 'B', 'C', 'C'],
'Valores': [1, 2, 5, 6, 2, 10]
})

# Gráfico de caja
#sns.boxplot(x='Categoría', y='Valores', data=data_box)
#plt.title('Boxplot de Valores por Categoría')
#plt.show()

# Personalización del Boxplot​
# Podemos ajustar la paleta de colores o agregar puntos para los valores atípicos:

sns.boxplot(x='Categoría', y='Valores', data=data_box, palette='Set3')
plt.title('Boxplot de Valores por Categoría', fontsize=14)
plt.show()
"""

#------------------------------------------------------------------------------------

"""
# 5. Violin Plot
# El Violin Plot combina un boxplot con la densidad de probabilidad de la variable.

# Datos
data_box = pd.DataFrame({
'Categoría': ['A', 'A', 'B', 'B', 'C', 'C'],
'Valores': [1, 2, 5, 6, 2, 10]
})

# Gráfico de violín
#sns.violinplot(x='Categoría', y='Valores', data=data_box)
#plt.title('Violin Plot de Valores por Categoría')
#plt.show()


# Personalización del Violin Plot
# Podemos ajustar los colores y la transparencia:

#sns.violinplot(x='Categoría', y='Valores', data=data_box, palette='muted', alpha=0.7)

# el de arriba es vieja version seaborn
sns.violinplot(x='Categoría', y='Valores', data=data_box, palette='muted', hue='Categoría',
legend=False, alpha=0.7)

plt.title('Violin Plot de Valores por Categoría', fontsize=14)
plt.show()
"""


#------------------------------------------------------------------------------------
"""
# 6. Swarm Plot
# Los swarm plots son útiles para visualizar la distribución de datos sobre una
# categoría y evitar la sobreposición de puntos.

# Datos
data_box = pd.DataFrame({
'Categoría': ['A', 'A', 'B', 'B', 'C', 'C'],
'Valores': [1, 2, 5, 6, 2, 10]
})

# Gráfico de swarm
# sns.swarmplot(x='Categoría', y='Valores', data=data_box, color='black')
#plt.title('Swarm Plot de Valores por Categoría')
#plt.show()


# Personalización del Swarm Plot
# Se pueden cambiar el color y ajustar el tamaño de los puntos:
sns.swarmplot(x='Categoría', y='Valores', data=data_box, color='blue', size=8)
plt.title('Swarm Plot de Valores por Categoría', fontsize=14)
plt.show()
"""

#------------------------------------------------------------------------------------


# Ejemplo 1: Subplots Básicos
#import matplotlib.pyplot as plt
import numpy as np
"""
# Crear datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear una figura y varios subplots
fig, axs = plt.subplots(2, 1) # 2 filas y 1 columna

# Primer subplot: Seno

axs[0].plot(x, y1, color='blue')
axs[0].set_title('Seno')
axs[0].set_xlabel('X')
axs[0].set_ylabel('sin(X)')

# Segundo subplot: Coseno
axs[1].plot(x, y2, color='red')
axs[1].set_title('Coseno')
axs[1].set_xlabel('X')
axs[1].set_ylabel('cos(X)')

# Ajustar el layout
plt.tight_layout()
plt.show()
"""

#------------------------------------------------------------------------------------

"""
# Ejemplo 2: Subplots en una Cuadrícula

# Crear datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Crear una figura y varios subplots en una cuadrícula de 2x2 
# (ocultamos el ultimo)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Gráfico de Seno
axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title('Seno')
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('sin(X)')

# Gráfico de Coseno
axs[0, 1].plot(x, y2, color='red')
axs[0, 1].set_title('Coseno')
axs[0, 1].set_xlabel('X')
axs[0, 1].set_ylabel('cos(X)')

# Gráfico de Tangente
axs[1, 0].plot(x, y3, color='green')
axs[1, 0].set_ylim(-10, 10) # Limitar el eje y
axs[1, 0].set_title('Tangente')
axs[1, 0].set_xlabel('X')
axs[1, 0].set_ylabel('tan(X)')

# Gráfico vacío
axs[1, 1].axis('off')

# Ajustar el layout
plt.tight_layout()
plt.show()
"""

#------------------------------------------------------------------------------------

"""
#Ejemplo 3: Subplots con Seaborn
#import seaborn as sns
#import pandas as pd

# Cargar el conjunto de datos
tips = sns.load_dataset('tips')

# Crear una figura y varios subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Gráfico de cajas de la propina por sexo
sns.boxplot(x='sex', y='tip', data=tips, ax=axs[0, 0])
axs[0, 0].set_title('Boxplot de Propinas por Sexo')

# Gráfico de dispersión de total_bill vs tip
sns.scatterplot(x='total_bill', y='tip', data=tips, ax=axs[0,1], hue='time')
axs[0, 1].set_title('Dispersión de Total Bill vs Tip')

# Histograma de propinas
sns.histplot(tips['tip'], bins=20, ax=axs[1, 0], kde=True)
axs[1, 0].set_title('Distribución de Propinas')

# Gráfico vacío
axs[1, 1].axis('off')

# Ajustar el layout
plt.tight_layout()
plt.show()

"""

#------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------

'''
=================================================================================
RESUMEN

GRAFICOS DE LINEAS
==================
# Datos
data = pd.DataFrame({'Tiempo':[1,2,3,4,5], 'Ventas':[10,15, 20, 25, 30]})


SEABORN
-------
sns.lineplot(x='Tiempo', y='Ventas', data=data, marker='o', color='green',linewidth=2)



SEABORN
-------

# GRÁFICO DE BARRAS
===================
sns.barplot(x='Categorías', y='Valores', data=data_barras)


'''
