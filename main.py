import cmath 
import math
from paquetes import complejo
from paquetes import operaciones

# Prueba de script, inicializando un numero complejo
x = 2
y = 0

z = complex(x,y); # creamos un numero complejo



print("Numero compleo: ",z)
print ("Parte Real:",end="") 
print (z.real) 

print ("Parte imaginaria:",end="") 
print (z.imag)

    def test_numero_complejo_polar(self):
        """test unitario para pasar de Binomica a Polar."""
        numeroComplejo = complejo.Complejo.CrearFormaBinomica(0,-2)
        print("Forma Polar: ",end="")
        print(numeroComplejo.formaPolar())
        

c1 = complejo.Complejo(4,3)
c2 = complejo.Complejo(3,4)

print ("Suma:",end="") 
print(operaciones.Operaciones.suma(c1, c2).formaBinomica())
print ("Resta:",end="") 
print(operaciones.Operaciones.resta(c1, c2).formaBinomica())
print ("Producto:",end="") 
print(operaciones.Operaciones.multiplicacion(c1, c2).formaBinomica())
print ("Cociente:",end="") 
print(operaciones.Operaciones.division(c1,c2).formaBinomica())
