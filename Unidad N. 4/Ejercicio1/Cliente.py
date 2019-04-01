from Base import Base

class Cliente(Base):
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def direccion(self):
        return self.__direccion
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @direccion.setter
    def direccion(self, nuevo_direccion):
        self.__direccion = nuevo_direccion
    
    def __str__(self):
         return "Nombre de Cliente: %s\nDirección: %i" % (self.nombre, self.direccion)
    
    def Captura(self):
        self.nombre = input("Nombre de Cliente: ")
        self.direccion = input("Dirección: ")