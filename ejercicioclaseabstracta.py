#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:40:33 2023

@author: alaneduardosuareztorres
"""

from abc import ABCMeta, abstractmethod

class Transporte:
    __metaclass__ = ABCMeta
    
    def __init__(self, medio):
        self.medio = medio
        print("se ha creado", self.medio)
        
    @abstractmethod
    def avanzar(self, frase): pass
    
    def giraIzquierda(self):
        print("gira a la izquiera")
        
    def giraDerecha(self):
        print("gira a la derecha")
    
    @abstractmethod
    def detener(self): pass

class Maritimo(Transporte):
    
    def comenzarNavegar(self):
        print("voy a navegar")
    
    def avanzar(self):
        print("estoy navegando")
    def detener(self):
        print("he llegado a puerto")

class Terrestre(Transporte):
    
    def comenzarAndar(self):
        print("voy a correr")
    
    def avanzar(self):
        print("estoy corriendo")
        
barco = Transporte("soy un barco")
barco.avanzar("necesito avanzar")
barco.giraIzquierda()
barco.giraDerecha()
barco.detener()
barco2 = Maritimo("soy otro barco")
barco2.comenzarNavegar()
barco2.giraIzquierda()
barco2.giraDerecha()
barco2.detener()
auto = Terrestre("soy un automovil")
auto.comenzarAndar()
auto.giraIzquierda()
auto.giraDerecha()