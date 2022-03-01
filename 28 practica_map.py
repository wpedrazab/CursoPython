#como usar la funci[on MAP
# esta funcion permite aplicar una funcion a los elementos de una lista ]
class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Pedro", "Presidente", 8500),
Empleado("Juan", "Director", 7500),
Empleado("Luis", "Gerente", 5500),
Empleado("Carlos", "Asistente", 2500),
Empleado("Ana", "Secretaria", 2000)
]

def calculo_comision(empleado):
	if(empleado.salario<=3000):
		empleado.salario= empleado.salario * 1.03
	return empleado

listaEmpleadosComision=map(calculo_comision,listaEmpleados)
for empleado in listaEmpleadosComision:
	print(empleado)