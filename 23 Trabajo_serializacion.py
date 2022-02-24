import pickle # esta es la libreria que tiene los metodos necesarios

# Pasos para crearlo
# lista_nombres=["Pedro", "Ana", "Maria", "Luis"]

# fichero_binario=open("lista_nombres","wb") # abre en forma de escritura binaria

# #lista_nombres va a ser el nombre del archivo en windows
# #fichero_binario es el archivo que creamos con la lista
# pickle.dump(lista_nombres, fichero_binario)

# fichero_binario.close()

# del (fichero_binario) #para borrar el archivo que se creo

#Pasos para leerlo
fichero=open("lista_nombres", "rb") # abre en modo lectura binaria
lista=pickle.load(fichero)
print(lista)
