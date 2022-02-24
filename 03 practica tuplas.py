mitupla=("Juan",15,1,2022)
print(mitupla[1])
print(mitupla)
milista=list(mitupla)
print(milista)
mitupla2=tuple(milista)
print(mitupla2)

print("Juan" in mitupla)

print(mitupla.count(15)) #contar las veces que aparece un elemento
print(len(mitupla)) #cuantos elementos tiene

nombre, dia, mes, agno=mitupla #desempaquetado de tuplas

print(nombre)
print(dia)
print(mes)
print(agno)

print(mitupla.index(15)) #buscar elementos
