import os
#os.getcwd()
#os.chdir(r'c:\\Users\\jmc\\Documents\\Ciencia de datos con Python\\ciencia-de-datos\\Unidad N. 4\\Ejercicio1')
from Lectura import Lectura

class App:
    def __init__(self):
        self.__lista = list()
        self.__lec = Lectura()
    def __menu(self):
        os.system('cls') #en windows
        print(" ==================================================== ")
        print(" [1] Vuelo Local")
        print(" [2] Vuelo Internacional")
        print(" [3] Vuelo de Carga")
        print(" [4] Ver la Lista Polimórfica" )
        print(" [5] Borrar la Lista Polimórfica")
        print(" [6] Salir")
        print(" ==================================================== ")
        return input("> ")

    def __mostrarLista(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            print(15 * "*" + "\n")
                
    def principal(self):
        respuesta = ""
        while respuesta != "6":
            respuesta = self.__menu()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosVueloLocal())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosVueloInternacional())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatosVueloCarga())
            elif respuesta == "4":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar")
            elif respuesta == "5":
                self.__lista.clear()

prueba = App()
prueba.principal()