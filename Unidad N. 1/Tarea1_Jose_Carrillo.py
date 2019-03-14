# -*- coding: utf-8 -*-
"""
Tarea 1

Jose Manuel Carrillo Angulo
"""
import numpy as np

##########   Ejercicio 1   ##########
 
# a) Resultado

# ---------- (1) -------------
pi = np.pi

r = (pi**2) * (6**3) - np.sqrt(40)
print(r) 

# ---------- (2) ------------- 

r = abs(12 - 17 * (2/3) - 9)
print(r)

# ---------- (3) -------------

r = np.math.factorial(4)
print(r)

# --------- (4) --------------

r = np.math.log(19, 7)
print(r)

# --------- (5) --------------

r = np.math.log10(5)
print(r)

# --------- (6) --------------

e = np.e

r = e ** 5
print(r)

# b) Calcule el valor de x

y = 9
z = np.pi

x = (1 + y) / (1 + 2*z**2)
print(x)

# c) Calcule el  valor de z

x = 10
y = 4 * np.pi

z = np.math.sqrt(x**2 + y**2)
print(z)

##########   Ejercicio 2   ##########

# a) listas

x = np.array([0, 3, -5, 31, -1, -9, 10, 0, 18, 90])
y = np.array([9, 1, 1, -3, 1, -99, -10, 10, -7, -1])

# b) Calcule la media, la varianza y la desviacion estandar de y.

mediaY = np.mean(y)
varianzaY = np.var(y)
desviacionEstY = np.std(y)

print("Media de Y: " + str(mediaY))
print("Varianza de Y: " + str(varianzaY))
print("Desviacion estandar de Y: " + str(desviacionEstY))  

# b) Calcule la media, la varianza y la desviacion estandar de x.

mediaX = np.mean(x)
varianzaX = np.var(x)
desviacionEstX = np.std(x)

print("Media de X: " + str(mediaX))
print("Varianza de X: " + str(varianzaX))
print("Desviacion estandar de X: " + str(desviacionEstX))

# c) Calcule la correlacion entre 'x' y 'y'.

corr = np.correlate(x, y)
print("La correlacion entre 'x' y 'y' es: " + str(corr[0]))

# d) Extraer los valores en los ´ındices del 2 al 7 de x

res = x[2:8]
print(res)

# e) Extraer los valores de y excepto los situados en los ındices 2 y 7

res = np.delete(y, [2,7])

print(res)
print(y)

# f)  Extraer los valores de y menores a -3 o mayores a 10

res = y[ (y < -3) | (y > 10)]
print(res)

# g)  Extraer los valores de x mayores a 0 y que sean numeros pares

res = x[ (x > 0) & (x % 2 == 0 )]
print(res)

##########   Ejercicio 3   ##########
import pandas as pd

data1 = {'Peso' : [76, 67, 55, 55, 87, 48],
        'Edad' : [24, 44, 19, 21, 57, 13],
        'Nivel Educativo' : ["Lic", "Bach", "Bach", "Bach", "Dr", "MSc"]}

dtFrame1 = pd.DataFrame(data1)
print(dtFrame1)

##########   Ejercicio 4   ##########

data2 = {'id' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'calificacion': ["B", "C", "B", "A", "A", "A", "C", "B", "A", "B"],
         'duracion' : [66, 85, 79, 83, 80, 78, 68, 82, 89, 61]}

dtFrame2 = pd.DataFrame(data2)

dtFrame2.info()

##########   Ejercicio 5   ##########

x = np.array([24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40])

# a) Indices de los valores o entradas del vector cuya divisi´on entre 2 tiene como resultado 45

res = np.where(x/2 == 45)
print(res)

# b) Indice del valor mas alto del vector

res = np.where(x == np.amax(x))
print(res)

# c) resultado de la suma de los valores (entradas del vector) menores a la media del vector.

res = np.sum(x[x < np.median(x)])
print(res)

