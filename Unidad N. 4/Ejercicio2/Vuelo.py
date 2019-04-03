from Base import Base
from Pasajero import Pasajero
import datetime 

class Vuelo(Base):
    
    def __init__(self, numero = 0, hora_salida = datetime.date.today(), hora_llegada = datetime.date.today()):
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
    def hora_salida(self, nuevo_hora_salida):
        self.__hora_salida = nuevo_hora_salida
    
    @hora_llegada.setter
    def hora_llegada(self, nuevo_hora_llegada):
        self.__hora_llegada = nuevo_hora_llegada
    
    def __str__(self):
        return "Número de Vuelo:%s\n Hora de Salida:%s\n Hora de Llegada:%s\n" % (self.numero, self.hora_salida, self.hora_llegada)

    def Captura(self):
        anio = [1,2]
        mes = [1,2]
        dia = [1,2]
        hora = [1,2]
        self.numero = input("Digite el número de vuelo: ")
        anio[0] = int(input("Digite la fecha y hora de salida: \n    año:"))    
        mes[0] = int(input("    mes: "))
        dia[0] = int(input("    día: "))
        hora[0] = int(input("    hora:"))
        anio[1] = int(input("Digite la fecha y hora de llegada: \n    año:"))    
        mes[1] = int(input("    mes: "))
        dia[1] = int(input("    día: "))
        hora[1] = int(input("    hora:"))

        self.hora_salida = datetime.datetime(anio[0], mes[0], dia[0], hora[0], 0, 0)
        self.hora_llegada = datetime.datetime(anio[1], mes[1], dia[1], hora[1], 0, 0) 


class VueloComercial(Vuelo):

    def __init__(self, numero = 0, hora_salida = datetime.date.today(), hora_llegada = datetime.date.today()):
        Vuelo.__init__(self, numero, hora_salida, hora_llegada)
        self.__lista = []

    @property
    def listaPasajeros(self):
        return self.__lista
    
    @listaPasajeros.setter
    def listaPasajeros(self, nueva_lista):
        self.__lista = nueva_lista
    
    def montoTotalVendido(self):
        suma = 0
        for pasajero in self.listaPasajeros:
            suma = suma + pasajero.totalPagar()

        return suma
    
    def Captura(self):
        Vuelo.Captura(self)
        self.numeroPasajeros = int(input("Cantidad de pasajeros: "))

        for i in range(self.numeroPasajeros):
            pasajero = Pasajero()
            pasajero.Captura()
            self.listaPasajeros.append(pasajero)
        
    def __str__(self):
        Vuelo.__str__(self)
        s = "\n\n=====Items=====\n"
        for i in range(self.numeroPasajeros):
            s = s +"\n"+ str(self.listaPasajeros[i]) + "\n"
        
        s = s + "\n================ \n\nMonto total vendido: %f"     
        
        return s % (self.montoTotalVendido())

    
class VueloLocal(VueloComercial):
    
    def __init__(self, numero = 0, hora_salida = datetime.date.today(), hora_llegada = datetime.date.today(), min_pasajeros = 0):
        VueloComercial.__init__(self, numero, hora_salida, hora_llegada)
        self.__min_pasajeros = min_pasajeros
        
    @property
    def min_pasajeros(self):
        return self.__min_pasajeros
    
    @min_pasajeros.setter
    def min_pasajeros(self, nuevo_min_pasajeros):
        self.__min_pasajeros = nuevo_min_pasajeros
    
    def __str__(self):
        s = "Vuelo Local \n\nNúmero de Vuelo:%s\n Hora de Salida:%s\n Hora de Llegada:%s\n Número mínimo de pasajeros: %i" 
        
        for i in range(self.numeroPasajeros):
            s = s +"\n"+ str(self.listaPasajeros[i]) + "\n"
        
        s = s + "\n================ \n\nMonto total vendido: %f"
        
        return s % (self.numero, self.hora_salida, self.hora_llegada, self.min_pasajeros, self.montoTotalVendido())

    def Captura(self):
        self.min_pasajeros = int(input("Vuelo Local \n\nMínimo de pasajeros: "))
        VueloComercial.Captura(self)


class VueloInternacional(VueloComercial):
    
    def __init__(self, numero = 0, hora_salida = datetime.date.today(), hora_llegada = datetime.date.today(), pais_destino = ""):
        VueloComercial.__init__(self, numero, hora_salida, hora_llegada)
        self.__pais_destino = pais_destino
    
    @property
    def pais_destino(self):
        return self.__pais_destino
    
    @pais_destino.setter
    def pais_destino(self, nuevo_pais_destino):
        self.__pais_destino = nuevo_pais_destino

    def __str__(self):
        s = "Vuelo Internacional \n\nNúmero de Vuelo:%s\n Hora de Salida:%s\n Hora de Llegada:%s\n País destino: %s" 
        
        for i in range(self.numeroPasajeros):
            s = s +"\n"+ str(self.listaPasajeros[i]) + "\n"
        
        s = s + "\n================ \n\nMonto total vendido: %f"
        
        return s % (self.numero, self.hora_salida, self.hora_llegada, self.pais_destino, self.montoTotalVendido())

    def Captura(self):
        self.pais_destino = input("Vuelo Internacional \n\n País destino: ")
        VueloComercial.Captura(self)

class VueloCarga(Vuelo):
    
    def __init__(self, numero = 0, hora_salida = datetime.date.today(), hora_llegada = datetime.date.today(), peso_maximo = 0):
        Vuelo.__init__(self, numero, hora_salida, hora_llegada)
        self.__peso_maximo = peso_maximo

    @property
    def peso_maximo(self):
        return self.__peso_maximo
    
    @peso_maximo.setter
    def peso_maximo(self, nuevo_peso_maximo):
        self.__peso_maximo = nuevo_peso_maximo

    def __str__(self):
        s = "Vuelo de Carga \n\nNúmero de Vuelo:%s\n Hora de Salida:%s\n Hora de Llegada:%s\n Peso Máximo: %ikg" 
        return s % (self.numero, self.hora_salida, self.hora_llegada, self.peso_maximo)

    def Captura(self):
        self.peso_maximo = int(input("Vuelo de Carga \n\n Peso Máximo: "))
        Vuelo.Captura(self)