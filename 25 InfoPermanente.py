import pickle

# en este ejemplo vamos a crear archivos que queden de forma permanente
# nuestro disco para se consultados por otros programas

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se agrego a ", self.nombre)

	def __str__(self): #convierte en texto la informacion de un objeto
		#esto devuelve el contenido con un formato determinado
		return "{} {} {}".format(self.nombre, self.genero, self.edad)


#vamos a crear una lista para grabar y leer la data
class ListaPersonas:
	personas=[]
	def __init__(self):
		listaDePersonas=open("ficheroExterno", "ab+") # apertura binaria lee y escribe
		listaDePersonas.seek(0) #para ubicarnos el inicio del fichero

		# como la primera vez va a estar vacio va a dar error
		# por eso implementamos un manejo de errores
		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero esta vacio")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)	

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardaPersonasEnFicheroExterno()
	def mostrarPersonas(self):
		for p in self.personas:
			print(p)
	def guardaPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La infor del externo es ")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()

p=Persona("Luis", "M", 35)
miLista.agregarPersonas(p)
p=Persona("Ana", "F", 15)
miLista.agregarPersonas(p)
p=Persona("Pedro", "M", 28)
miLista.agregarPersonas(p)
miLista.mostrarInfoFicheroExterno()

# miLista.mostrarPersonas()



