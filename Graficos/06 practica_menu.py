from tkinter import *
from tkinter import messagebox #para usar las ventanas emergentes

raiz=Tk()

def infoAdicional():
	messagebox.showinfo("Titulo de la ventana", "Procesador de texto 2022")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto con licencia gratuita")

def salirApp():
	#puede ser askokcancel pero devuelve True o False
	valor=messagebox.askquestion("Salir", "Desea salir?") #devuelve yes o no
	if valor=="yes":
		raiz.destroy()

def cerrarDoc():
	valor=messagebox.askretrycancel("Reintentar", "No es posible") #devuelve True False
	if valor=="yes":
		raiz.destroy()

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0) #teareoff elimina la barra por defecto de los submenu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Open")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDoc)
archivoMenu.add_command(label="Salir", command=salirApp)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")

archivoTools=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Tipo Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="A cerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoTools)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

raiz.mainloop()