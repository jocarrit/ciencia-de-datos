from Factura import Factura #, FactuaCredito, FacturaContado
import os

class Lectura:
    def LeeDatosFactura(self):
        factura = Factura()
        os.system('clear') #os.system('cls') #en windows
        factura.Captura()
        return factura
    def LeeDatosFactuaCredito(self):
        factuaCredito = FactuaCredito()
        os.system('clear') #os.system('cls') #en windows
        factuaCredito.Captura()
        return factuaCredito
    def LeeDatosFacturaContado(self):
        facturaContado = FacturaContado()
        os.system('clear') #os.system('cls') #en windows
        facturaContado.Captura()
        return facturaContado
    