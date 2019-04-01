# -*- coding: UTF-8 -*-

#%% [markdown]
# # Tarea # 3
# ## Ejercicio 1
# Se supone que una Factura que tiene los siguientes atributos: nombre cliente,
# direccion cliente, monto total, porcentaje impuesto y un metodo total pagar
# = monto total + porcentaje impuesto * monto total. Programe una clase al estilo 
# propio de Python que tenga los atributos citados arriba como privados con sus 
# respectivos métodos para obtener y modificar dichos atributos.
#%% [markdown]
# ### Imports
#%%
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir(r'c:\\Users\\jocarr3\\Documents\\projects\\ciencia de datos python\\Unidad N. 3')
#%% [markdown]
# ### Código de la Clase
#%%
class Factura(object):
    def __init__(self, nombre_cliente, direccion_cliente, monto_total):
        self.__nombre_cliente = nombre_cliente
        self.__direccion_cliente = direccion_cliente
        self.__monto_total = monto_total
        self.__porcentaje_impuesto = 0.13
    
    @property
    def nombre_cliente(self):
        return self.__nombre_cliente
    
    @nombre_cliente.setter
    def nombre_cliente(self, nuevo_nombre):
        self.__nombre_cliente = nuevo_nombre
    
    @property
    def direccion_cliente(self):
        return self.__direccion_cliente
    
    @direccion_cliente.setter
    def direccion_cliente(self, nueva_direccion):
        self.__direccion_cliente = nueva_direccion
    
    @property
    def monto_total(self):
        return self.__monto_total

    @monto_total.setter
    def monto_total(self, nuevo_monto):
        self.__monto_total = nuevo_monto

    @property
    def porcentaje_impuesto(self):
        return self.__porcentaje_impuesto

    @porcentaje_impuesto.setter
    def porcentaje_impuesto(self, nuevo_impuesto):
        self.__porcentaje_impuesto = nuevo_impuesto

    def total_pagar(self):
        return self.monto_total + self.monto_total*self.porcentaje_impuesto

#%% [markdown]
# ### Instancia y prueba
#%%
f = Factura("Guido V", "Palo Alto", 1000)
print(f"El monto total a pagar es c{f.total_pagar()}")

#%% [markdown]
# ## Ejercicio # 2
# Programe una clase en Python que tiene tres atributos (números) A, B, y C y 
# métodos para retornar el menor, el mayor, la suma de los tres y suma 
# cuadrados = A^2 + B^2 + C^2
# ### Código de la clase

#%%
class Mate(object):
    def __init__(self, A, B, C):
        self.__A = A
        self.__B = B
        self.__C = C

    @property
    def A(self):
        return self.__A

    @A.setter
    def A(self, new_A):
        self.__A = new_A

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, new_B):
        self.__B = new_B

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, new_C):
        print("entro")
        self.__C = new_C

    def menor(self):
        return min(self.A, self.B, self.C)

    def mayor(self):
        return max(self.A, self.B, self.C)

    def suma(self):
        return self.A + self.B + self.C

    def suma_cuadrados(self):
        return self.A**2 + self.B**2 + self.C**2

#%% [markdown]
# ### Instancia y pruebas

#%%
a = 4
b = 5
c = 6
m = Mate(a, b, c)
m.menor()
print(f"El menor entre {a}, {b} y {c} es : {m.menor()}")
print(f"El mayor entre {a}, {b} y {c} es : {m.mayor()}")
print(f"La suma entre {a}, {b} y {c} es : {m.suma()}")
print(f"La suma de cuadrados entre {a}, {b} y {c} es : {m.suma_cuadrados()}")


#%% [markdown]
# ## Ejercicio # 3
# Una línea aérea desea implementar un sistema para el control de sus vuelos, 
# para esto se cuenta con la siguiente información:
# * Se supone que un Vuelo tiene los siguientes atributos: Numero, Hora de Salida y Hora de
# Llegada.
# * Un Vuelo Local (USA) tiene ademas (respecto a un Vuelo) un Numero Mınimo de Pasajeros.
# * Un Vuelo Internacional tiene ademas (respecto a un Vuelo) un Paıs Destino.
# * Un Vuelo de Carga tiene ademas (respecto a un Vuelo) un Peso Maximo de carga soportado.
# * Un Pasajero tiene Codigo, Nombre, Precio Boleto, Porcentaje Impuesto y 
# Total a Pagar = Precio Boleto + Porcentaje Impuesto * Precio Boleto. Los pasajeros son de dos tipos:
# * los Pasajero Frecuente y los No Frecuentes, la diferencia es que a los pasajeros frecuentes 
# se les aplica un 20 % de descuento en el Total a Pagar.
# * La clase Vuelo Local incluye un atributo tipo Pasajero Frecuente mientras que la clase Vuelo 
# Internacional incluye un atributo tipo Pasajero.
# * Programe una Jerarquıa de Clases usando herencia que incluya al menos las clases: Vuelo, Vuelo 
# Local, Vuelo Internacional, Vuelo de Carga, Pasajero y Pasajero Frecuente.
# ### Código de la clase
#%%
class Pasajero(object):
    def __init__(self, codigo, nombre, precio_boleto):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio_boleto = precio_boleto
        self.__porcentaje_impuesto = 0.13
        self.__total_pagar = 0
    
    @property
    def codigo(self):
        return self.codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def precio_boleto(self):
        return self.__precio_boleto
    
    @precio_boleto.setter
    def precio_boleto(self, nuevo_precio):
        self.precio_boleto = nuevo_precio
    
    @property
    def porcentaje_impuesto(self):
        return self.__porcentaje_impuesto
    
    @property
    def total_pagar(self):
        return self.__total_pagar
    
    @total_pagar.setter
    def total_pagar(self, nuevo_total):
        nuevo_total = self.precio_boleto + self.porcentaje_impuesto*self.precio_boleto
        self.__total_pagar = nuevo_total
     
