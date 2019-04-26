#%% [markdown]
# # Tarea # 5
# ### Imports
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import prince
import scipy.stats
import os
#%%
# ## Ejercicio # 1
# a) Cargar la tabla
#%%
#os.getcwd()
#os.chdir(r'c:\\Users\\jmc\\Documents\\Ciencia de datos con Python\\ciencia-de-datos\\Unidad N. 5')
os.chdir(r'c:\\Users\\jocarr3\\Documents\\projects\\ciencia de datos python\\Unidad N. 5')

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
del datos['PassengerId']
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
# Tamano del plot
plt.rcParams["figure.figsize"] = [20, 10]

plt.style.use('ggplot')
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
# e) Boxplot, datos atipicos
#%%
boxplots = datos.boxplot(return_type='axes')
#%% [markdown]
# f) Graficos de densidad, histogramas y tests de normalidad
# **Densidad, Edad**
#%%
densidad = datos['Age'].plot(kind='density')
#%% [markdown]
# **Densidad, Parentezco**
#%%
densidad = datos['Parch'].plot(kind='density')
#%% [markdown]
# **Densidad, Tarifa**
#%%
densidad = datos['Fare'].plot(kind='density')

#%% [markdown]
# **Densidad, hermanos o conyuges**
#%%
densidad = datos['SibSp'].plot(kind='density')

#%% [markdown]
# **Histograma, Edad**
#%%
densidad = datos['Age'].plot(kind='hist')

#%% [markdown]
# **Histograma, Tarifa**
#%%
densidad = datos['Fare'].plot(kind='hist')

#%% [markdown]
# ***Tests de Normalidad***
#%% [markdown]
# ** Test de Shapiro-Wilk, Edad**
#%%
shapiro = scipy.stats.shapiro(datos.dropna()['Age'])
print(shapiro)
#%%
Test_Estadistico = shapiro[0]
print(Test_Estadistico)
#%%
p_value = shapiro[1]
print(p_value)
#%%
print(p_value < Test_Estadistico)

#%% [markdown]
# ** Test de Shapiro-Wilk, Parentezco**
#%%
shapiro = scipy.stats.shapiro(datos.dropna()['Parch'])
print(shapiro)
#%%
Test_Estadistico = shapiro[0]
print(Test_Estadistico)
#%%
p_value = shapiro[1]
print(p_value)
#%%
print(p_value < Test_Estadistico)

#%% [markdown]
# g) Scatter plots y grafico de todas las variables 2 a 2
# ** Scatter plot Edad vs Tarifa, 
#%%
x = datos['Fare']
y = datos['Age']
colores = recodificar(datos["Survived"], {"Si" : "red", "No": "green"})
plt.scatter(x, y, alpha=0.5, c=colores, cmap='viridis')


#%% [markdown]
# ** Scatter plot Edad vs Parentezco
#%%
x = datos['Fare']
y = datos['Age']
colores = recodificar(datos["Pclass"], {"primera" : "lightblue", "segunda" : "blue", "tercera": "purple"})
plt.scatter(x, y,  alpha=0.5, c=colores, cmap='viridis')

#%% [markdown]
# **  grafico de todas las variables 2 a 2
#%%
corrplot = sns.pairplot(datos, hue='Survived', size=2.5)

#%% [markdown]
# ** Matriz de correlaciones
#%%
corr = datos.corr()
print(corr)

#%% [markdown]
# ** Grafico de correlaciones
#%%
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


##########################################################
##########################################################

#%% [markdown]
# ### Ejercicio #2

datos = pd.read_csv('datos\\SAheart.csv', ";")
#%% [markdown]
# b) Recodifique las variables cualitativas
#%%
print(datos.head())

#%% [markdown]
# c) Estadisticas basicas
#%% [markdown]
# **Describe()**
#%%
print(datos.dropna().describe())
#%% [markdown]
# **Conteo de variables categoricas**
#%%
famHist = pd.crosstab(index=datos["famhist"],columns="count")
chd = pd.crosstab(index=datos["chd"],columns="count")

print(famHist)
print("\n")
print(chd)

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
# **Historia Familiar**
#%%
plt.rcParams["figure.figsize"] = [20, 10]

plt.style.use('ggplot')
alto = [famHist['count'][0], famHist['count'][1]]
barras = ('Present', 'Absent')
y_pos = np.arange(len(barras))

plt.bar(y_pos, alto, color=['darkviolet','violet'])
plt.xticks(y_pos, barras)

#%% [markdown]
# **Enfermedad card´ıaca coronaria**
#%%
alto = [chd['count'][0], chd['count'][1]]
barras = ('Present', 'Absent')
y_pos = np.arange(len(barras))

