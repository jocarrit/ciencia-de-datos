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
