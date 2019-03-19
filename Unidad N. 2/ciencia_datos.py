"""
Modulo de funciones de ciencia de datos
@autor Jose Manuel Carrillo
"""

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

def randomRango(cantidad, entre, ):
    """Genera una cantidad de numeros al azar y devuelve
    
    Arguments:
        bajo {[type]} -- [description]
        alto {[type]} -- [description]
        cantidad {[type]} -- [description]
    """
