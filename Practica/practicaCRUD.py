from tkinter import *
from tkinter import messagebox
import sqlite3

#------------funciones asociadas a los botones y el menu
def conexionBD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	try:
		miCursor.execute('''
			CREATE TABLE DatosUsuarios (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			Nombre_Usuario varchar(50),
			Pass varchar(20),
			Apellido varchar(50),
			Direccion varchar(50),
			Comentarios varchar(100))
			''')
		messagebox.showinfo("Base de Datos", "BD creada con exito")
	except:
		messagebox.showwarning("Atencion!!!", "La BD ya existe")

def salirApp():
	valor=messagebox.askquestion("Salir App", "Desea Salir?")
	if valor=="yes":
		root.destroy()


def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentario.delete("1.0", END) # esto es para borrar en el Text

def agregar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	# miCursor.execute("INSERT INTO DatosUsuarios VALUES(NULL, '"  + miNombre.get() +
	# 	"','" + miPass.get() + "','" + miApellido.get() + "','" + miDireccion.get() +
	# 	"','" + textoComentario.get("1.0", END) + "')")

	datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)
	miCursor.execute("INSERT INTO DatosUsuarios VALUES(NULL, ?,?,?,?,?)", (datos))


	miConexion.commit()

	messagebox.showinfo("BD", "Registro Agregado")

def consultar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DatosUsuarios WHERE ID="  + miId.get())

	elUsuario=miCursor.fetchall()

	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

	messagebox.showinfo("BD", "Registro Consultado")

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	# miCursor.execute("UPDATE DatosUsuarios SET Nombre_Usuario = '" + 
	# 	miNombre.get() + "', Pass = '" + miPass.get() + "', Apellido = '" +
	# 	miApellido.get() + "', Direccion = '" + miDireccion.get() + "', Comentarios = '" +
	# 	textoComentario.get("1.0", END) + "' WHERE ID =" + miId.get())

	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)
	miCursor.execute("UPDATE DatosUsuarios SET Nombre_Usuario=?,Pass=?,Apellido=?,Direccion=?," +
		"Comentarios=? WHERE ID=" + miId.get(), (datos))

	miConexion.commit()

	messagebox.showinfo("BD", "Registro Actualizado")

def eliminar():
	valor=messagebox.askquestion("Eliminar Usuario", "Desea Elimiar este Usuario?")
	if valor=="yes":
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		miCursor.execute("DELETE FROM DatosUsuarios WHERE ID="  + miId.get())

		miConexion.commit()

		messagebox.showinfo("BD", "Registro Eliminado")


root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bdMenu=Menu(barraMenu, tearoff=0)
bdMenu.add_command(label="Conectar", command=conexionBD)
bdMenu.add_command(label="Salir", command=salirApp)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrra Campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Agregar", command=agregar)
crudMenu.add_command(label="Consultar", command=consultar)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Eliminar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bdMenu)
barraMenu.add_cascade(label="Limpiar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#---------comienzo de campos

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

miId=StringVar() #esto es para poder manipular el contenido de los textbox
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scroolVert=Scrollbar(miFrame, command=textoComentario.yview) #crea el scroll asociado al text
scroolVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scroolVert.set) # asocia el text al scroll


#---------------Inicio de Label

idLabel=Label(miFrame, text="ID: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) 

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) # e de este, o w de west

passLabel=Label(miFrame, text="Contrasena: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#-------------inicio de botones

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Agregar", command=agregar)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonConsultar=Button(miFrame2, text="Consultar", command=consultar)
botonConsultar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

botonEliminar=Button(miFrame2, text="Eliminar", command=eliminar)
botonEliminar.grid(row=0, column=4, sticky="e", padx=10, pady=10)




root.mainloop()
