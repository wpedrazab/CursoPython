#Las funciones decoradoras reciben una funcion y retornan una funcion]
#se usan para agregar una misma funcionalidad a otras funciones
#por ejemplo para conectarse a una BD antes de y cerrar la BD luego de

def decoradora(parametro):
	"""Esta funcion es la decoradora, la triple comilla abre y cierra los comentarios
	*args dice que esta funcion puede recibir un numero indeterminado de parametros
	**kwargs le dice que tambien puede recibir parametros tipo clave valor"""
	def funcion_interior(*args, **kwargs): 
		print("Vamos a realizar un calculo: ")
		parametro(*args, **kwargs) #ejecuta la funcion que vino por parametro
	return funcion_interior

@decoradora #se coloca este comando antes de la declaracion para que use el decorado
def suma(num1, num2, num3):
	print(num1+num2+num3)

@decoradora
def resta(num1, num2):
	print(num1-num2)

@decoradora
def potencia(base, exponente):
	print(pow(base, exponente))

# esta instruccion imprime la documentacion de la funcion
#print(decoradora.__doc__)
help(decoradora) # igual muestra la documentacion
# si la funcion esta dentro de una clase debemos mencionarla
# igual aplica para los modulos:
# help(nombreclase.decoradora)

suma(35,20,5)
resta(35,20)
# aqui se pasan parametros tipo clave valor
potencia(base=5,exponente=3)

