from Base import Base

class Pasajero(Base):
    
    def __init__(self, codigo = 0, nombre = "", precioTiquete = 0, porcentajeImpuesto = 0.13):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precioTiquete = precioTiquete
        self.__porcentajeImpuesto = porcentajeImpuesto
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precioTiquete(self):
        return self.__precioTiquete
    
    @property
    def porcentajeImpuesto(self):
        return self.__porcentajeImpuesto
    
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @precioTiquete.setter
    def precioTiquete(self, nuevo_precioTiquete):
        self.__precioTiquete = nuevo_precioTiquete
    
    @porcentajeImpuesto.setter
    def porcentajeImpuesto(self, nuevo_porcentajeImpuesto):
        self.__porcentajeImpuesto = nuevo_porcentajeImpuesto
    
    def totalPagar(self):
        return self.precioTiquete + (self.precioTiquete * self.porcentajeImpuesto)
    
    def Captura(self):
        self.codigo = int(input("Código: "))
        self.nombre = input("Nombre: ")
        self.precioTiquete = float(input("Precio de tiquete: "))
    
    def __str__(self):
        return "Código: %i \nNombre: %s \nPrecio Tiquete %f \nImpuesto: %f \nTotal: %f" % (self.codigo, self.nombre, self.precioTiquete, (self.porcentajeImpuesto * self.precioTiquete), self.totalPagar())

class PasajeroFrecuente(Pasajero):

    def __init__(self, codigo = 0, nombre = "", precioTiquete = 0, porcentajeImpuesto = 0.13, descuento = 0):
        Pasajero.__init__(codigo, nombre, precioTiquete, porcentajeImpuesto)
        self.__descuento = descuento
    
    @property
    def descuento(self):
        return self.__descuento
    
    @descuento.setter
    def descuento(self, nuevo_descuento):
        self.__descuento = nuevo_descuento
    
    def Captura(self):
        Pasajero.Captura(self)
        self.descuento = float(input("Descuento: ")) 
    
    def __str__(self):
        return "Pasajero Frecuente \n\nCódigo: %i \nNombre: %s \nPrecio Tiquete %f \nImpuesto: %f \nDescuento: %f \nTotal: %f" % (self.codigo, self.nombre, self.precioTiquete, (self.porcentajeImpuesto * self.precioTiquete), (self.totalPagar() * self.descuento), (self.totalPagar - self.totalPagar() * self.descuento))
