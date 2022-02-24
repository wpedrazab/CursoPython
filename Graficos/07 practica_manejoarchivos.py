from tkinter import *
from tkinter import filedialog

raiz=Tk()

def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros Excel", "*.xls"), ("Ficheros de Texto", "*.txt"), ("Todos los ficheros", "*.*")))
	print(fichero)

Button (raiz, text="Abrir fichero", command=abreFichero).pack()




raiz.mainloop()