#como usar la funci[on filter
# esta es mas usada para filtrar objetos
def numero_par(num):
	if num % 2==0:
		return True

numeros=[17,24,7,39,8,51,92]
#filter devuelve un objeto, por eso usamos list, para que devuelva en formato de lista
print(list(filter(numero_par, numeros))) 

#si usamos lambda
numeros=[25,18,45,72,28]
print(list(filter(lambda numero_par: numero_par%2==0, numeros))) 


class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan", "Director", 75000),
Empleado("Pedro", "Presidente", 85000),
Empleado("Luis", "Gerente", 55000),
Empleado("Carlos", "Asistente", 25000),
Empleado("Ana", "Secretaria", 20000)
]

#funcion filter con lambda
salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:
	print(empleado_salario)