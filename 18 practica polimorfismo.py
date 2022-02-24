class Coche():
	def desplazamiento(self):
		print("con 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("con 2 ruedas")

class Camion():
	def desplazamiento(self):
		print("con 6 ruedas")

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)