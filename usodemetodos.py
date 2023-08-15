#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:57:39 2023

@author: alaneduardosuareztorres
"""

class Persona:
    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print("Se ha creado a ", self.nombre, "de", self.edad)
    
    def hablar(self, palabras):
        print(self.nombre, ":" ,palabras)

juan = Persona()
#ejecutar método
juan.hablar("Hola estoy hablando")