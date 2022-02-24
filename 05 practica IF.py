print("Programa de evaluación")

print("ingrese la nota: ")
nota_alumno=input()

def evaluacion(nota):
	if nota<=5:
		valoracion="insuficiente"
	elif nota<=7:
		valoracion="suficiente"
	elif nota<=9:
		valoracion="Aprobado"
	return valoracion

print(evaluacion(int(nota_alumno)))
