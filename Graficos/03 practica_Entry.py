from tkinter import *
raiz=Tk()
miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

nombreTexto=Entry(miFrame)
nombreTexto.grid(row=0, column=1, padx=10, pady=10)
nombreTexto.config(fg="red", justify="right")

apellidoTexto=Entry(miFrame)
apellidoTexto.grid(row=1, column=1, padx=10, pady=10)

direccionTexto=Entry(miFrame)
direccionTexto.grid(row=2, column=1, padx=10, pady=10)

passTexto=Entry(miFrame)
passTexto.grid(row=3, column=1, padx=10, pady=10)
passTexto.config(show="*")

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) # e de este, o w de west

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Contrasena: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()