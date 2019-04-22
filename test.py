import unittest 
from  paquetes import complejo

class Test(unittest.TestCase):
    """test unitario para numero compplejo."""
    def test_numero_complejo_modulo(self):
        """test unitario para moddulo numero compplejo."""
        numeroComplejo=complejo.Complejo(1,2)
        self.assertEqual(2.24,round(numeroComplejo.modulo(),2))

    def test_numero_complejo_argumento(self):
        """test unitario para argumento numero compplejo."""
        numeroComplejo=complejo.Complejo(1,2)
        self.assertEqual(1.107,round(numeroComplejo.argumento(),3))

    def test_numero_complejo_polar(self):
        """test unitario para pasar de Binomica a Polar."""
        numeroComplejo = complejo.Complejo.CrearFormaBinomica(1,2)
        print("Forma Polar: ",end="")
        print(numeroComplejo.formaPolar())

    def test_numero_complejo_binomica(self):
        """test unitario para pasar de Polar a Binomica."""
        numeroComplejo=complejo.Complejo.CrearFormaPolar(2.23606797749979,1.1071487177940904)
        print("Forma binomica: ",end="")
        print(numeroComplejo.formaBinomica())
       
       
if __name__ == "__main__":
    unittest.main()