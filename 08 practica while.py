import math #para importar una clase
# i=1

# while i<=5:
# 	print("Ejecución: " + str(i))
# 	i=i+1

# print("Termino")

# edad=int(input("cual es tu edad: "))

# while edad<1 or edad>90:
# 	print("Errada")
# 	edad=int(input("cual es tu edad: "))


# print("Tu edad es: "+str(edad))



print("Calculo de raiz cuadrada")
numero=int(input("numero: "))

intentos = 0
while numero<0:
	print("No se puede hallar la raiz de negativos")

	if intentos==2:
		print("demasiados intetos")
		break;
	numero=int(input("numero: "))

	if numero<0:
		intentos = intentos +1

if intentos<2:
	solucion=math.sqrt(numero)
	print("raiz cuadrada de " + str(numero) + " es: " + str(solucion))


