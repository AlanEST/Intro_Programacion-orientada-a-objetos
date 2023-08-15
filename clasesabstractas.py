#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:38:25 2023

@author: alaneduardosuareztorres
"""
from abc import ABCMeta, abstractmethod
class Persona:
    __metaclass__ = ABCMeta
    
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a ", self.nombre, "de", self.edad)

    @abstractmethod
    def hablar(self): pass
     
class Deportista(Persona): # implementación, Deportista es una imp. de persona
    
    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte
        print("Se ha creado a ", self.nombre, "de", self.edad)
    
    def practicarDeporte(self):
        print(self.nombre, "voy a practicar")
        
    def verMiDeporte(self):
        return(self.__deporte)
    
    def hablar(self, *palabras):
        for frase in palabras:
            print(self.nombre, ":", frase)

## si una clase abstracta tiene más de un método abstracto sus implementaciones
## deberán tener un definición para cada método.

# instancia del objeto

luis = Deportista(20, "Luis","natacion") #ahora el objeto luis es una instancia de la 
#clase Deportista
## ahora la instancia luis de la clase Deportista acepta 3 paramatros
## debido a que el constructor de la clase Persona está sobreescrito
## Ademas el metodo hablar sigue siendo el mismo heredado de Persona
luis.hablar("Hola estoy hablando", "este soy yo")
luis.practicarDeporte()
print("Luis voy a practicar", luis.verMiDeporte())