# d) cuales los valores del vector que son mayores a la media del vector y que sean divisibles entre 2.

res = x[(x > np.median(x)) & (x % 2 == 0)]
print(res)

##########   Ejercicio 6   ##########

v1 = np.array([2, 7, 6, 4, 52])
v2 = np.array([7, 5, 7, 0, 1])
v3 = np.array([2, 4, 3, 5, 6])

sum1 = np.sum(v1)
sum2 = np.sum(v2)
sum3 = np.sum(v3)

print("v1: " + str(sum1) + "\n v2: " + str(sum2) + "\n v3: " + str(sum3))

sumf1 = 0
sumf2 = 0
sumf3 = 0


for i1 in v1:
    sumf1 = sumf1 + i1
    
for i2 in v2:
    sumf2 = sumf2 + i2

for i3 in v3:
    sumf3 = sumf3 + i3
    
print("v1: " + str(sumf1) + "\n v2: " + str(sumf2) + "\n v3: " + str(sumf3))

##########   Ejercicio 7   ##########

x = np.array([24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40])

media = np.median(x)
maximo = np.max(x)
minimo = np.min(x)
de = np.std(x)

data = {'Media: ' : [media],
        'Maximo: ' : [maximo],
        'Minimo: ' : [minimo]}

lista1 = pd.DataFrame(data)

print(lista1)

##########   Ejercicio 8   ##########

a1 = np.array([9, 3, 4, 1, 3, -1, 0, 0, -10]).reshape(3, 3)
a2 = np.array([91, -3, 6, 1, 8, 0, -4, 5, -3]).reshape(3, 3)

res = a1 + 2*np.transpose(a2)

print(res)

##########   Ejercicio 9   ##########

import os

os.chdir("C:/Users/jocarr3/Documents/projects/ciencia de datos python/Unidad N. 1/datos")
print(os.getcwd())

# Cargue en un DataFrame el archivo titanic.csv

titanic = pd.read_csv("titanic.csv", delimiter=',', decimal='.', index_col=0)

# a) Calcule la dimensi´on de la Tabla de Datos.

print(titanic.shape)

# b) Despliegue las primeras 2 columnas de la tabla de datos.

print(titanic.loc[:,['Survived']])

# c) Ejecute un info() de los datos.

print(titanic.info())

# d) Calcule la Media para dos variables cualesquiera.

medianAge = titanic['Age'].median()
print(medianAge)

##########   Ejercicio 10   ##########

heart = pd.read_csv("SAheart.csv", delimiter=';', decimal='.')

# a) Calcule la dimensi´on de la Tabla de Datos.

print(heart.shape)

# b) Despliegue las primeras 3 columnas de la tabla de datos

print(heart.loc[:,['sbp','tobacco','ldl']])

# c) Ejecute un info() de los datos.

print(heart.info())

# d) Calcule la suma de las columnas con variables cuantitativas (num´ericas).

print("SBP: "+ str(sum(heart.loc[:,'sbp'])))
print("Tobacco: "+ str(sum(heart.loc[:,'tobacco'])))
print("LDL: "+ str(sum(heart.loc[:,'ldl'])))
print("Adiposity: "+ str(sum(heart.loc[:,'adiposity'])))
print("Type a: "+ str(sum(heart.loc[:,'typea'])))
print("Obesity: "+ str(sum(heart.loc[:,'obesity'])))
print("alcohol: "+ str(sum(heart.loc[:,'alcohol'])))
print("Age: "+ str(sum(heart.loc[:,'age'])))

# e) Calcule para todas las variables cuantitativas presentes en el archivo SAheart.csv: El
# m´ınimo, el m´aximo, la media, la mediana y para la variables chd determine la cantidad
# de Si y de No.

