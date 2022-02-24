for i in range(5,25,3): #desde, hasta, de cuanto en cuanto
	print(f"valor de la variable {i}") #la f une la variable con el texto


valido=False

email=input("cual es tu correo: ")

for i in range(len(email)):
	if email[i]=="@":
		valido = True

if valido:
	print("Correcto")
else:
	print(Incorrecto)