#%% [markdown]
# #Tarea 7 - Jose Carrillo
# ##Imports
#%%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

#%%
def recodificar(col, nuevo_codigo):
  col_cod = pd.Series(col, copy=True)
  for llave, valor in nuevo_codigo.items():
    col_cod.replace(llave, valor, inplace=True)
  return col_cod
#%% [markdown]
# ## Ejercicio N 1
# Supongamos que tenemos un modelo predictivo para detectar Fraude
# en Tarjetas de Credito, la variable a predecir es Fraude con dos posibles valores Sı (para el
# caso en que sı fue fraude) y No (para el caso en que no fue fraude). Supongamos la matriz de
# confusion es:
#%%
data = [[83254, 12],[889, 3]]

mc = pd.DataFrame(data, index=['No', 'Si'], columns = ['No', 'Si'])

print(mc)
#%%
total = mc.sum()['No'] + mc.sum()['Si']
total_no = 83266
total_si = 892
VN = mc.loc['No', 'No']
FP = mc.loc['No', 'Si']
FN = mc.loc['Si', 'No']
VP = mc.loc['Si', 'Si']

PG = (VN + VP)/total
PP = VP / (FN + VP)
AP = VP / (FP + VP)
AN = VN / (VN + FN)
PN = VN / (VN + FP)
PFP = FP / (VN + FP)
PFN = FN / (FN + VP) 

print('Precisión Global: ' + str(PG*100) + '%\n')
print('Precisión Positiva: ' + str(PP*100) + '%\n')
print('Precisión Negativa: ' + str(PN*100) + '%\n')
print('Falsos positivos: ' + str(PFP*100) + '%\n')
print('Falsos negativos: ' + str(PFN*100) + '%\n')
print('Asetividad positiva: ' + str(AP*100) + '%\n')
print('Asetividad negativa: ' + str(AN*100) + '%\n')

#%% [markdown]
# ### ¿Es bueno o malo el modelo predictivo?
# 

#%% [markdown]
# ## Ejercicio N 2
# Esta pregunta utiliza los datos sobre la conocida historia y tragedia del
# Titanic, usando los datos (titanic.csv) de los pasajeros se trata de predecir la supervivencia
# o no de un pasajero.
# 1 -Cargue la tabla de datos titanic.csv en Python. Asegurese re-codificar las variables
# cualitativas y de ignorar variables que no se deben usar.
#%%
os.chdir(r'c:\\Users\\jmc\\Documents\\Ciencia de datos con Python\\ciencia-de-datos\\Unidad N. 7')
datos = pd.read_csv('DatosTarea\\titanic.csv')

print(datos.head())
del datos['PassengerId']
del datos['Name']
del datos['Ticket']
del datos['Cabin']

# Recodificar
datos["Survived"] = recodificar(datos["Survived"], {0 : "Si", 1: "No"})
datos["Sex"] = recodificar(datos["Sex"], {'male' : 0, 'female' : 1})
datos["Embarked"] = recodificar(datos["Embarked"], {'C' : 0, 'Q': 1, 'S' : 2})

datos["Sex"] = datos["Sex"].astype('category')
datos["Embarked"] = datos["Embarked"].astype('category')
datos["Survived"] = datos["Survived"].astype('category')

print(datos.info())

#%% [markdown]
# 2 -Genere al azar una tabla de testing con el 25 % de los datos y con el resto de los datos
# genere una tabla de aprendizaje.
#%%
datos.dropna()
X = datos.iloc[:,1:]
print(X.head())

Y = datos.iloc[:,0]
print(Y.head())

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.75, random_state=0)

#%% [markdown]
# 3 -Usando todos los metodos predictivos vistos en clase genere modelos predictivos para la
# tabla de aprendizaje. Grafique el arbol de decision.
# ### KNN
#%%
instancia_knn = KNeighborsClassifier(n_neighbors=70)

instancia_knn.fit(X_train,y_train)

print("Las predicciones en Testing son: {}".format(instancia_knn.predict(X_test)))

print("Precisión en Testing: {:.2f}".format(instancia_knn.score(X_test, y_test)))