plt.bar(y_pos, alto, color=['green','lime'])
plt.xticks(y_pos, barras)

#%% [markdown]
# e) Boxplot, datos atipicos
#%%
boxplots = datos.boxplot(return_type='axes')
#%% [markdown]
# f) Graficos de densidad, histogramas y tests de normalidad
# **Densidad, Tabaco**
#%%
densidad = datos['tobacco'].plot(kind='density')
#%% [markdown]
# **Densidad, alcohol**
#%%
densidad = datos['alcohol'].plot(kind='density')

#%% [markdown]
# **Histograma, Edad**
#%%
densidad = datos['age'].plot(kind='hist')

#%% [markdown]
# **Histograma, Tarifa**
#%%
densidad = datos['ldl'].plot(kind='hist')

#%% [markdown]
# ***Tests de Normalidad***
#%% [markdown]
# ** Test de Shapiro-Wilk, SBP**
#%%
shapiro = scipy.stats.shapiro(datos.dropna()['sbp'])
print(shapiro)
#%%
Test_Estadistico = shapiro[0]
print(Test_Estadistico)
#%%
p_value = shapiro[1]
print(p_value)
#%%
print(p_value < Test_Estadistico)

#%% [markdown]
# ** Test de Shapiro-Wilk, Obesidad**
#%%
shapiro = scipy.stats.shapiro(datos.dropna()['obesity'])
print(shapiro)
#%%
Test_Estadistico = shapiro[0]
print(Test_Estadistico)
#%%
p_value = shapiro[1]
print(p_value)
#%%
print(p_value < Test_Estadistico)

#%% [markdown]
# g) Scatter plots y grafico de todas las variables 2 a 2
# ** Scatter plot Edad vs SBP, con historia familiar 
#%%
x = datos['sbp']
y = datos['age']
colores = recodificar(datos["famhist"], {"Present" : "red", "Absent": "green"})
plt.scatter(x, y, alpha=0.5, c=colores, cmap='viridis')


#%% [markdown]
# ** Scatter plot Edad vs Parentezco
#%%
x = datos['tobacco']
y = datos['obesity']
colores = recodificar(datos["chd"], {"Si" : "red", "No" : "blue"})
plt.scatter(x, y,  alpha=0.5, c=colores, cmap='viridis')

#%% [markdown]
# **  grafico de todas las variables 2 a 2
#%%
corr = sns.pairplot(datos, hue='chd', size=2.5)

#%% [markdown]
# ** Matriz de correlaciones
#%%
corr = datos.corr()
print(corr)

#%% [markdown]
# ** Grafico de correlaciones
#%%
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)

#%% [markdown]
# ### Ejercicio #3
# a) Efectuar ACP 
#%%
def circulo(datos,eje1=0,eje2=1):
    corr = pca.column_correlations(datos)
    (fig, ax) = plt.subplots(figsize=(12, 12))
    # Ejes
    ax.arrow(0,0,0,1,color="b")   
    ax.arrow(0,0,1,0,color="b")
    ax.arrow(0,0,0,-1,color="b")
    ax.arrow(0,0,-1,0,color="b")
    for i in range(0, len(corr.values)):     
        ax.arrow(0,
                 0,  
                 corr.values[i, eje1]*0.95,  # 0 para PC1
                 corr.values[i, eje2]*0.95,  # 1 fpara PC2
                 head_width=0.05,
                 head_length=0.05)
        plt.text(corr.values[i, eje1] + 0.05,
                 corr.values[i, eje2] + 0.05,
                 corr.index.values[i])
        an = np.linspace(0, 2 * np.pi, 100)
        plt.plot(np.cos(an), np.sin(an),color="b")  # Agrega el círculo
        plt.axis('equal')
        ax.set_title('Círculo de Correlaciones')
#%%
datos = pd.read_csv('datos\\ImportacionesMexico.csv', delimiter=';', decimal=',', index_col=0)
datos.index = datos.index.astype(str)
plt.style.use('seaborn')

pca = prince.PCA(n_components=5)
pca = pca.fit(datos)

print(datos.head())
#%%
print(datos.dtypes)

#%% [markdown]
# ** cosenos cuadrados
#%%

print(pca.row_coordinates(datos))


#%% [markdown]
# ** correlaciones de las variables con respecto a las componentes
#%%
print(pca.row_cosine_similarities(datos))
#%% [markdown]
# ** Valores Propios
#%%
print(pca.column_correlations(datos))
#%%
print(pca.eigenvalues_)
#%% [markdown]
# *** Componentes principales

