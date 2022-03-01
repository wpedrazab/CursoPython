import sqlite3

miConexion=sqlite3.connect("GestionProductos") #crear la tabla

miCursor=miConexion.cursor()

#la triple comilla simple deja crear la instruccion en varias lineas
miCursor.execute('''
	CREATE TABLE Productos (
	Codigo_Articulo varchar(4) PRIMARY KEY,
	Nombre_Articulo varchar(50),
	Precio integer,
	Seccion varchar(20))
''')

# crear la lista con tuplas en su interior para agregar la data
productos=[
	("AR01", "Pelota", 20, "Jugueteria"),
	("AR02", "Pantalon", 15, "Ropa"),
	("AR03", "Destornillador", 25, "Ferreteria"),
	("AR04", "Jarron", 45, "Decoracion")
]

miCursor.executemany("INSERT INTO Productos VALUES (?,?,?,?)", productos)


miConexion.commit()
miConexion.close()