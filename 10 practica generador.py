def generapares(limite):
	num=1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num+=1
	return miLista

print(generapares(10))

# lo mismo pero usando un generador

def generapares2(limite):
	num=1
	# miLista=[] no hace falta el contenedor

	while num<limite:
		# miLista.append(num*2)

		yield num*2
		num+=1

devuelvepares2=generapares2(10)

print(next(devuelvepares2))

print("aqui podria ir mas código")

print(next(devuelvepares2))

print("aqui podria ir mas código")
