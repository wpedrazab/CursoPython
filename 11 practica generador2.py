def devuelveCiudades(*ciudades): # el * indica que va a recibir un numero indeterminado de elementos y que los va a recibir en forma de tupla
		for elemento in ciudades:
			# for subElemento in elemento:
				yield from elemento # el from elimina el uso del for anterior

ciudadesDevueltas=devuelveCiudades("Bogotá", "Caracas", "Rio", "Quito")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

