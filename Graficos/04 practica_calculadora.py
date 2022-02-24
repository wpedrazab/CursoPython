from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

operacion=""
resultado=0

# Diseno pantalla

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #columspan hace los botones iguales
pantalla.config(background="black", fg="#03f943", justify="right")

# Pulsaciones de teclado

def numeroPulsado(num):
	global operacion
	if operacion!="":
		numeroPantalla.set(num)
		operacion=""
	else:
		numeroPantalla.set(numeroPantalla.get() + num)

# Suma-----------
def suma(num):
	global operacion
	global resultado
	resultado+=int(num)
	operacion="suma"
	numeroPantalla.set(resultado)

# Resultado
def elResultado():
	global resultado
	numeroPantalla.set(resultado+int(numeroPantalla.get()))
	resultado=0


# 1ra fila de botones
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonD=Button(miFrame, text="/", width=3)
botonD.grid(row=2, column=4)
# 2ra fila de botones
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonM=Button(miFrame, text="X", width=3)
botonM.grid(row=3, column=4)
# 3ra fila de botones
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonR=Button(miFrame, text="-", width=3)
botonR.grid(row=4, column=4)
# 4ra fila de botones
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:elResultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

# Funcionalidad



raiz.mainloop()