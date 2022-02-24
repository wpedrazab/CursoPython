from io import open #metodo para abrir un archivo externo txt por ejemplo

# leer este enlace para mas info: https://docs.python.org/3/library/io.html

# para escribir:
# archivo_texto=open("archivo.txt","w")
# frase="Buen dia \nPara estudiar Python"
# archivo_texto.write(frase)
# archivo_texto.close()

# para leer:
# archivo_texto=open("archivo.txt","r")
# texto=archivo_texto.read()
# archivo_texto.close()
# print(texto)

# para leer el archivo almacenando las lineas en una lista
# archivo_texto=open("archivo.txt","r")
# lineas_texto=archivo_texto.readlines()
# archivo_texto.close()
# print(lineas_texto[1]) #se muestra la linea que indique el indice

# Para agregar data
# archivo_texto=open("archivo.txt","a")
# archivo_texto.write("\notro dia mas")
# archivo_texto.close()

# para leer y ubicarse en diferentes partes dle archivo:
#archivo_texto=open("archivo.txt","r")
#archivo_texto.seek(11) para ubicarse en el caracter 11
#print(archivo_texto.read(11)) tambien para ubicarse en el caracter 11
#archivo_texto.seek(len(archivo_texto.read())/2) para ubicarse en la mitad del archivo
#archivo_texto.seek(len(archivo_texto.readline()))
#print(archivo_texto.read())

#Para abrir en modo lectura y escritura a la vez
archivo_texto=open("archivo.txt","r+") #para lectura y escritura r+
#archivo_texto.write("Comienzo del texto")
#print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines()
lista_texto[1]=" Esta linea ha sido incluida \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto) #esto sobre escribe la linea 1
archivo_texto.close()