class Pasajero_Frecuente(Pasajero):
    def __init__(self, codigo, nombre, precio_boleto):
        super().__init__(codigo, nombre, precio_boleto)
        self.total_pagar = self.total_pagar*.2
    
    def describe(self):
        print(f"Código - {self.codigo} \n Nombre - {self.nombre}")

class Vuelo(object):
    def __init__(self, numero, hora_salida, hora_llegada):
        self.__numero = numero
        self.__hora_salida = hora_salida
        self.__hora_llegada = hora_llegada
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def hora_salida(self):
        return self.__hora_salida
    
    @property
    def hora_llegada(self):
        return self.__hora_llegada
    
    @numero.setter
    def numero(self, nuevo_numero):
        self.__numero = nuevo_numero

    @hora_salida.setter
    def hora_salida(self, nueva_hora_salida):
        self.__hora_salida = nueva_hora_salida
    
    @hora_llegada.setter
    def hora_llegada(self, nueva_hora_llegada):
        self.__hora_llegada = nueva_hora_llegada

class Vuelo_Local(Vuelo):
    def __init__(self, numero, hora_salida, hora_llegada, minimo_pasajeros, codigo, nombre, precio_boleto):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__minimo_pasajeros = minimo_pasajeros
        self.pasajero_frecuente = Pasajero_Frecuente(codigo, nombre, precio_boleto)

    
    @property
    def minimo_pasajeros(self):
        return self.__minimo_pasajeros
    
    @minimo_pasajeros.setter
    def minimo_pasajeros(self, nuevo_minimo_pasajeros):
        self.__minimo_pasajeros = nuevo_minimo_pasajeros

class Vuelo_Internacional(Vuelo):
    def __init__(self, numero, hora_salida, hora_llegada, pais_destino, codigo, nombre, precio_boleto):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__pais_destino = pais_destino
        self.pasajero = Pasajero(codigo, nombre, precio_boleto)
    
    @property
    def pais_destino(self):
        return self.__pais_destino
    
    @pais_destino.setter
    def pais_destino(self, nuevo_pais_destino):
        self.__pais_destino = nuevo_pais_destino
    
class Vuelo_Carga(Vuelo):
    def __init__(self, numero, hora_salida, hora_llegada, peso_maximo):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__peso_maximo = peso_maximo
    
    @property
    def peso_maximo(self):
        return self.__peso_maximo
    
    @peso_maximo.setter
    def peso_maximo(self, nuevo_peso_maximo):
        self.peso_maximo = nuevo_peso_maximo

#%% [markdown]
# ### Instancia y pruebas
#%%
now = datetime.now()
later = now + timedelta(hours=2)
print(format(now, '%Y-%m-%d %H:%M:%S'))
print(format(later, '%Y-%m-%d %H:%M:%S'))
vueloLocal = Vuelo_Local(1320, now, later, 10, 1, 'Jon', 400)

print(f"Informacion de vuelo local: \n\n")
print(f"Número - {vueloLocal.numero}\n")
print(f"Hora de salida - {vueloLocal.hora_salida}\n")
print(f"Hora de llegada - {vueloLocal.hora_llegada}\n")
print(f"Mínimo de Pasajeros - {vueloLocal.minimo_pasajeros}\n")

