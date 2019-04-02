from Factura import Factura , FacturaCredito, FacturaContado
import os

class Lectura:
    def LeeDatosFactura(self):
        factura = Factura()
        os.system('clear') #os.system('cls') #en windows
        factura.Captura()
        return factura
    def LeeDatosFacturaCredito(self):
        facturaCredito = FacturaCredito()
        os.system('clear') #os.system('cls') #en windows
        facturaCredito.Captura()
        return facturaCredito
    def LeeDatosFacturaContado(self):
        facturaContado = FacturaContado()
        os.system('clear') #os.system('cls') #en windows
        facturaContado.Captura()
        return facturaContado
    