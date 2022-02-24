class Vehiculos(object):
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo,	"\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena) #\n salta una linea

class Camioneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La camioneta va cargada"
		else:
			return "La camioneta vno esta cargada"

class Moto(Vehiculos): #asi Moto hereda de Vehiculos
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo,	"\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito) #\n salta una linea

class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		#Para que tambien tome el constructor de Vehiculo
		super().__init__(marca, modelo)
		self.autonomia=100
	def cargarEnergia(self):
		self.cargado=True

miMoto=Moto("Honda", "CBR") #le debemos pasar los parametros que heredo de Vehiculos
miMoto.caballito()
miMoto.estado()

miCamioneta=Camioneta("Ford", "Pickup")
miCamioneta.arrancar()
miCamioneta.carga(True)
miCamioneta.estado()
print(miCamioneta.carga(True))

class BicicletaElectrica(VElectricos,Vehiculos): 
#esta clase hereda de dos clases, pero el constructor que hereda es de la primera clase que se mencione
	pass

miBici=BicicletaElectrica("Merida", "CRV1500") #al instanciar la clase, no se le puede pasar modelo y marca porque daria error
