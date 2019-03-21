# -*- coding: UTF-8 -*-


#%% [markdown]
# ## Imports
#%%
import os
import ciencia_datos as cd
import importlib
importlib.reload(cd)
import pandas as pd

#%% [markdown]
# ## Ejercicio 1
# Programe en Python una función que recibe dos valores, determinar cual de los dos valores es 
# el mayor y luego lo retorna (no puede usar la funcion max de Python).
#%%
a = 5
b = 7

print('El Mayor entre ' + str(a) + ' y ' + str(b) + ' es: ' + str(cd.obtenerMayor(a, b)))

#%% [markdown]
# ## Ejercicio 2
# Programe en Python una funcion que recibe tres valores A, B, y C y retorna el mayor (no puede
# usar la funcion max de Python)
#%%
A = 11
B = 9
C = 67

print('El Mayor entre ' + str(A) + ' , ' + str(B) + ' y ' + str(C) + ' es: ' + str(cd.obtenerMayor3(A, B, C)))

#%% [markdown]
# ## Ejercicio 3
# Programe en Python una funcion que recibe cuatro numeros y retorna el mayor (no puede usar
# la funcion max de Python).
#%%
W = 100
X= 200
Y = 670
Z = 810

print('El Mayor entre ' + str(W) + ' , ' + str(X) + ' , ' + str(Y) + ' y ' + str(Z) + ' es: ' + str(cd.obtenerMayor4(W, X, Y, Z)))

#%% [markdown]
# ## Ejercicio 4
# Programe en Python una funcion que recibe un numero n y retorna la sumatoria de los numeros
# enteros al cuadrado comprendidos entre el 1 y el n.
#%%
n = 4
print('La sumatoria de enteros al cuadrado de 1 hasta ' + str(n) + ' es: ' + str(cd.sumatoria(n)))

#%% [markdown]
# ## Ejercicio 5
# Desarrolle una funcion que realice la sumatoria de los numeros enteros multiplos de 3, comprendidos entre el 1 y el n.
#%%
n = 9
print('La sumatoria de enteros multiplos de 3 desde 1 hasta ' + str(n) + ' es: ' + str(cd.sumatoriaMult3(n)))

#%% [markdown]
# ## Ejercicio 6
# Programe en Python una funcion que genera 2000 numeros al azar entre 1 y 5000 y luego calcula
# cuantos estan entre el 1500 y 4500, ambos inclusive.
#%%
print('Los numeros aleatorios generados entre 1500 y 4500 son: \n\n' + str(cd.randomRango()))


#%% [markdown]
# ## Ejercicio 7
# Desarrolle una funcion que calcula el promedio de una lista de numeros. No puede utilizar la
# funcion sum ni la funcion mean.
#%%
lista = [1,4,9,7,3,5,10,15,21,3]

print('Dada la lista de numeros enteros: \n\n' + str(lista) + '\n\nEl promedio es: ' + str(cd.promedio(lista)))

#%% [markdown]
# ## Ejercicio 8
# Desarrolle una funci´on que calcula la varianza de una lista de n´umeros. No puede utilizar la
# funci´on la funci´on sum, la funci´on mean ni la funci´on var
#%%
lista2 = [1, 8, 6, 4, 9, 7, 21, 32, 15, 10]
print('Dada la lista de numeros enteros: \n\n' + str(lista2) + '\n\nLa varianza es: ' + str(cd.varianza(lista2)))

#%% [markdown]
# ## Ejercicio 9
# Desarrolle una funci´on que calcula el costo de una llamada telef´onica que ha durado t minutos
# sabiendo que si t < 1 el costo es de 0,4 d´olares, mientras que para duraciones superiores el
# costo es de 0,4 + (t − 1)/4 d´olares, la funci´on debe recibir el valor de t
#%%
tiempo_de_llamada1 = 0.5
tiempo_de_llamada2 = 2
tiempo_de_llamada3 = 10

print('Tiempo de llamada: ' + str(tiempo_de_llamada1) + ' minutos' + '\nCosto: $' + str(cd.costoLlamada(tiempo_de_llamada1)) + '\n')
print('Tiempo de llamada: ' + str(tiempo_de_llamada2) + ' minutos' + '\nCosto: $' + str(cd.costoLlamada(tiempo_de_llamada2)) + '\n')
print('Tiempo de llamada: ' + str(tiempo_de_llamada3) + ' minutos' + '\nCosto: $' + str(cd.costoLlamada(tiempo_de_llamada3)) + '\n')

#%% [markdown]
# ## Ejercicio 10
# Desarrolle una funci´on que reciba un vector de n´umeros reales y un n´umero real x, tal que
# indique el porcentaje de elementos mayores o iguales a un valor x.
#%%
y = [12, 4, 9, 7, 20, 32, 1, 6, 8, 15]
x = 10

print('Dada la lista: \n' + str(y) + '\n El porcentaje de números mayores o iguales a ' + str(x) + ' es: ' + str(cd.porcenjeMayores(y, x)) + '%')

#%% [markdown]
# ## Ejercicio 11
# Desarrolle una funci´on que reciba un n´umero natural n (suponiendo que n > 1) y que construya
# y retorne un vector v de tama˜no n tal que vk = vk−1/3 + 0,5 para k = 2, . . . , n y si endo que v1 = 1.
#%%
n = 8
print('Para un valor de n = ' + str(n) + '\nLos valores de k serían: \n' + str(cd.numNatural(n)))

#%% [markdown]
# ## Ejercicio 12
# Desarrolle una funci´on que recibe una matriz cuadrada A de tama˜no n × n y calcula su traza,
# es decir, la suma de los elementos de la diagonal. Por ejemplo, la traza de la siguiente matriz:
#%%
A = [[9,3,4],[1,3,-1],[4,12,-2]]

print('La traza de la matriz: \n' + str(A) + '\n Es: ' + str(cd.traza(A)))

#%% [markdown]
# ## Ejercicio 13
# Desarrolle una funci´on en Python que recibe un DataFrame que retorna la cantidad de entradas
# de este DataFrame que son divisibles entre 2
#%%
DF = pd.read_csv("datos.csv", delimiter=';', decimal=',')

print('Dado el DataFrame: \n\n' + str(DF) + '\n\nLa cantidad de numeros divisibles entre 2 es: ' + str(cd.cantPares(DF)))

#%% [markdown]
# ## Ejercicio 14
# Desarrolle una funci´on en Python que recibe un DataFrame y dos n´umeros de columna y que
# retorna en un diccionario con el nombre de las variables correspondientes a las columnas, la
# covarianza y la correlaci´on entre esas dos variables
#%%
DF2 = pd.read_csv("EjemploEstudiantes.csv", delimiter=';', decimal=',')
print(cd.estadisticas(DF2, 1, 3))