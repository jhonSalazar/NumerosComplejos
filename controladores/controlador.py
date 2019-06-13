#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paquetes.complejo import Complejo
from paquetes.fasor import Fasor
from paquetes.operaciones import Operaciones
"""
Created on Wed Jun 12 21:47:34 2019

@author: jhon
"""

class Controlador(object):
    
    def sumar_binomicos(self,binomico1,binomico2):
        binomico1_c1 = self.armar_formato_binomica(binomico1)
        binomico1_c2 = self.armar_formato_binomica(binomico2)
        binomico_complejo1 = self.crear_complejo_binomico(binomico1_c1[0],binomico1_c1[1])
        binomico_complejo2 = self.crear_complejo_binomico(binomico1_c2[0],binomico1_c2[1])
        return Operaciones.suma(binomico_complejo1,binomico_complejo2)
        
    def crear_complejo_binomico(self,real,imaginaria):
        c_real = int(real)
        c_imaginaria = int(imaginaria)
        return Complejo.CrearFormaBinomica(c_real,c_imaginaria)
    
    def armar_formato_binomica(self,forma_binomica):
        forma_binomica = forma_binomica.replace('(','')
        forma_binomica = forma_binomica.replace(')','')
        forma_binomica = forma_binomica.split(',')
        return forma_binomica
        
  #  def crear_complejo_polar(self,modulo,angulo):
    def validar_entrada_bin(self,forma_binomica):
        """Validar el formato de binomica y validar que sean numericos"""
        if forma_binomica[0] == '(' and forma_binomica[len(forma_binomica)-1] == ')':
            forma_binomica = self.armar_formato_binomica(forma_binomica)
            if not self.validar_numericos(forma_binomica[0]) and not self.validar_numericos(forma_binomica[1]):
                return False
        return True
            
    def validar_entrada_polar(self,forma_polar):
        """Validar el formato de polar y validar que sean numericos"""
        if forma_polar[0] == '[' and forma_polar[len(forma_polar)-1] == ']':
           forma_polar = forma_polar.replace('[','')
           forma_polar = forma_polar.replace(']','')
           forma_polar = forma_polar.split(',')
           if not self.validar_numericos(forma_polar[0]) and not self.validar_numericos(forma_polar[1]):
                return False
        return True
            
        
    def validar_numericos(self,valor):
        """Validar que sean numeros"""
        try:
           valor_numerico = int(valor)
           return False; # falso para cortar el while true anterior, es decir se ingreso el valor correcto
        except ValueError:
           print('Ingrese valores numericos por favor')
           return True;# seguimos en el while true ya que se ingresaron incorrectamente los valores
        
        
    