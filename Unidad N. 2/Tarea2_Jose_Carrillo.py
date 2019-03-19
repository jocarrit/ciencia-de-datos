# -*- coding: UTF-8 -*-

#%% [markdown]
# ## Ejercicio 1
# Programe en Python una función que recibe dos valores, determinar cual de los dos valores es 
# el mayor y luego lo retorna (no puede usar la funci´on max de Python).

#%%
import ciencia_datos as cd
import importlib
importlib.reload(cd)

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
# Programe en Python una funci´on que recibe cuatro n´umeros y retorna el mayor (no puede usar
# la funci´on max de Python).
#%%
W = 100
X= 200
Y = 670
Z = 810

print('El Mayor entre ' + str(W) + ' , ' + str(X) + ' , ' + str(Y) + ' y ' + str(Z) + ' es: ' + str(cd.obtenerMayor4(W, X, Y, Z)))

#%% [markdown]
# ## Ejercicio 4
# Programe en Python una funci´on que recibe un n´umero n y retorna la sumatoria de los n´umeros
# enteros al cuadrado comprendidos entre el 1 y el n.
#%%
n = 4
print('La sumatoria de enteros al cuadrado de 1 hasta ' + str(n) + ' es: ' + str(cd.sumatoria(n)))

#%% [markdown]
# ## Ejercicio 5
# Desarrolle una funci´on que realice la sumatoria de los n´umeros enteros m´ultiplos de 3, comprendidos entre el 1 y el n.
#%%
n = 9
print('La sumatoria de enteros multiplos de 3 desde 1 hasta ' + str(n) + ' es: ' + str(cd.sumatoriaMult3(n)))

#%% [markdown]
# ## Ejercicio 6
# Programe en Python una funci´on que genera 2000 n´umeros al azar entre 1 y 5000 y luego calcula
# cu´antos est´an entre el 1500 y 4500, ambos inclusive.