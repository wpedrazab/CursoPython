import pickle

class Vehiculo():
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
		print("Marca: ", self.marca, "\nModelo: ", self.modelo,	
		"\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, 
		"\nFrenando: ", self.frena) #\n salta una linea

# Proceso para crear el archivo
# creamos una lista
coche1=Vehiculo("Ford", "Explorer")
coche2=Vehiculo("Fiat", "Siena")
coche3=Vehiculo("Ford", "malibu")
coches=[coche1, coche2, coche3]
#creamos el archivo serializado
fichero=open("loscoches", "wb") # write binario
pickle.dump(coches, fichero) #la lista coches va al archivo loscoches
fichero.close()
del (fichero)

# Abrimos el archivo y lo llevamos a una variable tipo coleccion
ficheroApertura=open("loscoches", "rb")
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
	print(c.estado())
