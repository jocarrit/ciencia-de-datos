#%% [markdown]
# #Tarea 6 - Jose Carrillo
# ## Imports
#%%
import os
import pandas as pd
import numpy as np
import scipy
from   math import pi
import matplotlib.pyplot as plt
from   sklearn.datasets import make_blobs
from   sklearn.decomposition import PCA
from   sklearn.datasets import make_blobs
from   sklearn.cluster import KMeans


# Import the dendrogram function and the ward, single, complete, average, linkage and fcluster clustering function from SciPy
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
from scipy.spatial.distance import pdist

os.getcwd()
os.chdir(r'c:\\Users\\jmc\\Documents\\Ciencia de datos con Python\\ciencia-de-datos\\Unidad N. 6')
#os.chdir(r'c:\\Users\\jocarr3\\Documents\\projects\\ciencia de datos python\\Unidad N. 6')

#%% [markdown]
# ** Funciones
#%%
def centroide(num_cluster, datos, clusters):
  ind = clusters == num_cluster
  return(pd.DataFrame(datos[ind].mean()).T)

def bar_plot(centros, labels, cluster = None, var = None):
    from seaborn import color_palette
    colores = color_palette()
    def inside_plot(valores, labels, titulo):
        plt.barh(range(len(valores)), valores, 1/1.5, color = colores)
        plt.title(titulo, color='k')
    if var is not None:
        centros = np.array([n[[x in var for x in labels]] for n in centros])
        colores = [colores[x % len(colores)] for x, i in enumerate(labels) if i in var]
        labels = labels[[x in var for x in labels]]
    if cluster is None:
        for i in range(centros.shape[0]):
            plt.subplot(1, centros.shape[0], i + 1)
            inside_plot(centros[i].tolist(), labels, ('Cluster ' + str(i)))
            plt.yticks(range(len(labels)), labels) if i == 0 else plt.yticks([]) 
    else:
        pos = 1
        for i in cluster:
            plt.subplot(1, len(cluster), pos)
            inside_plot(centros[i].tolist(), labels, ('Cluster ' + str(i)))
            plt.yticks(range(len(labels)), labels) if pos == 1 else plt.yticks([]) 
            pos += 1

def radar_plot(centros, labels):
    from math import pi
    centros = np.array([((n - min(n)) / (max(n) - min(n)) * 100) if 
                        max(n) != min(n) else (n/n * 50) for n in centros.T])
    angulos = [n / float(len(labels)) * 2 * pi for n in range(len(labels))]
    angulos += angulos[:1]
    ax = plt.subplot(111, polar = True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    plt.xticks(angulos[:-1], labels)
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
           ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], 
           color = "grey", size = 8)
    plt.ylim(-10, 100)
    for i in range(centros.shape[1]):
        valores = centros[:, i].tolist()
        valores += valores[:1]
        ax.plot(angulos, valores, linewidth = 1, linestyle = 'solid', 
                label = 'Cluster ' + str(i))
        ax.fill(angulos, valores, alpha = 0.3)
    plt.legend(loc='upper right', bbox_to_anchor = (0.1, 0.1))

#%% [markdown]
# ## Ejercicio 1
# ** a) Cargar tabla
#%%
Importaciones = pd.read_csv('datosTarea\\ImportacionesMexico.csv', delimiter=';', decimal=',', index_col=0)
print(Importaciones)
#%% [markdown]
# ** b) Ejecute un Clustering Jerarquico con la agregacion del Salto Maximo, Salto Mınimo,
# Promedio y Ward. Grafique el dendograma con cortes para dos y tres clusteres.
#%%
ward_res = ward(Importaciones)         #Ward
single_res = single(Importaciones)     #Salto mínimo
complete_res = complete(Importaciones) #Salto Máximo
average_res = average(Importaciones)   #Promedio
#%% [markdown]
# ** Agregacion promedio
#%%
plt.style.use('seaborn')
plt.figure(figsize=(13,10))

