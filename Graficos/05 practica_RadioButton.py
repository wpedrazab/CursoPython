from tkinter import *

raiz=Tk()
varOption=IntVar()
playa=IntVar()
montana=IntVar()
campo=IntVar()

def imprimir():
	if varOption.get() == 1:
		etiqueta.config(text="Escogiste Masculino")
	else:
		etiqueta.config(text="Escogiste Femenino")

Label(raiz,text="Genero").pack()

Radiobutton(raiz, text="Masculino", variable=varOption, value=1, command=imprimir).pack()
Radiobutton(raiz, text="Femenino", variable=varOption, value=2, command=imprimir).pack()

etiqueta=Label(raiz)
etiqueta.pack()

def opcionesVacaciones():
	opcionEscogida=""
	if(playa.get()==1):
		opcionEscogida+=" Playa"
	if(montana.get()==1):
		opcionEscogida+=" Montana"
	if(campo.get()==1):
		opcionEscogida+=" Campo"

	textoFinal.config(text=opcionEscogida)

frame=Frame(raiz, background="green") #para unir los check
frame.pack()

Label(frame,text="Que destinos te gustan?").pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesVacaciones).pack()
Checkbutton(frame, text="Montana", variable=montana, onvalue=1, offvalue=0, command=opcionesVacaciones).pack()
Checkbutton(frame, text="Campo", variable=campo, onvalue=1, offvalue=0, command=opcionesVacaciones).pack()

textoFinal=Label(frame)
textoFinal.pack()

raiz.mainloop()