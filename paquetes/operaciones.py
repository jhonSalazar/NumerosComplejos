import math
from paquetes.complejo import Complejo

class Operaciones:

    @classmethod
    def suma( cls, complejo1, complejo2 ):
        real = complejo1.real + complejo2.real
        imginaria = complejo1.img + complejo2.img
        return Complejo( real, imginaria )

    @classmethod
    def resta( cls, complejo1, complejo2 ):
        real = complejo1.real - complejo2.real
        imginaria = complejo1.img - complejo2.img
        return Complejo( real, imginaria )

    @classmethod
    def multiplicacion( cls, complejo1, complejo2 ):
        modulo = complejo1.modulo() * complejo2.modulo()
        argumento = complejo1.argumento() + complejo2.argumento()
        return Complejo.CrearFormaPolar( modulo,argumento )

    @classmethod
    def division( cls, complejo1, complejo2 ):
        modulo = complejo1.modulo() / complejo2.modulo()
        argumento = complejo1.argumento() - complejo2.argumento()
        return Complejo.CrearFormaPolar( modulo, argumento )

    @classmethod
    def potencia( cls, complejo, exponente ):
        modulo = complejo.modulo() ** exponente
        argumento = complejo.argumento() * exponente
        return Complejo.CrearFormaPolar( modulo, argumento )

    @classmethod
    def raices( cls, complejo, exponente ):
        modulo = complejo.modulo() ** ( 1 / exponente )
        argumento = complejo.argumento() / exponente
        complejos = []
        for i in range( exponente ):
            complejos.append( Complejo.CrearFormaPolar( modulo, argumento + math.pi * 2 / exponente * i ) )
        return complejos
