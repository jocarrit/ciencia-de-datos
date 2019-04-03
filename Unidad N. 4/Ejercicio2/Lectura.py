from Vuelo import Vuelo , VueloLocal, VueloInternacional, VueloCarga
import os

class Lectura:
    def LeeDatosVueloLocal(self):
        vuelo = VueloLocal()
        os.system('clear') #os.system('cls') #en windows
        vuelo.Captura()
        return vuelo
    def LeeDatosVueloInternacional(self):
        vueloInternacional = VueloInternacional()
        os.system('clear') #os.system('cls') #en windows
        vueloInternacional.Captura()
        return vueloInternacional
    def LeeDatosVueloCarga(self):
        vueloCarga = VueloCarga()
        os.system('clear') #os.system('cls') #en windows
        vueloCarga.Captura()
        return vueloCarga
    