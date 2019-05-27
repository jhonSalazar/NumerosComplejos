import math 
from paquetes.fasor import Fasor
from paquetes.operaciones import Operaciones
# Prueba de script, resultado de fasor
         
fasor1= Fasor(7,5,math.pi/3)
fasor2= Fasor(5,5,3*math.pi/2)
fasorResultado = Operaciones.sumarfasores(fasor1,fasor2)
print ("SUMA DE FASORES : Amplitud, frecuencia, angulo inicial" )
print("Amplitud: ",fasorResultado.amplitud,"Frecuencia: ", fasorResultado.frecuencia,"Angulo en Radianes",fasorResultado.anguloInicial)