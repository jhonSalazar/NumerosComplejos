import math
import cmath 

class Complejo( object ):
	""" Clase para representar numero complejo """

	def __init__ ( self, real = 0, img = 0 ):
		""" Constructor con componentes bonimicas """
		self.real = real
		self.img  = img

	@classmethod
	def CrearFormaBinomica( cls, real = 0, img = 0 ):
		""" Factory para crear de forma binomica """
		return cls( float( real ), float( img ) )

	@classmethod
	def CrearFormaPolar( cls, modulo = 0, argumento = 0 ):
		""" Factory para crear de forma polar """
		argumento = cls.AjustarAPrimerGiro( argumento )
		return cls( modulo * round( math.cos( argumento ), 5 ), modulo * round( math.sin( argumento ), 5 ) )

	@staticmethod
	def AjustarAPrimerGiro( argumento ):
		""" Retorna argumento en primer giro positivo ( entre 0 y 2 pi ) """
		return argumento % ( 2 * math.pi )

	def modulo( self ):
		""" Retorna modulo del numero complejo """
		return math.sqrt( self.real ** 2 + self.img ** 2)

	def argumento( self ):
		""" Retorna argumento del numero complejo en el primer giro positivo """
		return Complejo.AjustarAPrimerGiro( math.atan2( self.img, self.real ) )

	def formaBinomica( self ):
		""" Imprime por pantalla representacion del complejo en forma binomica """
		#return cmath.rect(self.modulo(),self.argumento())
		print( f"( { self.real }, { self.img } )" )

	def formaPolar( self ):
		""" Imprime por pantalla representacion del complejo en forma polar """
		#return cmath.polar(complex(self.real,self.img))
		argu = self.AjustarAPrimerGiro( self.argumento() )
		print( f"[ { self.modulo() }, { argu } ]" )
        
