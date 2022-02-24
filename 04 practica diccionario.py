midiccionario={"Alemania":"Berlín","Francia":"París","Colombia":"Bogotá","Venezuela":"Caracas"}
print(midiccionario["Francia"])

midiccionario["Italia"]="Lisboa" #agregar
print(midiccionario)

midiccionario["Italia"]="Roma" #Modificar

print(midiccionario)

del midiccionario["Alemania"] #eliminar

print(midiccionario)

midiccionario2={"Alemania":"Berlin", 23:"Jordan", 3:"Mosqueteros"}
print(midiccionario2)

mitupla=["Perú", "Ecuador", "Brasil"]

midiccionario3={mitupla[0]:"Lima", mitupla[1]:"Quito", mitupla[2]:"Rio"}

print(midiccionario3)

#Un diccionario dentro de otro

midiccionario4={23:"Jordan", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(len(midiccionario4)) #largo
print(midiccionario4.keys()) #claves
print(midiccionario4.values()) #valores
