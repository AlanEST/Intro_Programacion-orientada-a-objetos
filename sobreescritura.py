#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:27:48 2023

@author: alaneduardosuareztorres
"""

class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a ", self.nombre, "de", self.edad)

    def hablar(self, *palabras):
        for contador in palabras:
            print(self.nombre, ":" ,contador)
            

class Deportista(Persona):
    
    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.deporte = deporte
        print("Se ha creado a ", self.nombre, "de", self.edad)
    
    def practicarDeporte(self):
        print(self.nombre, "voy a practicar")
# instancia del objeto
juan = Persona(18, "Juan")  
juan.hablar("Hola estoy hablando", "este soy yo")
luis = Deportista(20, "Luis","natacion") #ahora el objeto luis es una instancia de la 
#clase Deportista
## ahora la instancia luis de la clase Deportista acepta 3 paramatros
## debido a que el constructor de la clase Persona está sobreescrito
## Ademas el metodo hablar sigue siendo el mismo heredado de Persona
luis.hablar("Hola estoy hablando", "este soy yo")
luis.practicarDeporte()
print("Luis voy a practicar", luis.deporte)