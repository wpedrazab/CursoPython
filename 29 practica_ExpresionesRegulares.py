import re

cadena="Vamos a aprender en Python expresiones regulares. Python es un lenguaje sencillo"

#print(re.search("aprender", cadena))

#esto devuelve un objeto re
#<re.Match object; span=(8, 16), match='aprender'>

# otro uso
textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None:
	print("Lo encontre")
else:
	print("No lo encontre")

#otro uso
textoEncontrado=re.search(textoBuscar, cadena)

# print(textoEncontrado.start())
# print(textoEncontrado.end())
# print(textoEncontrado.span())

textoBuscar2="Python"
#print(len(re.findall(textoBuscar2, cadena))) #busca todas las coincidencias

#otro uso (anclas)

lista_nombres=['Ana Gomez', 'Maria Martin', 'Sandra Lopez', 
'Santiago Martin', 'niños', 'niñas', 
'MA1','MA2','MA3','MA4','MA5','BA1','BA2','VA1','MAA','MAB','MAC' ]
for elemento in lista_nombres:

	# if re.findall('^Sandra', elemento): # ^ ese metacaracter indica que debe buscar al inicio
	# 	print(elemento)

	# if re.findall('Martin$', elemento): # $ ese metacaracter indica que debe buscar al final
	# 	print(elemento)

	# if re.findall('[gz]', elemento): # [] se usan para buscar x caracteres en la lista
	# 	print(elemento)

	if re.findall('niñ[oa]s', elemento): # [] buscar x caracteres en la lista
		print(elemento)

	# if re.findall('^[M-S]', elemento): # ^[M-S] buscar los que comiencen con letras mayusculas entre M y S
	# 	print(elemento)

	# if re.findall('MA[1-3]', elemento): # ^busca los que comiencen con MA y continuen con numeros del 1 al 3
	# 	print(elemento)

	# if re.findall('MA[^1-3]', elemento): # ^busca los que comiencen con MA y NO continuen con numeros del 1 al 3
	# 	print(elemento)

	# if re.findall('MA[1-3A-B]', elemento): # ^busca los que comiencen con MA y continuen con numeros del 1 al 3
	# 	print(elemento)

#ejemplos con match, esta siempre busca al principio
cadena1="Sandra Lopez"
cadena2="500 Sandra Lopez"

# if re.match("sandra", cadena1, re.IGNORECASE):
# 	print("Lo encontre")

# if re.match("...dra", cadena1): #valida que luego de 3 caracteres tenga dra en el contenido
# 	print("Lo encontre")

# if re.match("\d", cadena2): #valida si comienza con un numero
# 	print("Lo encontre")

#ejemplos con search, esta busca en toda la cadena de texto

codigo1="kh8hh8h871lkj8"
codigo2="oiuoijoui1iu3ikk3o32"

if re.search("71", codigo2): #valida que luego de 3 caracteres tenga dra en el contenido
	print("Lo encontre")