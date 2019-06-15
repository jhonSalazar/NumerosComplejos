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
    
    def convertir_complejo_bin(self,binomico1):
        binomico1_c1 = self.armar_formato_binomica(binomico1)
        binomico_complejo1 = self.crear_complejo_binomico(binomico1_c1[0],binomico1_c1[1])
        return binomico_complejo1
    
    def convertir_complejo_polar(self,binomico2):
        binomico1_c2 = self.armar_formato_polar(binomico2)
        binomico_complejo2 = self.crear_compejo_polar(binomico1_c2[0],binomico1_c2[1])
        return binomico_complejo2
        
    def convertir_complejos(self,operacion,binomico1,binomico2):
        
        es_binomico = self.validar_entrada_bin(binomico1)
        if not es_binomico: # si el primer compleo viene en forma binomica ingresamos
             binomico_complejo1 = self.convertir_complejo_bin(binomico1)
             es_binomico = True
             es_binomico = self.validar_entrada_bin(binomico2)
             if not es_binomico:#si el segundo complejo viene en forma binomica ingresampos
                binomico_complejo2 = self.convertir_complejo_bin(binomico2)
               # return Operaciones.suma(binomico_complejo1,binomico_complejo2)
             else:#el segundo complejo caso vino en formato Polar, creamos en formato polar y sumamos ambos C1 y C2
                 binomico_complejo2 = self.convertir_complejo_polar(binomico2)
              #   return Operaciones.suma(binomico_complejo1,binomico_complejo2)
        else: # el primero complejo vino en foma polar
             binomico1_c1 = self.armar_formato_polar(binomico1)
             binomico_complejo1 = self.crear_compejo_polar(binomico1_c1[0],binomico1_c1[1])
             es_binomico = True
             es_binomico = self.validar_entrada_bin(binomico2)
             if not es_binomico:#si el segundo complejo viene en forma binomica ingresampos
                binomico1_c2 = self.armar_formato_binomica(binomico2)
                binomico_complejo2 = self.crear_complejo_binomico(binomico1_c2[0],binomico1_c2[1])
             #   return Operaciones.suma(binomico_complejo1,binomico_complejo2)
             else:#el segundo complejo caso vino en formato Polar, creamos en formato polar y sumamos ambos C1 y C2
                 binomico1_c2 = self.armar_formato_polar(binomico2)
                 binomico_complejo2 = self.crear_compejo_polar(binomico1_c2[0],binomico1_c2[1])
        self.binomico_complejo1 = binomico_complejo1
        self.binomico_complejo2 = binomico_complejo2
        
    def ejecutar_operacion_avanzada(self,operacion,complejo,exponente):
        es_binomico = self.validar_entrada_bin(complejo)
        if not es_binomico: # si el primer compleo viene en forma binomica ingresamos
            binomico_complejo1 = self.convertir_complejo_bin(complejo)
        else:
            binomico_complejo1 = self.convertir_complejo_polar(complejo)
                
        if operacion == '1':# Potencia
               return Operaciones.potencia(binomico_complejo1,exponente)
        if  operacion == '2': # raiz
               return Operaciones.raices(binomico_complejo1,exponente)
        if  operacion == '3': # raiz primitiva
               return Operaciones.raicesPrimitivas(binomico_complejo1,exponente)
        
    def ejecutar_operacion_basica(self,operacion,binomico1,binomico2):
        
        self.convertir_complejos(operacion,binomico1,binomico2)
        #Despues de validar elegimos la operacion, suma, resta, multiplicacion o division
        if operacion == '1':# suma
               return Operaciones.suma(self.binomico_complejo1,self.binomico_complejo2)
        if  operacion == '2': # resta
               return Operaciones.resta(self.binomico_complejo1,self.binomico_complejo2)
        if  operacion == '3':#multiplicacion
               return Operaciones.multiplicacion(self.binomico_complejo1,self.binomico_complejo2)
        if  operacion == '4':#Division
              return Operaciones.division(self.binomico_complejo1,self.binomico_complejo2) 
     
    def crear_complejo_binomico(self,real,imaginaria):
        c_real = float(real)
        c_imaginaria = float(imaginaria)
        return Complejo.CrearFormaBinomica(c_real,c_imaginaria)
    def crear_compejo_polar(self,modulo,angulo):
        c_modulo = float(modulo)
        c_angulo = float(angulo)
        return Complejo.CrearFormaPolar(c_modulo,c_angulo)
    
    def armar_formato_polar(self,forma_polar):
        forma_polar = forma_polar.replace('[','')
        forma_polar = forma_polar.replace(']','')
        forma_polar = forma_polar.split(',')
        return forma_polar
        
    def armar_formato_binomica(self,forma_binomica):
        forma_binomica = forma_binomica.replace('(','')
        forma_binomica = forma_binomica.replace(')','')
        forma_binomica = forma_binomica.split(',')
        return forma_binomica
        
  #  def crear_complejo_polar(self,modulo,angulo):
    def validar_entrada_bin(self,forma_binomica):
        """Validar el formato de binomica y validar que sean numericos"""
        # este caso es para ra evitar un solo numero ingresado en el formato
        
       
        if forma_binomica[0] == '(' and forma_binomica[len(forma_binomica)-1] == ')':
            forma_binomica = self.armar_formato_binomica(forma_binomica)
            try:
               forma_binomica[2]
            except IndexError:
              return True
            if not self.validar_numericos(forma_binomica[0]) and not self.validar_numericos(forma_binomica[1]):
                return False
        return True
            
    def validar_entrada_polar(self,forma_polar):
        """Validar el formato de polar y validar que sean numericos"""
       
        
        if forma_polar[0] == '[' and forma_polar[len(forma_polar)-1] == ']':
           forma_polar = self.armar_formato_polar(forma_polar)
           try:
             forma_polar[2]
           except IndexError:
             return True
           if not self.validar_numericos(forma_polar[0]) and not self.validar_numericos(forma_polar[1]):
                return False
        return True
            
        
    def validar_numericos(self,valor):
        """Validar que sean numeros"""
        try:
           float(valor)
           return False; # falso para cortar el while true anterior, es decir se ingreso el valor correcto
        except ValueError:
           print('Ingrese valores numericos por favor')
           return True# seguimos en el while true ya que se ingresaron incorrectamente los valores
    
    def validar_numericos_enteros(self,valor):
        """Validar que sean numeros"""
        try:
           int(valor)
           return False; # falso para cortar el while true anterior, es decir se ingreso el valor correcto
        except ValueError:
           print('Ingrese valores enteros unicamente')
           return True   
        
    