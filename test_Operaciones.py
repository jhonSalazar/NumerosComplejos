import unittest 
from  paquetes import complejo
from  paquetes import operaciones

class Test(unittest.TestCase):
    """test unitario para numero complejo."""
    def test_numero_complejo_operacionesBinomica(self):
        """test Operaciones de 2 Nros. Complejos (Forma Binómica)"""
        complejo1=complejo.Complejo(0,2)
        complejo2=complejo.Complejo(1.4142136,-1.4142136)
        sumaBinomica=operaciones.Operaciones.suma(complejo1,complejo2)
        restaBinomica=operaciones.Operaciones.resta(complejo1,complejo2)
        productoBinomica=operaciones.Operaciones.multiplicacion(complejo1,complejo2)
        cocienteBinomica=operaciones.Operaciones.division(complejo1,complejo2)
        self.assertEqual(0.5858,round(sumaBinomica.img,4))
        self.assertEqual(-1.4142,round(restaBinomica.real,4))
        self.assertEqual(4.0000,round(productoBinomica.modulo(),4))
        self.assertEqual(2.3562,round(cocienteBinomica.argumento(),4))
        print (" ")
        print (" --  T E S T - #1 --")
        print (" -- Resultado de Operaciones con 2 Nros. Complejos -- E N  B I N Ó M I C A --")
        print (" --- S U M A  --  R E S T A  --  P R O D U C T O  --  C O C I E N T E  ---")
        print (" ")
        print ("C O M P L E J O S   I N G R E S A D O S ")
        print (" ")
        print ("N° Complejo 1 - FORMA BINOMICA :",end="")
        print(complejo1.formaBinomica())
        print ("N° Complejo 2 - FORMA BINOMICA :",end="")
        print(complejo2.formaBinomica())
        print ("N° Complejo 1 - FORMA POLAR :",end="")
        print(complejo1.formaPolar())
        print ("N° Complejo 2 - FORMA POLAR :",end="")
        print(complejo2.formaPolar())
        print (" ")
        print ("S U M A  --  B I N Ó M I C A :",end="")
        print(sumaBinomica.formaBinomica())
        print ("S U M A  --  P O L A R :",end="")
        print(sumaBinomica.formaPolar())
        print ("R E S T A  --  B I N Ó M I C A :",end="")
        print(restaBinomica.formaBinomica())
        print ("R E S T A  --  P O L A R :",end="")
        print(restaBinomica.formaPolar())
        print ("P R O D U C T O  --  B I N Ó M I C A :",end="")
        print(productoBinomica.formaBinomica())
        print ("P R O D U C T O  --  P O L A R :",end="")
        print(productoBinomica.formaPolar())
        print ("C O C I E N T E  --  B I N Ó M I C A :",end="")
        print(cocienteBinomica.formaBinomica())
        print ("C O C I E N T E  --  P O L A R :",end="")
        print(cocienteBinomica.formaPolar())

        
    def test_numero_complejo_operacionesPolar(self):
        """test Operaciones de 2 Nros. Complejos (Forma Polar)"""
        complejo1=complejo.Complejo.CrearFormaPolar(2,1.5707963279)
        complejo2=complejo.Complejo.CrearFormaPolar(2,5.4977871438)
        sumaPolar=operaciones.Operaciones.suma(complejo1,complejo2)
        restaPolar=operaciones.Operaciones.resta(complejo1,complejo2)
        productoPolar=operaciones.Operaciones.multiplicacion(complejo1,complejo2)
        cocientePolar=operaciones.Operaciones.division(complejo1,complejo2)
        self.assertEqual(0.5858,round(sumaPolar.img,4))
        self.assertEqual(-1.4142,round(restaPolar.real,4))
        self.assertEqual(4.0000,round(productoPolar.modulo(),4))
        self.assertEqual(2.3562,round(cocientePolar.argumento(),4))
        print (" ")
        print (" --  T E S T - #2 --")
        print (" -- Resultado de Operaciones con 2 Nros. Complejos -- E N    P O L A R  --")
        print (" --- S U M A  --  R E S T A  --  P R O D U C T O  --  C O C I E N T E  ---")
        print (" ")
        print ("C O M P L E J O S   I N G R E S A D O S ")
        print (" ")
        print ("N° Complejo 1 - FORMA BINOMICA :",end="")
        print(complejo1.formaBinomica())
        print ("N° Complejo 2 - FORMA BINOMICA :",end="")
        print(complejo2.formaBinomica())
        print ("N° Complejo 1 - FORMA POLAR :",end="")
        print(complejo1.formaPolar())
        print ("N° Complejo 2 - FORMA POLAR :",end="")
        print(complejo2.formaPolar())
        print (" ")
        print ("S U M A  --  B I N Ó M I C A :",end="")
        print(sumaPolar.formaBinomica())
        print ("S U M A  --  P O L A R :",end="")
        print(sumaPolar.formaPolar())
        print ("R E S T A  --  B I N Ó M I C A :",end="")
        print(restaPolar.formaBinomica())
        print ("R E S T A  --  P O L A R :",end="")
        print(restaPolar.formaPolar())
        print ("P R O D U C T O  --  B I N Ó M I C A :",end="")
        print(productoPolar.formaBinomica())
        print ("P R O D U C T O  --  P O L A R :",end="")
        print(productoPolar.formaPolar())
        print ("C O C I E N T E  --  B I N Ó M I C A :",end="")
        print(cocientePolar.formaBinomica())
        print ("C O C I E N T E  --  P O L A R :",end="")
        print(cocientePolar.formaPolar())

       
       
if __name__ == "__main__":
    unittest.main()
