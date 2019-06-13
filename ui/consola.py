#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from controladores.controlador import Controlador
"""
Created on Wed Jun 12 21:44:37 2019

@author: jhon
"""

class Consola (object):
    
    def __init__(self,controlador):
        self.controlador = Controlador()
    
    def entrada_nivel_operacion(self,operacion):
        return {
                '1':1,#Nivel Avanzado
                '2':self.elegir_operacion_basica(),#Nivel basico
                '3':3,#Suma de fasores
                }.get(operacion,'Elegir Nivel de operacion correcta')
        
    def entrada_operacion_basica(self,operacion):
        return {
                '1':self.ingresar_2_complejos(operacion),#Suma
                '2':2,#Resta
                '3':3,#Multiplicacion
                '4':4#Division
                }.get(operacion,'Elegir operacion basica correcta')
   
    def realizar_operacion(self,operacion,complejo1,complejo2):
        return {
                '1':self.sumar_complejos(operacion,complejo1,complejo2),#Suma
                '2':2,#Resta
                '3':3,#Multiplicacion
                '4':4#Division
                }.get(operacion,'Elegir operacion basica correcta')

    def input_usuario(self):
        """El usuario ingresa los valores para calcular """
        while True:
            input_complejo =  self.elegir_nivel_operacion()
            print(self.entrada_nivel_operacion(input_complejo))
            
    def main(self):
        self.input_usuario()
        
    def elegir_operacion_basica(self):
        """Elegir el tipo de operacion, suma, resta, multiplicacion"""
        input_operacion = input('\nElegir operacion\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n')
        self.entrada_operacion_basica(input_operacion)
        #validar de elegir el correcto numero de operacion basico
       # return input_operacion
        
    def elegir_nivel_operacion(self):
        """Elegir nivel basico o avanzado"""
        print("Elegir Nivel de operacion\n")
        input_nivel_operacion = input('1. Avanzado\n2. Basico\n3. Suma de fasores\n')
        #Validar el nivel de operacion exacto
        return input_nivel_operacion
    
    def elegir_operacion_avanzada(self):
        """Elegir el tipo de operacion avanzada, potencia, radiacion"""
        input_operacion_avanzada = input('Elegir operacion 1. Potencia 2.Radicacion\n')
        #Validar el nivel de operacion exacto
        return input_operacion_avanzada
    
    def ingresar_2_complejos(self,operacion):
        print('\n\n')
        print('Ingresar 2 complejos\nDebe respetar el formato adecuado,  Binomica y Polar\n')
        print('Para el formato Binomica debe escribir: (a,b)\nDonde a(Real) y b(imaginaria) representa el numero complejo')
        print('Para el formato Polar debe escribir: [a,b]\nDonde a(modulo) y b(angulo) representan el numero complejo')
        #validar el complejo 2
        #Luego trasnformar segun el caso
        formato = True
        while formato:
           
           input_complejo1 = input('Ingresar el primer complejo o escriba r para regresar a las operaciones\n ')
           
           if input_complejo1 == 'r':
               formato = True
               break
               
           if input_complejo1[0] == '(':
              formato_valido_c1 = self.controlador.validar_entrada_bin(input_complejo1)
           else:
               formato_valido_c1 = self.controlador.validar_entrada_polar(input_complejo1)
           
           input_complejo2 = input('Ingresar el segundo complejo o precione la tecla r para regresar a las operaciones\n')
           
           if input_complejo2 == 'r':
               formato = True
               break
           
           if input_complejo2[0] == '(':
               formato_valido_c2 = self.controlador.validar_entrada_bin(input_complejo2)
           else:
               formato_valido_c2 = self.controlador.validar_entrada_polar(input_complejo2)
               
           

           if formato_valido_c1 == False and  formato_valido_c2 == False: # salida del usuario para regresar
              formato = False
              break
            
           print('Escriba nuevamente el formato correcto o presione la tecla  r para salir\n')
        
        if formato == False: #ingreamos la operacion elegida
               self.aplicar_operacion_basicas(operacion,input_complejo1,input_complejo2)

    
    def aplicar_operacion_basicas(self,operacion,complejo1,complejo2):
         """Suma 2 complejos"""
         nuevo_complejo =  self.controlador.sumar_binomicos(operacion,complejo1,complejo2)
         print('Resultado real,imaginaria',nuevo_complejo.real,nuevo_complejo.img)
             
         