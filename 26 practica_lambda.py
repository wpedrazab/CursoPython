#como usar las funciones Lambda

#esto seria la forma tradicional
def area(base, altura):
	return(base*altura)/2

print(area(2,4))
print(area(6,8))

#usando Lambda
area=lambda base, altura:(base*altura)/2

print(area(3,5))
print(area(7,9))

# otro ejemplo
cubo=lambda numero:pow(numero,3) #pow para elevar a cualquier potencia, podria ser tambien numero**3

print(cubo(5))

#otro ejemplo
comisionalta=lambda comision:"$ ¡{}!".format(comision)

print(comisionalta(1 4575))