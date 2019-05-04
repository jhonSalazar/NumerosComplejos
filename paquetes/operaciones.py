import math
from paquetes import complejo

class Operaciones:

    @classmethod
    def suma(cls, complejo1, complejo2):
        real = complejo1.real + complejo2.real
        imginaria = complejo1.img + complejo2.img
        return complejo.Complejo(real,imginaria)

    @classmethod
    def resta(cls, complejo1, complejo2):
        real = complejo1.real - complejo2.real
        imginaria = complejo1.img - complejo2.img
        return complejo.Complejo(real, imginaria)

    @classmethod
    def multiplicacion(cls, complejo1, complejo2):
        modulo = complejo1.modulo() * complejo2.modulo()
        argumento = complejo1.argumento() + complejo2.argumento()
        return complejo.Complejo.CrearFormaPolar(modulo,argumento)

    @classmethod
    def division(cls, complejo1, complejo2):
        modulo = complejo1.modulo() / complejo2.modulo()
        argumento = complejo1.argumento() - complejo2.argumento()
        return complejo.Complejo.CrearFormaPolar(modulo, argumento)


