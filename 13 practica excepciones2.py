def divide():

	try:
		op1=(float(input("Primer número: ")))
		op2=(float(input("Segundo número: ")))
		print("La división es: " + str(op1/op2))

	except ValueError:
		print("Valor erróneo")

	except ZeroDivisionError:
		print("No se puede dividir entre cero")

	finally:
		print("Calculo finalizado")

divide()