for letra in "Python":
	if letra=="h":
		continue #ignora el resto del bucle y va al inicio

	print("viendo la letra: " + str(letra))

# otro ejemplo
nombre="Pildoras Informáticas"

contador = 0

for i in nombre:
	if i==" ":
		continue
	contador+=1 #equivalente contador = contador + 1

print("Cantidad de caracteres: " + str(contador))

# Otro ejemplo
email=input("Cual es tu correo: ")

for i in email:
	
	if i=="@":
		
		arroba=True
		break;

else: # se ejecuta cuando halla terminado todas las vueltas del bucle
	
	arroba=False

print(arroba)