print("Mediana")
print("SBP: "+ str(heart['sbp'].min()))
print("Tobacco: "+ str(heart['tobacco'].min()))
print("LDL: "+ str(heart['ldl'].min()))
print("Adiposity: "+ str(heart['adiposity'].min()))
print("Type a: "+ str(heart['typea'].min()))
print("Obesity: "+ str(heart['obesity'].min()))
print("alcohol: "+ str(heart['alcohol'].min()))
print("Age: "+ str(heart['age'].min()))

print("Mediana")
print("SBP: "+ str(heart['sbp'].max()))
print("Tobacco: "+ str(heart['tobacco'].max()))
print("LDL: "+ str(heart['ldl'].max()))
print("Adiposity: "+ str(heart['adiposity'].max()))
print("Type a: "+ str(heart['typea'].max()))
print("Obesity: "+ str(heart['obesity'].max()))
print("alcohol: "+ str(heart['alcohol'].max()))
print("Age: "+ str(heart['age'].max()))

print("Mediana")
print("SBP: "+ str(heart['sbp'].median()))
print("Tobacco: "+ str(heart['tobacco'].median()))
print("LDL: "+ str(heart['ldl'].median()))
print("Adiposity: "+ str(heart['adiposity'].median()))
print("Type a: "+ str(heart['typea'].median()))
print("Obesity: "+ str(heart['obesity'].median()))
print("alcohol: "+ str(heart['alcohol'].median()))
print("Age: "+ str(heart['age'].median()))

print("Media")
print("SBP: "+ str(heart['sbp'].mean()))
print("Tobacco: "+ str(heart['tobacco'].mean()))
print("LDL: "+ str(heart['ldl'].mean()))
print("Adiposity: "+ str(heart['adiposity'].mean()))
print("Type a: "+ str(heart['typea'].mean()))
print("Obesity: "+ str(heart['obesity'].mean()))
print("alcohol: "+ str(heart['alcohol'].mean()))
print("Age: "+ str(heart['age'].mean()))

##########   Ejercicio 11   ##########

notas = np.array([91, 45, 89])
promedio = np.mean(notas)

if promedio > 67.5 :
        print("Ganó el curso")

if promedio >= 47.5 < 67.5:
        print("Extraordinario")

if promedio < 47.5:
        print("Perdió el curso")

##########   Ejercicio 12   ##########

li = np.array([-9,-45,0,7,45,-100,89])

pos = np.sum(li[li > 0])
neg = np.sum(np.abs(li[li < 0]))

if pos > neg:
        print(pos)
else:
        print(neg)

##########   Ejercicio 13   ##########

print(np.sum(np.arange(101)))

##########   Ejercicio 14   ##########

a = 4
b = 3

if a > b:
        print("b es menor")
if b > a:
        print("a es menor")

##########   Ejercicio 15   ##########

A = 5
B = 7
C = 3

if A < B and A < C:
        print("A es el menor")
if B < A and B < C:
        print("B es el menor")
if C < A and C < B:
        print("C es el menor")

##########   Ejercicio 16   ##########

n1 = 1
n2 = 2
n3 = 3
n4 = 4

if n1 > n2 and n1 > n3 and n1 > n4:
        print("n1 es el mayor")
if n2 > n1 and n2 > n3 and n2 > n4:
        print("n2 es el mayor")
if n3 > n1 and n3 > n2 and n3 > n4:
        print("n3 es el mayor")
if n4 > n1 and n4 > n2 and n4 > n3:
        print("n4 es el mayor")

##########   Ejercicio 17   ##########

n = 3
sum = 1

for x in range(1,n):
        sum = sum + x

print(sum)

##########   Ejercicio 18   ##########

n = 5
sum = 0

for x in range(1,n):
        if x%2 == 0: sum = sum + x

print(sum)

##########   Ejercicio 19   ##########

n = 11
sum = 0

for x in range(1,n):
        if x%5 == 0: sum = sum + x

print(sum)

##########   Ejercicio 20   ##########

rand = np.random.randint(1, 501, 200)
print(rand)
print(rand[(rand >= 50) & (rand <= 450)])
