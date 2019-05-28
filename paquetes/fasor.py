#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 00:56:00 2019

@author: jhon
"""
import math

class Fasor(object):
    """ Clase que representa un fasor"""

    def __init__ ( self, amplitud = 0, frecuencia = 0, anguloInicial=0 ):
        """ Constructor con componentes del fasor, amplitud. frecuencia y angulo inicial """
        self.amplitud = amplitud
        self.frecuencia  = frecuencia
        self.anguloInicial = anguloInicial

    def igualfrecuencia(self,frecuencia2):
        return (self.frecuencia == frecuencia2)

    def crearParteReal(fasor):
        return fasor.amplitud * math.cos(fasor.anguloInicial) #recibe en radianes, multiplicamos directamente

    def crearParteImaginaria(fasor):
        return fasor.amplitud * math.sin(fasor.anguloInicial)
    
    def pasarACoseno(self):
        self.anguloInicial = self.anguloInicial - math.pi
        

        
        