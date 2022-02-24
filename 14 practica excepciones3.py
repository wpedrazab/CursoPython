import math

def evaluaEdad(edad):
	if edad<0:
		# se debe indicar el tipo de excepción que queremos que se maneje
		# podemos usar una u otra, al final lo que va a enviar es el error
		raise TypeError("No se permiten edades negativas")
	elif edad<20:
		return "Eres joven"
	elif edad<40:
		return "Eres muy joven"
	elif edad<60:
		return "Eres mayor"
	elif edad<100:
		return "Cuidate..."

print(evaluaEdad(15)) #con valores negativos es que se forza el error

#las lineas posteriores no se ejecutan porque no estamos manejando un Try except
#Podemos crear una clase para el manejo de mis propias excepciones Class MiManejoErrores()

# otro ejemplo

def calculaRaiz(num1):
	if num1<0:
		raise ValueError("Numero negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:
	print(calculaRaiz(op1))

except ValueError as MiError:
	print(MiError)

print("Terminamos")
