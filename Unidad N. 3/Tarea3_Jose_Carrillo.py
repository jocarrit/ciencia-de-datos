# -*- coding: UTF-8 -*-

#%% [markdown]
# # Tarea # 3
# ## Ejercicio 1
# Se supone que una Factura que tiene los siguientes atributos: nombre cliente,
# direccion cliente, monto total, porcentaje impuesto y un m´etodo total pagar
# = monto total + porcentaje impuesto * monto total. Programe una clase al estilo 
# propio de Python que tenga los atributos citados arriba como privados con sus 
# respectivos métodos para obtener y modificar dichos atributos.
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
# ### Instancia
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
# ### Instancia

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

#%%
class Vuelo(object):
    def __init__(numero, hora_salida, hora_llegada):
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
    def __init__(minimo_pasajeros):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__minimo_pasajeros = minimo_pasajeros
    
    @property
    def minimo_pasajeros(self):
        return self.__minimo_pasajeros
    
    @minimo_pasajeros.setter
    def minimo_pasajeros(self, nuevo_minimo_pasajeros):
        self.__minimo_pasajeros = nuevo_minimo_pasajeros

class Vuelo_Internacional(Vuelo):
    def __init__(pais_destino):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__pais_destino = pais_destino
    
    @property
    def pais_destino(self):
        return self.__pais_destino
    
    @pais_destino.setter
    def pais_destino(self, nuevo_pais_destino):
        self.__pais_destino = nuevo_pais_destino
    
class Vuelo_Carga(Vuelo):
    def __init__(peso_maximo):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__peso_maximo = peso_maximo
    
    @property
    def peso_maximo(self):
        return self.__peso_maximo
    
    @peso_maximo.setter
    def peso_maximo(self, nuevo_peso_maximo):
        self.peso_maximo = nuevo_peso_maximo

class Pasajero(object):
    def __init__(codigo, nombre, precio_boleto):
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
    def total_pagar(self):
        return self.__total_pagar
    
    @total_pagar.setter
    def total_pagar(self, nuevo_total):
        self.__total_pagar = nuevo_total
    
    

class Pasajero_Frecuente(Pasajero):

