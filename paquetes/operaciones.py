import math
from paquetes.complejo import Complejo
from paquetes.fasor import Fasor
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

    @classmethod
    def raicesPrimitivas( cls, complejo, exponente ):
        todasLasRaices = cls.raices( complejo, exponente )
        indicesDePrimtivas = filter( 
            lambda i: cls._maximoComunDivisor( i, exponente ) == 1,
            range( exponente ))
        raicesFiltradas = map( lambda i: todasLasRaices[ i ], indicesDePrimtivas )
        return list( raicesFiltradas )

    @classmethod
    def _maximoComunDivisor( cls, k, n ):
        a = max( k, n )
        b = min( k, n )
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    
    @classmethod
    def sumarfasores(cls,fasor,otroFasor):
        # se deberia validar desde esta parte que ambos tengan la misma frecuencia, pero esa validacion
        #lo hacemos desde la interfaz
        numeroComplejo =  Complejo.CrearFormaBinomica(fasor.crearParteReal(),fasor.crearParteImaginaria())
        numeroComplejo2 = Complejo.CrearFormaBinomica(otroFasor.crearParteReal(),otroFasor.crearParteImaginaria())
        sumaBinomica= cls.suma(numeroComplejo,numeroComplejo2)
        nuevoFasor = Fasor(sumaBinomica.modulo(),fasor.frecuencia,sumaBinomica.argumento())
        return nuevoFasor


    
