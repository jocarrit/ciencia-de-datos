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
