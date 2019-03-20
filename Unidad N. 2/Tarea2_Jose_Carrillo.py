# -*- coding: UTF-8 -*-


#%% [markdown]
# ## Imports
#%%
import os
import ciencia_datos as cd
import importlib
importlib.reload(cd)

#%% [markdown]
# ## Ejercicio 1
# Programe en Python una función que recibe dos valores, determinar cual de los dos valores es 
# el mayor y luego lo retorna (no puede usar la funcion max de Python).

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
print('Los numeros aleatorios generados entre 1500 y 4500 son: \n\n' + str(cd.randomRango()))


#%% [markdown]
# ## Ejercicio 7
# Desarrolle una funcion que calcula el promedio de una lista de numeros. No puede utilizar la
# funcion sum ni la funcion mean.

lista = [1,4,9,7,3,5,10,15,21,3]

print('Dada la lista de numeros enteros: \n\n' + str(lista) + '\n\nEl promedio es: ' + str(cd.promedio(lista)))

#%% [markdown]
# ## Ejercicio 8
# 