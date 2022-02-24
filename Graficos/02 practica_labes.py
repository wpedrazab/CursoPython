from tkinter import *
root=Tk() #abre la ventana
miFrame=Frame(root, width=500, height=400) #crea el frame
miFrame.pack() #lo ubica dentro de la ventana
milabel=Label(miFrame, text="Hola mundo...")
#milabel.pack() # esto hace que el frame se ajuste al tamano del label
milabel.place(x=100, y=200)

# otra forma de crearlos
Label(miFrame, text="Otro label", fg="red", font=("Verdana", 18)).place(x=100, y=250)

# para mostrar imagenes solo acepta png y gif
miImagen=PhotoImage(file="Imagen.png")
Label(miFrame, image=miImagen).place(x=100, y=50)


root.mainloop()

