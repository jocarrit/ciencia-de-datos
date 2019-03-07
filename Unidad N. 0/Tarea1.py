# -*- coding: utf-8 -*-
"""
Tarea 1

Jose Manuel Carrillo Angulo
"""
import numpy as np

# Ejercicio 1
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