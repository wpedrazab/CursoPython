for i in ["primavera", "verano", "otoño", "Invierno"]:
	print("hola", end=" ")
	print("Hola " + str(i))


email=False
miEmail=input("Tu correo es: ")

for i in miEmail:
	if(i=="@"):
		email=True

if email: # se puede omitir esto "==True":
	print("Email correcto")
else:
	print("Email incorrecto")

for i in range(5):
	print("Hola" + str(i))
