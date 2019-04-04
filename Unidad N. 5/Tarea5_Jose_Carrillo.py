#%% [markdown]
# # Tarea # 5
# ### Imports
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#%%
# ## Ejercicio # 1
# a) Cargar la tabla
#%%
#os.getcwd()
os.chdir(r'c:\\Users\\jmc\\Documents\\Ciencia de datos con Python\\ciencia-de-datos\\Unidad N. 5')
datos = pd.read_csv('datos\\Titanic.csv')
#%% [markdown]
# b) Recodifique las variables cualitativas
#%%
def recodificar(col, nuevo_codigo):
  col_cod = pd.Series(col, copy=True)
  for llave, valor in nuevo_codigo.items():
    col_cod.replace(llave, valor, inplace=True)
  return col_cod

datos["Survived"] = recodificar(datos["Survived"], {0 : "Si", 1: "No"})

datos["Pclass"] = recodificar(datos["Pclass"], {1 : "primera", 2: "segunda", 3 : "tercera"})

print(datos.head())

#%% [markdown]
# c) Estadisticas basicas
#%% [markdown]
# **Describe()**
#%%
datos.drop(columns="PassengerId", axis=1)
print(datos.dropna().describe())
#%% [markdown]
# **Conteo de variables categoricas**
#%%
survived = pd.crosstab(index=datos["Survived"],columns="count")
pClass = pd.crosstab(index=datos["Pclass"],columns="count")
sex = pd.crosstab(index=datos["Sex"],columns="count")
embarked = pd.crosstab(index=datos["Embarked"],columns="count")

print(survived)
print("\n")
print(pClass)
print("\n")
print(sex)
print("\n")
print(embarked)

#%% [markdown]
# **Media de datos numericos**
#%%
print(datos.mean(numeric_only=True))
#%% [markdown]
# **Mediana de datos numericos**
#%%
print(datos.median(numeric_only=True))
#%% [markdown]
# **Desviacion Estandar de datos numericos**
#%%
print(datos.std(numeric_only=True))
#%% [markdown]
# **Maximos de datos numericos**
#%%
print(datos.max(numeric_only=True))
#%% [markdown]
# **Percentiles de datos numericos**
#%%
print(datos.quantile(np.array([0,.25,.50,.75,1])))

#%% [markdown]
# d) Grafico de barras para determinar distribucion de variables categoricas
# **Survided**
#%%
# Altura de la barra
alto = [survived['count'][0], survived['count'][1]]

# definicion de las barras
barras = ('No', 'Sí')

# Posicion de las barras en eje x
y_pos = np.arange(len(barras))

plt.bar(y_pos, alto, color=['red','blue'])
plt.xticks(y_pos, barras)

#%% [markdown]
# **Passenger Class**
#%%
alto = [pClass['count'][0], pClass['count'][1], pClass['count'][2]]
barras = ('Primera', 'Segunda', 'Tercera')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['green', 'blue', 'lightblue'])
plt.xticks(y_pos, barras)

#%% [markdown]
# **Sex**
#%%
alto = [sex['count'][0], sex['count'][1]]
barras = ('Femenino', 'Masculino')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['purple', 'lime'])
plt.xticks(y_pos, barras)

#%% [markdown]
# **Embarked Port**
#%%
alto = [embarked['count'][0], embarked['count'][1], embarked['count'][2]]
barras = ('Cherbourg', 'Queenstown', 'Southampton')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['yellow', 'orange', 'red'])
plt.xticks(y_pos, barras)

#%% [markdown]
# **Boxplot, datos atipicos**
#%%
datos.head()
boxplots = datos.boxplot(return_type='axes')
