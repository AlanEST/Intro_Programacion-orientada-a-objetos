#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:02:08 2023

@author: alaneduardosuareztorres
"""

## Variables de instancia

class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a ", self.nombre, "de", self.edad)
    
    def hablar(self, palabras):
        print(self.nombre, ":" ,palabras)

# instancia del objeto juan
juan = Persona(18, "Juan")  #clase persona
#ejecutar método
juan.hablar("Hola estoy hablando")

# instancia del objeto luis
luis = Persona(20, "Luis")
#ejecutar método
luis.hablar("Hola estoy hablando")