dendrogram(average_res,labels= Importaciones.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [150, 150], '--', c='k')
ax.plot(limites, [120, 120], '--', c='k')
ax.text(limites[1], 150, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 120, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion salto minimo
#%%
plt.figure(figsize=(13,10))
dendrogram(single_res,labels= Importaciones.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [110, 110], '--', c='k')
ax.plot(limites, [80, 80], '--', c='k')
ax.text(limites[1], 110, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 80, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion salto maximo
#%%
plt.figure(figsize=(13,10))
dendrogram(complete_res,labels= Importaciones.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [200, 200], '--', c='k')
ax.plot(limites, [150, 150], '--', c='k')
ax.text(limites[1], 200, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 150, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion Ward
#%%
plt.figure(figsize=(13,10))
dendrogram(ward_res,labels= Importaciones.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [250, 250], '--', c='k')
ax.plot(limites, [170, 170], '--', c='k')
ax.text(limites[1], 250, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 170, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")

#%% [markdown]
# ** c) Usando tres clusteres interprete los resultados del ejercicio anterior para el caso de 
# agregacion de Ward mediante graficos de barras y graficos tipo Radar.
#%%
grupos = fcluster(linkage(pdist(Importaciones), method = 'ward', metric='euclidean'), 3, criterion = 'maxclust')
grupos = grupos-1
print(grupos)
#%%
centros = np.array(pd.concat([centroide(0, Importaciones, grupos), 
                              centroide(1, Importaciones, grupos),
                              centroide(2, Importaciones, grupos)]))
print(centros)

#%%
plt.figure(1, figsize = (12, 8))
bar_plot(centros, Importaciones.columns)
#%%
plt.figure(1, figsize = (10, 10))
radar_plot(centros, Importaciones.columns)

#%% 
clusters = pd.DataFrame({'year' : Importaciones.index, 'cluster': grupos})
print(clusters)

#%% [markdown]
# Interpretacion
#%% [markdown]
# ** K medias
#%%
kmedias = KMeans(n_clusters=3)
kmedias.fit(Importaciones)
print(kmedias.predict(Importaciones))
#%%
centros = np.array(kmedias.cluster_centers_)
print(centros)
#%%
plt.figure(1, figsize = (12, 8))
bar_plot(centros, Importaciones.columns)
#%%
plt.figure(1, figsize = (10, 10))
radar_plot(centros, Importaciones.columns)
#%%
Importaciones['Cluster'] = kmedias.predict(Importaciones)
print(Importaciones)
Importaciones.to_csv('ImportacionesMexicoCluster.csv',sep=';',index=False)

#%% [markdown]
# ## Ejercicio #2

#%%
Padecimientos = pd.read_csv('DatosClase\\SAheart.csv', ';')
del Padecimientos['famhist']
del Padecimientos['chd']
print(Padecimientos)


#%% [markdown]
# b)  Usando solamente las variables numericas, ejecute un Clustering Jerarquico 
# con la agregacion del Salto Maximo, Salto Mınimo, Promedio y Ward. 
# Grafique el dendograma con cortes para dos y tres clusteres.

#%%
ward_res = ward(Padecimientos)         #Ward
single_res = single(Padecimientos)     #Salto mínimo
complete_res = complete(Padecimientos) #Salto Máximo
average_res = average(Padecimientos)   #Promedio
#%% [markdown]
# ** Agregacion promedio
#%%
plt.style.use('seaborn')
plt.figure(figsize=(13,10))

dendrogram(average_res,labels= Padecimientos.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [150, 150], '--', c='k')
ax.plot(limites, [120, 120], '--', c='k')
ax.text(limites[1], 150, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 120, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion salto minimo
#%%
plt.figure(figsize=(13,10))
dendrogram(single_res,labels= Padecimientos.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [110, 110], '--', c='k')
ax.plot(limites, [80, 80], '--', c='k')
ax.text(limites[1], 110, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 80, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion salto maximo
#%%
plt.figure(figsize=(13,10))
dendrogram(complete_res,labels= Padecimientos.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [200, 200], '--', c='k')
ax.plot(limites, [150, 150], '--', c='k')
ax.text(limites[1], 200, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 150, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion Ward
#%%
plt.figure(figsize=(13,10))
dendrogram(ward_res,labels= Padecimientos.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [250, 250], '--', c='k')
ax.plot(limites, [170, 170], '--', c='k')
ax.text(limites[1], 250, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 170, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")

#%% [markdown]
# c) Usando 3 clusteres interprete los resultados del ejercicio anterior para el caso de agregacion
# de Ward mediante graficos de barras y graficos tipo Radar.
#%%
grupos = fcluster(linkage(pdist(Padecimientos), method = 'ward', metric='euclidean'), 3, criterion = 'maxclust')
grupos = grupos-1
print(grupos)
#%%
centros = np.array(pd.concat([centroide(0, Padecimientos, grupos), 
                              centroide(1, Padecimientos, grupos),
                              centroide(2, Padecimientos, grupos)]))
print(centros)

#%%
plt.figure(1, figsize = (12, 8))
bar_plot(centros, Padecimientos.columns)
#%%
plt.figure(1, figsize = (10, 10))
radar_plot(centros, Padecimientos.columns)

#%% [markdown]
# ## Usando variables categoricas

#%%
Padecimientos = pd.read_csv('DatosClase\\SAheart.csv', ';')
dummies = pd.get_dummies(Padecimientos)
print(dummies)


#%% [markdown]
# b)  Usando solamente las variables numericas, ejecute un Clustering Jerarquico 
# con la agregacion del Salto Maximo, Salto Mınimo, Promedio y Ward. 
# Grafique el dendograma con cortes para dos y tres clusteres.

#%%
ward_res = ward(dummies)         #Ward
single_res = single(dummies)     #Salto mínimo
complete_res = complete(dummies) #Salto Máximo
average_res = average(dummies)   #Promedio
#%% [markdown]
# ** Agregacion promedio
#%%
plt.style.use('seaborn')
plt.figure(figsize=(13,10))

dendrogram(average_res,labels= dummies.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [150, 150], '--', c='k')
ax.plot(limites, [120, 120], '--', c='k')
ax.text(limites[1], 150, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 120, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion salto minimo
#%%
plt.figure(figsize=(13,10))
dendrogram(single_res,labels= dummies.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [110, 110], '--', c='k')
ax.plot(limites, [80, 80], '--', c='k')
ax.text(limites[1], 110, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 80, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion salto maximo
#%%
plt.figure(figsize=(13,10))
dendrogram(complete_res,labels= dummies.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [200, 200], '--', c='k')
ax.plot(limites, [150, 150], '--', c='k')
ax.text(limites[1], 200, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 150, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")
#%% [markdown]
# ** Agregacion Ward
#%%
plt.figure(figsize=(13,10))
dendrogram(ward_res,labels= dummies.index.tolist())

ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [250, 250], '--', c='k')
ax.plot(limites, [170, 170], '--', c='k')
ax.text(limites[1], 250, ' dos clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
ax.text(limites[1], 170, ' tres clústeres', va='center', fontdict={'size': 15, 'color': 'black'})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")

#%% [markdown]
# c) Usando 3 clusteres interprete los resultados del ejercicio anterior para el caso de agregacion
# de Ward mediante graficos de barras y graficos tipo Radar.
#%%
grupos = fcluster(linkage(pdist(dummies), method = 'ward', metric='euclidean'), 3, criterion = 'maxclust')
grupos = grupos-1
print(grupos)
#%%
centros = np.array(pd.concat([centroide(0, dummies, grupos), 
                              centroide(1, dummies, grupos),
                              centroide(2, dummies, grupos)]))
print(centros)

#%%
plt.figure(1, figsize = (12, 8))
bar_plot(centros, dummies.columns)
#%%
plt.figure(1, figsize = (10, 10))
radar_plot(centros, dummies.columns)

#%% [markdown]
# ## Problema #3
# a) Cargue la tabla de datos y ejecute un dropna().describe(), y encuentre la dimension de
# la tabla de datos (numero de filas y columnas) datos.shape, con esto verifique la correcta
# lectura de los datos
#%%
Beijing = pd.read_csv('DatosTarea\\DatosBeijing.csv', ',')

withNa = Beijing.shape[0]
print(withNa)
print(Beijing.describe())
print(Beijing.shape)

#%% [markdown]
#%% b) Elimine las filas con NA. ¿Cuantas filas se eliminaron?
#%%
Beijing = Beijing.dropna()
noNa = Beijing.shape[0]
print("Se eliminaron " + str(withNa - noNa) + " filas")

#%% [markdown]
# c) Elimine de la tabla de datos la variable DireccionViento. ¿Por que se debe eliminar?
# ¿Que otra alternativa se tiene en lugar de eliminarla?
#%%
del Beijing['DireccionViento']
print(Beijing)
#%% [markdown]
# Se elimina esta variable por ser una variable categorica.
# Existe la opcion de convertirla en variable dummy para ser utilizada como nuemrica

#%% [markdown]
# d) ¿Que pasa si ejecutamos un clustering jerarquico para esta tabla de datos. ¿Por que sucede
# esto?
#%%
#grupos = fcluster(linkage(pdist(Beijing), method = 'ward', metric='euclidean'), 3, criterion = 'maxclust')
#%% [markdown]
# Al tener una compudatora de baja capacidad, este algoritmo es muy pesado, pues tiene que manejar un array de n x n, donde
# n = 43 000, por tanto, no es viable ejecutarlo.
# Aun asi, como prueba se ejcuto y hubo que reiniciar la computadora de manera forzada,
# pues ni siquiera la interrupcion del mouse al procesador estaba siendo ejecutada.

#%% [markdown]
# Investigue y explique para que sirven los atributos max iter (similar a iter.max en R)
# y n init (similar a nstart en R), ambos de la clase sklearn.cluster.KMeans. Luego
# ejecute un k-medias con k = 3 usando max iter=5000 y n init=10.
#%%
del Beijing['ID']
#del Beijing['Anno']
del Beijing['Hora']
del Beijing['Dia']
del Beijing['Mes']

Beijing['Anno'] = Beijing['Anno'].astype(str)

dummies = pd.get_dummies(Beijing)

kmedias = KMeans(n_clusters=3, max_iter=5000, n_init=10)
kmedias.fit(dummies)
print(kmedias.predict(dummies))
#%%
centros = np.array(kmedias.cluster_centers_)
print(centros)
#%%
plt.figure(1, figsize = (12, 8))
bar_plot(centros, dummies.columns)
#%%
plt.figure(1, figsize = (10, 10))
radar_plot(centros, dummies.columns)

#%% [markdown]
# ## Ejercicio # 4
#%%
class Exploratorio():
    def __init__(self, dataframe = pd.DataFrame()):
        self.__dataframe = dataframe
    
    @property
    def dataframe(self):
        return self.__dataframe
    
    @dataframe.setter
    def dataframe(self, nuevo_dataframe):
        self.dataframe = nuevo_dataframe
    
    def analisis(self, var):
        print("Encabezado \n")
        print(self.__encabezado())
        print("\nDimension\n")
        print(self.__dimension())
        print("\nMedia\n")
        print(self.__estadisticas()['Media'])
        print("\nMediana\n")
        print(self.__estadisticas()['Mediana'])
        print("\nDesviación Estandar\n")
        print(self.__estadisticas()['DS'])
        print("\nMínimo\n")
        print(self.__estadisticas()['minimo'])
        print("\nPercentiles\n")
        print(self.__percentiles())
        print("\nMáximo\n")
        print(self.__estadisticas()['maximo'])
        print("\nBoxplot\n")
        box = self.__boxplot()

    def __encabezado(self):
        return self.dataframe.head()
    
    def __dimension(self):
        return self.dataframe.shape
        
    def __estadisticas(self):
        return {'Media' : self.dataframe.mean(numeric_only=True),
                'Mediana' : self.dataframe.median(numeric_only=True),
                'DS' : self.dataframe.std(numeric_only=True),
                'minimo' : self.dataframe.min(numeric_only=True),
                'maximo' : self.dataframe.max(numeric_only=True)}
    
    def __percentiles(self):
        return self.dataframe.quantile(np.array([0,.25,.50,.75,1]))

    def __boxplot(self):
        return self.dataframe.boxplot(return_type='axes')
    
    def __dist_densidad(self, var):
        return self.dataframe[var].plot(kind='density')
    
    def __histograma(self, var):
        return self.dataframe[var].plot(kind='hist')
    
    def __test_normalidad(self, var):
        return scipy.stats.shapiro(self.dataframe.dropna()[var])
#%%
Estudiantes = pd.read_csv('DatosClase\\EjemploEstudiantes.csv', ';', decimal=',')
Exp = Exploratorio(Estudiantes)

var = ['Matematicas', 'Ciencias']

Exp.analisis(var)