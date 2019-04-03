from Base import Base
from Cliente import Cliente
from Compra import Compra

class Factura(Base):
    def __init__(self, nombreCliente = "", direccion = "", porcentajeImpuesto = 0.13, totalPagar = 0):
        self.__cliente = Cliente(nombreCliente, direccion)
        self.__porcentajeImpuesto = porcentajeImpuesto
        self.__numeroCompras = 0
        self.__lista = []
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def porcentajeImpuesto(self):
        return self.__porcentajeImpuesto
    
    @property
    def numeroCompras(self):
        return self.__numeroCompras
    
    @property
    def listaItems(self):
        return self.__lista
    
    @cliente.setter
    def cliente(self, nuevoCliente):
        self.__cliente = nuevoCliente
    
    @porcentajeImpuesto.setter
    def porcentajeImpuesto(self, nuevoImpuesto):
        self.__porcentajeImpuesto = nuevoImpuesto
    
    @numeroCompras.setter
    def numeroCompras(self, nuevoNumero):
        self.__numeroCompras = nuevoNumero
    
    @listaItems.setter
    def listaItems(self, nuevaLista):
        self.__lista = nuevaLista
    
    def montoTotal(self):
        suma = 0
        for compra in self.listaItems:
            suma = suma + compra.monto

        return suma
    
    def totalPagar(self):
        return self.montoTotal() + (self.porcentajeImpuesto * self.montoTotal())

    def __str__(self):
        s ="Nombre de Cliente: %s\nDireccion: %s\n\n=====Items=====\n"
        monto = self.montoTotal()

        for i in range(self.numeroCompras):
            s = s +"\n"+ str(self.listaItems[i]) + "\n"
        s = s + "\n================ \n\nMonto: %f \nImpuesto: %f \nTotal: %f \n"     
        
        return s % (self.cliente.nombre ,self.cliente.direccion, monto, (monto * self.porcentajeImpuesto), self.totalPagar())

    def Captura(self):
        self.cliente.Captura()
        self.numeroCompras = int(input("Cantidad de items: "))

        for i in range(self.numeroCompras):
            compra = Compra()
            compra.Captura()
            self.listaItems.append(compra)
        

class FacturaCredito(Factura):
    def __init__(self, nombreCliente = "", direccion = "", porcentajeImpuesto = 0.13, totalPagar = 0, plazo = 0):
        Factura.__init__(self, nombreCliente, direccion, porcentajeImpuesto)
        self.__plazoCredito = plazo
    
    @property
    def plazoCredito(self):
        return self.__plazoCredito
    
    @plazoCredito.setter
    def plazoCredito(self, nuevo_plazo):
        self.__plazoCredito = nuevo_plazo

    def __str__(self):
        s ="Factura de crédito \n\nNombre de Cliente: %s\nDireccion: %s\nPlazo de crédito: %i meses\n\n=====Items=====\n"
        monto = self.montoTotal()

        for i in range(self.numeroCompras):
            s = s +"\n"+ str(self.listaItems[i]) + "\n"
        s = s + "\n================ \n\nMonto: %f \nImpuesto: %f \nTotal: %f \n"
        return s % (self.cliente.nombre ,self.cliente.direccion, self.plazoCredito, monto, (monto * self.porcentajeImpuesto), self.totalPagar())

    def Captura(self):
        Factura.Captura(self)
        self.plazoCredito = int(input("Plazo del crédito en meses: "))

class FacturaContado(Factura):
    def __init__(self, nombreCliente = "", direccion = "", porcentajeImpuesto = 0.13, totalPagar = 0, descuento = 0):
        Factura.__init__(self, nombreCliente, direccion, porcentajeImpuesto)
        self.__porcentajeDescuento = descuento
    
    @property
    def descuento(self):
        return self.__porcentajeDescuento
    
    @descuento.setter
    def descuento(self, nuevo_descuento):
        self.__porcentajeDescuento = nuevo_descuento

    def __str__(self):
        s ="Factura de contado \n\nNombre de Cliente: %s\nDireccion: %s\n\n=====Items=====\n"
        monto = self.montoTotal()
        descuento = self.descuento * monto

        for i in range(self.numeroCompras):
            s = s +"\n"+ str(self.listaItems[i]) + "\n"
        s = s + "\n================ \n\nMonto: %f \nImpuesto: %f \nDescuento: %f \nTotal: %f \n"
        return s % (self.cliente.nombre ,self.cliente.direccion, monto, (monto * self.porcentajeImpuesto), descuento, (self.totalPagar() - descuento))

    def Captura(self):
        Factura.Captura(self)
        self.descuento = float(input("Porcentaje de descuento: "))