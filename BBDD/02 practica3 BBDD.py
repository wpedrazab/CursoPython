import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#la triple comilla simple deja crear la instruccion en varias lineas
miCursor.execute('''
	CREATE TABLE Productos (
	ID integer PRIMARY KEY AUTOINCREMENT, #clave primaria autoincremental
	Nombre_Articulo varchar(50) UNIQUE, # para no permitir duplicidad, sin ser clave primaria
	Precio integer,
	Seccion varchar(20))
''')

productos=[
	("Pelota", 20, "Jugueteria"),
	("Pantalon", 15, "Ropa"),
	("Destornillador", 25, "Ferreteria"),
	("Jarron", 45, "Decoracion")
]

miCursor.executemany("INSERT INTO Productos VALUES (null, ?,?,?)", productos)

miConexion.commit()
miConexion.close()