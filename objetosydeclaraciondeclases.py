#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:48:25 2023

@author: alaneduardosuareztorres
"""

class Persona:
    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print("Se ha creado a ", self.nombre, "de", self.edad)


juan = Persona()