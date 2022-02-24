milista=["Maria", 1, True, "Antonio"]

print(milista[:])
print(milista[2]) #los indices comienzan en cero 0
print(milista[-3])
print(milista[1:2]) #desde el 1 y excluyendo desde el indice 2

milista.append("Sandra") #agrega un valor al final
milista.insert(2,"José") #agrega un valor en una posición definida

print(milista[:])

milista.extend(["Ana", "Luis"])

print(milista[:])
print(milista.index("Antonio"))

print("Luis" in milista)

milista.remove("Ana") #elimina un elemento
print(milista[:])
milista.pop() #elimina el último de la lista
print(milista[:])

milista2=["Carlos", "Teresa"]
milista2=milista2*3

milista3=milista+milista2

print(milista3)
