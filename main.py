import math 
from paquetes.fasor import Fasor
from paquetes.operaciones import Operaciones
from ui.consola import Consola
from controladores.controlador import Controlador
# Prueba de script, resultado de fasor
         
if __name__ == "__main__":
    consola = Consola(Controlador())
    consola.main()