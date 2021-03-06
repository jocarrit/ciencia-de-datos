"""
Modulo de funciones de ciencia de datos
@autor Jose Manuel Carrillo
"""
import numpy as np
import pandas as pd

def obtenerMayor(a ,b):
    """Devuelve el numero mayor de dos argumentos, si son iguales devuelve None
    
    Arguments:
        a {[int]} 
        b {[int]}
    Returns:
        int | None
    """

    if (a > b):
        return a
    elif(b > a):
        return b
    else:
        return None

def obtenerMayor3(a, b, c):
    """Devuelve el numero mayor de tres argumentos, si son iguales devuelve None
    
    Arguments:
        a {[int]} 
        b {[int]}
        c {[int]}
    Returns:
        int | None
    """

    if(a == b and b == c):
        return None
    elif (a > b and a > c):
        return a
    elif(b > c):
        return b
    else:
        return c

def obtenerMayor4(a, b, c, d):
    """Devuelve el numero mayor de cuatro argumentos, si son iguales devuelve None
    
    Arguments:
        a {[int]} 
        b {[int]}
        c {[int]}
        d {[int]}
    Returns:
        int | None
    """
    if(a == b and b == c and c == d):
        return None
    elif(a > b and a > c and a > d):
        return a
    elif(b > c and b > d):
        return b
    elif(c > d):
        return c
    else:
        return d

def sumatoria(n):
    """Devuelve la sumatoria de numeros enteros de 1 hasta n
    
    Arguments:
        n {int} -- límite de sumatoria
    """
    sum = 0
    for i in range(1, n+1):
        sum = sum + i**2
    return sum

def sumatoriaMult3(n):
    """Devuelve la sumatoria de numeros enteros multiplos de 3 de 1 hasta n
    
    Arguments:
        n {int} -- límite de sumatoria
    """
    sum = 0
    for i in range(1, n+1):
        if(i%3 == 0):
            sum += i
    return sum

def randomRango():
    """Genera 2000 numeros al azar entre 5000 y 2000 y devuelve los que esten entre 1500 y 4000
    
    Returns:
        rand {list}
    """
    rand = np.random.randint(1, 5000, 2000)

    return rand[(rand >= 1500) & (rand <= 4000)]

def promedio(lista):
    """devuelve el promedio de una lista dada
    
    Arguments:
        lista {list} -- Lista de numeros enteros
    Returns:
        promedio {float}
    """
    sum = 0
    for n in lista:
        sum += n

    return sum/len(lista)   

def varianza(lista):
    """devuelve la varianza de una lista\
    
    Arguments:
    lista {list}

    Returns:
    varianza {int}
    """
    prom = promedio(lista)
    return promedio([(i - prom)**2 for i in lista])

def costoLlamada(t):
    """devuelve el costo de la llamada en funcion de t
    
    Arguments:
    t {int}
    Returns:
    costo {int}
    """    

    if (t < 1):
        return 0.4
    else:
        return 0.4 + (t -1)/4

def porcenjeMayores(lista, referencia):
    """devuelve el porcentaje de numeros mayores a la referencia, con base a una lista de numeros enteros

    Arguments:
    lista {list}
    referencia {int}

    Returns:
    porcentaje {float}
    """

    contador = 0

    for i in lista:
        if i >= referencia:
            contador += 1
        
    return (contador/len(lista))*100

def numNatural(n):
    """construye un vector de longitud n y lo llena con numeros naturales pasados por una formula
    
    Arguments:
        n {[int]} 
    Returns:
        k {list}
    """
    k = []
    for i in range(1, n):
        k.append(((i - 1)/3) + 0.5)
    
    return k

def traza(m):
    """Calcula la traza de una matriz
    
    Arguments:
        m {[array]} 
    
    Returns:
        [int] 
    """

    return np.trace(m)

def cantPares(DF):
    """Devuelve la cantidad de Pares de un Data Frame
    
    Arguments:
        DF {[dataframe]}
    """
    n = DF.shape[0]
    m = DF.shape[1]
    
    contador = 0
    for i in range(n):
        for j in range(m):
            if DF.iloc[i,j] % 2 == 0:
                contador = contador + 1
    return contador

def estadisticas(DF, col1, col2):
    """Devuleve el nombre de variable, la covarianza y la correlacion de dos columnas de un Dataframe
    
    Arguments:
        DF  {[pandas.DataFrame]}
        col1    {[int]}
        col2    {[int]}

    Returns:
        dictionaire
    """

    return {'Columna 1' : DF.columns.values[col1],
            'Columna 2' : DF.columns.values[col2],
          'Covarianza 1' : np.cov(DF.iloc[:,col1]),
          'Covarianza 2' : np.cov(DF.iloc[:,col2]),
          'Correlacion' : np.correlate(DF.iloc[:,col1], DF.iloc[:,col2])}
    
def maximos(DF):
    f = DF.shape[0]
    c = DF.shape[1]
    
    maxFilas = []
    maxCol = []



    for i in range(c):
        max = DF.iloc[0,c]
        for j in range(f):
            if j > max:
                max = DF.iloc[]
