class Coche():

	def __init__(self): #condtructor de la clase
		self.__largoChasis=250 #los guiones bajos encapsulan las variables para que no se pueden modificar desde fuera de la clase
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enMarcha=False

	def arrancar(self, arrancamos):
		self.__enMarcha=arrancamos
		if(self.__enMarcha):
			chequeo=self.__chequeoInterno()

		if(self.__enMarcha and chequeo):
			return "Esta en marcha"
		elif(self.__enMarcha and chequeo==False):
			return "Algo esta mal, no podemos arrancar"
		else:
			return "Esta detenido"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas, un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

	def __chequeoInterno(self): #los guiones encapsulan el metodo
		print("realizando chequeo")
		self.gasolina="Ok"
		self.aceite="Ok"
		self.puertas="Cerradas"

		if(self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
			return True
		else:
			return False

miCoche=Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print()
print("Segundo objeto:")

miCoche2=Coche()
print(miCoche.arrancar(False))
# miCoche2.__ruedas=2 ejemplo de que no podemos acceder a variables encapsuladas
miCoche2.estado()
