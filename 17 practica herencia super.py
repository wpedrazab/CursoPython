class Persona():
	def __init__(self, nombre, edad, direccion):
		self.nombre = nombre
		self.edad = edad
		self.direccion = direccion

	def descripcion(self):
		print("Nombre: ", self.nombre, " Edad: ", self.edad, " Direccion: ", self.direccion)

class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, direccion_empleado):
		# esta instruccion Super, llama al init de la clase padre (Persona)
		# para que la clase Empleado tambien tenga esos atributos
		super().__init__(nombre_empleado, edad_empleado, direccion_empleado)
		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		#aqui aplica igual para otro metodo ademas del init
		super().descripcion()
		print("Salario: ", self.salario, " Antiguedad: ", self.antiguedad)

William=Empleado(1500, 15, "William", 53, "Venezuela")
William.descripcion()

print("Es Empleado: ", isinstance(William, Empleado))
print("Es Persona: ", isinstance(William, Persona))
