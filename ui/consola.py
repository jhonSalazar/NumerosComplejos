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

    def entrada_operacion_basica(self,operacion):
        """Se realizan las operaciones basicas """
        if not self.ingresar_2_complejos(operacion):
            self.aplicar_operacion_basicas(operacion,self.formato_complejo1,self.formato_complejo2)
    
    def entrada_operacion_avanzada(self,operacion):
        """Se realizan las operaciones avanzadas """
        if not self.ingresar_1_complejo(operacion):
            self.aplicar_operacion_avanzadas(operacion,self.formato_complejo1,self.exponente)
            
    def elegir_operacion_avanzada(self):
        """Elegir el tipo de operacion avanzada, potencia, radiacion"""
       
        while True:
            input_operacion_avanzada = input('Elegir operacion\n1. Potencia\n2. Radicacion\n3. Raices primitivas\n')
            if input_operacion_avanzada == '1':
                break
            elif input_operacion_avanzada == '2':
                break
            elif input_operacion_avanzada == '3':
                break
            else: 
               print('Elegir la correcta operacion avanzada') 
            
        self.entrada_operacion_avanzada(input_operacion_avanzada)
        
    
    def input_usuario(self):
        """El usuario ingresa los valores para calcular """
        print("Elegir Nivel de operacion\n")
        while True:
            input_complejo =  self.elegir_nivel_operacion()
            
            if input_complejo == '1':
                self.elegir_operacion_basica()
            elif input_complejo == '2':
                self.elegir_operacion_avanzada()
            elif input_complejo == '3':
                self.entrada_operacion_fasores()
            else:
               print('Elegir el Nivel de operacion correcta\n')
                
            
            
    def main(self):
        self.input_usuario()
 
    def entrada_operacion_fasores(self):
        """Se realizan las operaciones de fasores """
        if not self.ingresar_fasores():
            self.aplicar_operacion_fasores(self.fasor1,self.fasor2,self.tipo_funcion1,self.tipo_funcion1)
    
    def validar_tipo_funcion(self,input_tipo_funcion):
        """se verifica si es funcion seno o coseno"""
        if input_tipo_funcion == '1' or input_tipo_funcion == '2':
            return True
        else:
            print('Ingresar el tipo de funcion correcto\n')
            return False
    
    def ingresar_fasores(self):
        """se ingresan los fasores"""
        print('\n\n')
        print('Ingresar 2 Fasores\nDebe respetar el formato adecuado, sinusoidales con frecuencias iguales\n')
        print('Para el formato Seno y conseno debe escribir: (a,b,c)\nDonde a(amplitud), b(frecuencia) y c(fase inicial) representa al fasor\n')
        
        formato = True
        while formato:
           
           input_tipo_funcion=input('Elegir el tipo de la primer funcion o escriba r para regresar a las operaciones\n1. Seno\n2. Coseno\n')
          
           if input_tipo_funcion == 'r':
               return True
               break
           
           if not self.validar_tipo_funcion(input_tipo_funcion):
               continue
                     
           input_fasor1 = input('Ingresar el primer Fasor o escriba r para regresar a las operaciones\n')
           
           if input_fasor1 == 'r':
               return True
               break
           
           formato_valido_f1 = True
           if input_fasor1[0] == '(':
              formato_valido_f1 = self.controlador.validar_entrada_fasor(input_fasor1)
           
           input_tipo_funcion2=input('Elegir el tipo de la segunda funcion o escriba r para regresar a las operaciones \n1. Seno\n2. Coseno\n')
           
           if input_tipo_funcion2 == 'r':
               return True
               break
           
           if not self.validar_tipo_funcion(input_tipo_funcion2):
               continue 
            
           input_fasor2 = input('Ingresar el segundo Fasor o escriba r para regresar a las operaciones\n')
           
           if input_fasor2 == 'r':
               return True
               break
           
           formato_valido_f2 = True
           if input_fasor2[0] == '(':
               formato_valido_f2 = self.controlador.validar_entrada_fasor(input_fasor2)          
           
           if not self.controlador.validar_igualdad_frecuencias(input_fasor1,input_fasor2):
              print('Las funciones no tiene la mismas frecuencias')
              continue
            
           if formato_valido_f1 == False and  formato_valido_f2 == False: # salida del usuario para regresar
              self.fasor1 = input_fasor1
              self.fasor2 = input_fasor2
              self.tipo_funcion1 = input_tipo_funcion
              self.tipo_funcion2 = input_tipo_funcion2
              return False
            
           print('Escriba nuevamente el formato correcto o presione la tecla  r para salir\n')
        
    def elegir_operacion_basica(self):
        """Elegir el tipo de operacion, suma, resta, multiplicacion"""
        
        while True:
            input_operacion = input('\nElegir operacion\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n')
            if input_operacion == '1':
                break
            elif input_operacion == '2':
                break
            elif input_operacion == '3':
                break
            elif input_operacion == '4':
                break
            print('Elegir la correcta operacion basica') 
            
        self.entrada_operacion_basica(input_operacion)
        #validar de elegir el correcto numero de operacion basico
       # return input_operacion
        
    def elegir_nivel_operacion(self):
        """Elegir nivel basico o avanzado"""
        input_nivel_operacion = input('1. Basico\n2. Avanzado\n3. Suma de fasores\n')
        #Validar el nivel de operacion exacto
        return input_nivel_operacion
    def ingresar_1_complejo(self,operacion):
        print('\n\n')
        print('Ingrese un numero complejo\nDebe respetar el formato adecuado, Binomica y Polar\n')
        print('Para el formato Binomica debe escribir: (a,b)\nDonde a(Real) y b(imaginaria) representa el numero complejo\n')
        print('Para el formato Polar debe escribir: [a,b]\nDonde a(modulo) y b(angulo) representan el numero complejo\n')
        #validar el complejo 2
        #Luego trasnformar segun el caso
        formato = True
        while formato:
           
           input_complejo1 = input('Ingrese el numero complejo  o escriba r para regresar a las operaciones\n')
           
           if input_complejo1 == 'r':
               return True
               break
               
           if input_complejo1[0] == '(':
              formato_valido_c1 = self.controlador.validar_entrada_bin(input_complejo1)
           else:
              formato_valido_c1 = self.controlador.validar_entrada_polar(input_complejo1)
           
           input_exonente = input('Ingrese el exponente o escriba r para regresar a las operaciones\n') 
           if input_exonente == 'r':
               return True
               break
           
           if not self.controlador.validar_numericos_enteros(input_exonente):
                  formato_valido_exp = False
           else:
               formato_valido_exp = True
           
           if formato_valido_c1 == False and formato_valido_exp == False: # salida del usuario para regresar
               self.formato_complejo1 = input_complejo1
               self.exponente = input_exonente
               return False
            
           print('Escriba nuevamente el formato del compejo correcto o exponente entero\nPresione la tecla  r para salir\n')
           
    def ingresar_2_complejos(self,operacion):
        print('\n\n')
        print('Ingresar 2 complejos\nDebe respetar el formato adecuado, Binomica y Polar\n')
        print('Para el formato Binomica debe escribir: (a,b)\nDonde a(Real) y b(imaginaria) representa el numero complejo\n')
        print('Para el formato Polar debe escribir: [a,b]\nDonde a(modulo) y b(angulo) representan el numero complejo\n')
        #validar el complejo 2
        #Luego trasnformar segun el caso
        formato = True
        while formato:
           
           input_complejo1 = input('Ingresar el primer complejo o escriba r para regresar a las operaciones\n ')
           
           if input_complejo1 == 'r':
               return True
               break
               
           if input_complejo1[0] == '(':
              formato_valido_c1 = self.controlador.validar_entrada_bin(input_complejo1)
           else:
              formato_valido_c1 = self.controlador.validar_entrada_polar(input_complejo1)
           
           input_complejo2 = input('Ingresar el segundo complejo o precione la tecla r para regresar a las operaciones\n')
           
           
           if input_complejo2 == 'r':
               return True
               break
           
           if input_complejo2[0] == '(':
               formato_valido_c2 = self.controlador.validar_entrada_bin(input_complejo2)
           else:
               formato_valido_c2 = self.controlador.validar_entrada_polar(input_complejo2)
               
           

           if formato_valido_c1 == False and  formato_valido_c2 == False: # salida del usuario para regresar
              self.formato_complejo1 = input_complejo1
              self.formato_complejo2 = input_complejo2
              return False
            
           print('Escriba nuevamente el formato correcto o presione la tecla  r para salir\n')
        
        
    def aplicar_operacion_basicas(self,operacion,complejo1,complejo2):
        """Se ejecutan las operaciones basicas """
        nuevo_complejo =  self.controlador.ejecutar_operacion_basica(operacion,complejo1,complejo2)
        print('\nResultado\n')
        nuevo_complejo.formaBinomica()
        nuevo_complejo.formaPolar()
        print('\n')
        
    def aplicar_operacion_fasores(self,fasor1,fasor2,input_tipo_funcion1,input_tipo_funcion2):
        """se ejecutan la suma de fasores"""
        fasor1 = self.controlador.convertir_fasor(fasor1,input_tipo_funcion1)
        fasor2 = self.controlador.convertir_fasor(fasor2,input_tipo_funcion2)
        nuevo_fasor1 =  self.controlador.ejecutar_operacion_fasores(fasor1,fasor2)
        print('\nResultado\n')
        print( f"({nuevo_fasor1.amplitud } , { nuevo_fasor1.frecuencia } , { nuevo_fasor1.anguloInicial} )",'(Amplitud,frecuencia,angulo) --> Forma Coseno' )
        nuevo_fasor1.pasarASeno() # pasamos a seno el angulo inicial y luego imprimimos el nuevo formato
        print( f"( {nuevo_fasor1.amplitud }, { nuevo_fasor1.frecuencia } , { nuevo_fasor1.anguloInicial} )",'(Amplitud,frecuencia,angulo) --> Forma seno\n' )
        print('\n')
    def aplicar_operacion_avanzadas(self,operacion,complejo1,exponente):
        """Se ejecutan las operaciones avanzadas """
        exponente_int = int(exponente)
        nuevo_complejo =  self.controlador.ejecutar_operacion_avanzada(operacion,complejo1,exponente_int)
        raices = 0
        print('\nResultados\n')
        if operacion == '1':# si es potencia
                nuevo_complejo.formaBinomica()
                nuevo_complejo.formaPolar()
                print('\n')
        elif operacion == '2': # si es Raiz
            for complejo in nuevo_complejo:
                print('Raiz:',raices) 
                complejo.formaBinomica()
                complejo.formaPolar()
                print('\n')
                raices = raices + 1
        elif operacion == '3':# si es raices primitivas
             for complejo in nuevo_complejo:
                 print('Raiz:',raices)
                 complejo.formaBinomica()
                 complejo.formaPolar()
                 print('\n')
                 raices = raices + 1
        print('\n')
       
             