#%% [markdown]
# ## Ejercicio # 4
# Agregue a la clase class mi DF() vista en clase los siguientes metodos:
# * Retorna la cantidad de entradas de este DataFrame que son divisibles entre 3 
# * Recibe dos números de columna y que retorna en una lista con el nombre de las variables
# correspondientes a las columnas, la covarianza y la correlación entre esas dos variables
# ### Código de la clase
#%%
class mi_DF():
    def __init__(self, DF = pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF
    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def DF(self):
        return self.__DF  
    def maximo(self):
        max = self.DF.iloc[0,0]
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
        return max
    def valores(self):
        min = self.DF.iloc[0,0]
        max = self.DF.iloc[0,0]
        total_ceros = 0
        total_pares = 0
        divisibles3 = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
                if self.DF.iloc[i,j] < min:
                    min = self.DF.iloc[i,j]
                if self.DF.iloc[i,j] == 0:
                    total_ceros = total_ceros+1
                if self.DF.iloc[i,j] % 2 == 0:
                    total_pares = total_pares+1
                if self.DF.iloc[i,j] % 3 == 0:
                    divisibles3 = divisibles3+1
        return {'Maximo' : max, 'Minimo' : min, 'Total_Ceros' : total_ceros, 'Pares' : total_pares, 'Divisibles_entre_3' : divisibles3}
    def estadisticas(self,nc):
        media = np.mean(self.DF.iloc[:,nc])
        mediana = np.median(self.DF.iloc[:,nc])
        deviacion = np.std(self.DF.iloc[:,nc])
        varianza = np.var(self.DF.iloc[:,nc])
        maximo = np.max(self.DF.iloc[:,nc])
        minimo = np.min(self.DF.iloc[:,nc])
        return {'Variable' : self.DF.columns.values[nc],
                'Media' : media,
                'Mediana' : mediana,
                'DesEst' : deviacion,
                'Varianza' : varianza,
                'Maximo' : maximo,
                'Minimo' : minimo}
    
    def obtiene_corr_y_cof(self, c1, c2):
        return [self.DF.columns[c1], self.DF.columns[c2], self.covarianza(c1, c2), self.correlacion(c1, c2) ] 
    
    def correlacion(self, c1, c2):
        return np.corrcoef(self.DF.iloc[:, c1], self.DF.iloc[:, c2])
    
    def covarianza(self, c1, c2):
        return np.cov(self.DF.iloc[:, c1], self.DF.iloc[:, c2])
#%% [markdown]
# ### Instancia y pruebas
#%%
archivoEst = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",")
datos = mi_DF(archivoEst)
print(f"{archivoEst}\n\n")
print(f"La covarianza entre las Columnas {str(datos.obtiene_corr_y_cof(3,4)[0])} y {str(datos.obtiene_corr_y_cof(3,4)[1])} es:\n\n {str(datos.obtiene_corr_y_cof(3,4)[2])}\n\n")
print(f"La correlacion entre las Columnas {str(datos.obtiene_corr_y_cof(3,4)[0])} y {str(datos.obtiene_corr_y_cof(3,4)[1])} es:\n\n {str(datos.obtiene_corr_y_cof(3,4)[3])}\n\n")

#%% [markdown]
# ## Ejercicio # 4
# Desarrolle una clase denominada Matriz que tiene como atributos una matriz tipo numpy, el
# numero de filas y el numero de columnas. Ademas tiene metodos que calculan la suma total de
# la matriz, la suma de una fila dada (el numero de fila es un parametro del metodo), la suma
# de una columna dada (el numero de columna es un parametro del metodo), la suma de todas
# las entradas de la matriz en valor absoluto y a suma de todas las entradas de la matriz al
# cuadrado.
# ### Código de la clase
#%%
class Matriz():
    def __init__(self, mtx = np.matrix([])):
        self.__nf = mtx.shape[0]
        self.__nc = mtx.shape[1]
        self.__matrix = mtx
    
    @property
    def numero_filas(self):
        return self.__nf
    
    @property
    def numero_columnas(self):
        return self.__nc
    
    @property
    def matrix(self):
        return self.__matrix
    
    def suma_total(self):
        return self.matrix.sum()
    
    def suma_fila(self, fila):
        return self.matrix.sum(axis=1,)[fila]
    
    def suma_columna(self, columna):
        return self.matrix.sum(axis=0)[columna]
    
    def suma_valor_absoluto(self):
        return abs(self.matrix.sum())
    
    def suma_cuadrados(self):
        return self.matrix.sum()**2

#%% [markdown]
# ### Instancia y pruebas
#%%
mtx = np.matrix('1 8; 16 -2; 10 -8')
fila = 1
columna = 0
matrix = Matriz(mtx)

print(f"Dada la matriz: \n\n{str(mtx)}\n\n")
print(f"La suma de todos los elementos es: {matrix.suma_total()}")
print(f"La suma de los elementos de la fila {fila} es: {matrix.suma_fila(fila)}")
print(f"La suma de los elementos de la fila {fila} es: {matrix.suma_fila(fila)}")
print(f"La suma del valor absoluto de todos los elementos es: {matrix.suma_valor_absoluto()}")
print(f"La suma de los cuadrados de todos los elementos es: {matrix.suma_cuadrados()}")


