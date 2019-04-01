#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:50:40 2018

@author: oldemarrodriguez
"""
# Método endswith
# str.endswith(suffix[, start[, end]])
# Devuelve True si la cadena termina con el sufijo especificado; 
# de lo contrario, devuelve False 

class SuenaAudio:
    def __init__(self, nombre_archivo):
        if not nombre_archivo.endswith(self.ext):
            raise Exception("formato invalido")
        self.nombre_archivo = nombre_archivo

class SuenaMP3(SuenaAudio):
    ext = "mp3"
    def suena(self):
        print("Sonando {} como un mp3".format(self.nombre_archivo))

class SuenaWav(SuenaAudio):
    ext = "wav"
    def suena(self):
        print("Sonando {} como un wav".format(self.nombre_archivo))

class SuenaOgg(SuenaAudio):
    ext = "ogg"
    def suena(self):
        print("Sonando {} como un ogg".format(self.nombre_archivo))
        
   
ogg = SuenaOgg("archivo.ogg")
ogg.suena()

mp3 = SuenaMP3("archivo.mp3")
mp3.suena()

# El siguinte código da un error
# debido a que SuenaAudio.__init__ es capaz de chequear el tipo
# del archivo aún cuando en la misma clase no se define que podría ser
# Pero sí cuando la subclase llama el constructor
no_mp3 = SuenaMP3("archivo.ogg")



     