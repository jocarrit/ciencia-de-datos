from Base import Base

class Compra(Base):
    def __init__(self, codigo = 0, descripcion = "", monto = 0):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__monto = monto
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def monto(self):
        return self.__monto

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo
    
    @descripcion.setter
    def descripcion(self, nuevo_descripcion):
        self.__descripcion = nuevo_descripcion
    
    @monto.setter
    def monto(self, nuevo_monto):
        self.__monto = nuevo_monto
    
    def __str__(self):
         return "Código: %i \nDescripción: %s \nMonto: %f" % (self.codigo, self.descripcion, self.monto)
    
    def Captura(self):
        self.codigo = int(input("Código: "))
        self.descripcion = input("Descripción: ")
        self.monto = float(input("Monto: "))

    