# el modulo doctest sirve para probar las funciones desde el area de
# comentarios de la funcion, se pueden hacer varias pruebas si desea
def areaTriangulo(base,altura):
	"""
	Calcula el area de un triangulo

	>>> areaTriangulo(3,6)
	'El area es de: 9.0'

	>>> areaTriangulo(2,4)
	'El area es de: 4.0'

	"""
	return ('El area es de: ' + str(base*altura/2))


"""
Este programa devuelve esto, si la prueba falla, si no falla, no devuelve nada
**********************************************************************
File "D:\Cursos\Python\31 practica_doctest.py", line 5, in __main__.areaTriangulo
Failed example:
    areaTriangulo(3,6)
Expected:
    8.0
Got:
    9.0
**********************************************************************
"""

# otro ejemplo de pruebas en los comentarios

def compruebaMail(mailUsuario):
	"""
	Funcion que valida un correo

	>>> compruebaMail('wp@gmail.com')
	True

	>>> compruebaMail('wpgmail.com')
	False

	>>> compruebaMail('@gmail.com')
	False

	"""
	arroba=mailUsuario.count('@')

	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

# otro ejemplo colocando instrucciones anidadas en la prueba en comentarios
import math
def raizCuadrada(listaNumeros):
	"""
	Funcion que calcula la raiz cuadrada de una lista de numeros
	Para anidar expresiones en la prueba se usa ...
	Si esperamos que devuelva un error se coloca como el ejemplo de abajo
	Solo el encabezado y pie del error

	>>> lista=[]
	>>> for i in [4, 9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista=[]
	>>> for i in [4, -9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
    Traceback (most recent call last):
		...
    ValueError: math domain error

	"""
	return [math.sqrt(n) for n in listaNumeros]

import doctest
doctest.testmod()



