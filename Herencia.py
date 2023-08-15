#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:20:32 2023

@author: alaneduardosuareztorres
"""
# Declarar una clase llamada Deportista que hereda el
# método hablar de la clase persona

class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a ", self.nombre, "de", self.edad)

    def hablar(self, *palabras):
        for contador in palabras:
            print(self.nombre, ":" ,contador)
            

class Deportista(Persona):
    
    def practicarDeporte(self):
        print(self.nombre, "voy a practicar")
# instancia del objeto
juan = Persona(18, "Juan")  
juan.hablar("Hola estoy hablando", "este soy yo")
luis = Deportista(20, "Luis") #ahora el objeto luis es una instancia de la 
#clase Deportista
luis.hablar("Hola estoy hablando", "este soy yo")
luis.practicarDeporte()