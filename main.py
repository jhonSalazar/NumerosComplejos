import cmath 
import math
from paquetes import complejo
from paquetes import operaciones

# Prueba de script, inicializando un numero complejo
x = 5
y = 3

z = complex(x,y); # creamos un numero complejo

print("Numero compleo: ",z)
print ("Parte Real:",end="") 
print (z.real) 

print ("Parte imaginaria:",end="") 
print (z.imag)

c1 = complejo.Complejo(1, 2)
c2 = complejo.Complejo(2, -1)

print(operaciones.Operaciones.suma(c1, c2).formaBinomica())
print(operaciones.Operaciones.resta(c1, c2).formaBinomica())
print(operaciones.Operaciones.resta(c1, c2).formaBinomica())
print(operaciones.Operaciones.multiplicacion(c1, c2).formaBinomica())
print(operaciones.Operaciones.division(c1, c2).formaBinomica())