# En el plano principal, se pueden notar tres clusters, uno compuesto por 1984 y 1985, el segundo de 1979, 1980 y 1987,
# y el tercero por 1981, 1982 y 1983. 
#%%
pca.plot_row_coordinates(datos,labels=datos.index,ellipse_fill=True)
#%% [markdown]
# *** Circulo de correlaciones
# En el círculo de correlaciones, se puede deducir que existe correlación positiva entre
# los países de Honduras, Guatemala y El Salvador, que son los de la parte norte de Centroamérica.
# También se notar que hay correlación positiva entre Costa Rica, Nicaragua y Panamá
# Costa Rica y Nicaragua no poseen correlación entre El Salvador, Guatemala y Honduras, pues su ángulo
# tiende a noventa grados
#%%
circulo(datos, 0, 1)
#%% [markdown]
# Se puede decir que de 1981 a 1983, las importaciones de Costa Rica, Nicaragua y Panamá
# fueron altas; mientras que entre 1984 y 1985 los países que tuvieron altas importaciones
# fueron Honduras, Guatemala y El Salvador
# Los años 1979 y 1980 fueron de importaciones bajas para todos.

#%% [markdown]
# *** Componentes 1 y 3
#%%
pca = prince.PCA(n_components=5)
pca = pca.fit(datos)
# Plotea el plano principal en "x_component=0, y_component=2"
pca.plot_row_coordinates(datos,x_component=0, y_component=2,labels=datos.index,ellipse_fill=True)

#%%
circulo(datos, 0, 2)
#%% [markdown]
# En este análisis, se puede notar que aunque antes no estaban correlacionadas, Honduras y 
# Costa Rica, tuvieron mayores importaciones en los años 1987 y 1988

#%% [markdown]
# ### Ejercicio #4
#%%
datos = pd.read_csv('datos\\SAheart.csv', ";")

#Se quitan variables categoricas
del datos['famhist']
del datos['chd']

pca = prince.PCA(n_components=5)
pca = pca.fit(datos)
#%% [markdown]
# ** cosenos cuadrados
#%%

print(pca.row_coordinates(datos))


#%% [markdown]
# ** correlaciones de las variables con respecto a las componentes
#%%
print(pca.row_cosine_similarities(datos))
#%% [markdown]
# ** Valores Propios
#%%
print(pca.column_correlations(datos))
#%%
print(pca.eigenvalues_)
#%% [markdown]
# *** Componentes principales

# Se hace dificil denotar clusters a simple vista, sin embargo si se ve en cuadrantes y 
# comparandolo con el círculo de correlaciones, en el cuadrante superior derecho se tiene 
# se determina que las variables definidas por alcohol y tabaco están positivamente correlacionadas
# con el sbp (presión sistólica) y la edad.
# Así como el ldl está fuerte y positivamente ligado a la obesidad, también existe correlación
# con la adiposidad
# La personalidad tipo A, se podría decir que es inversamente correlacionao con el alcohol,
# sin embargo tiene una muestra representativa baja 
#%%

pca.plot_row_coordinates(datos,ellipse_fill=True)
#%%
circulo(datos, 0, 1)

#%% [markdown]
# *** ACP con variables categoricas
#%%
datos = pd.read_csv('datos\\SAheart.csv', ";")

#%%
datos_dummy = pd.get_dummies(datos)
print(datos_dummy.head())
#%%
print(datos_dummy.dtypes)
#%%
pca = prince.PCA(n_components=5)
pca = pca.fit(datos_dummy)
# Plotea el plano principal
pca.plot_row_coordinates(datos_dummy,ellipse_fill=True)
#%% [markdown]
# ** cosenos cuadrados
#%%
print(pca.row_coordinates(datos_dummy))

#%% [markdown]
# ** correlaciones de las variables con respecto a las componentes
#%%
print(pca.row_cosine_similarities(datos_dummy))
#%% [markdown]
# ** Valores Propios
#%%
print(pca.column_correlations(datos_dummy))
#%%
print(pca.eigenvalues_)
#%%
circulo(datos_dummy)
#%% [markdonw]
# Se denota que la historia familiar(familyhist) y el tener una enfermedad coronaria(chd),
# estan fuerte y positivamente corelacionados.
# Al mismo tiempo estas variables no tienen relacion con el alcohol o el tabaco ni la obesidad
# pues como se puede ver tienen un angulo cercano a los noventa grados

#%% [markdown]
# c) ¿Cu´al de los an´alisis anteriores le parece m´as interesante? ¿Porqu´e?
# el analisis por medio del plano principal y el circulo de correlaciones, pues permite ver
# comportamientos entre las varialbes que pueden ser abstractos o tener relacion unas con otras. 