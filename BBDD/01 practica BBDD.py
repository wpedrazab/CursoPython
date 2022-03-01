import sqlite3

#Si la BD no existe la crea
miConexion=sqlite3.connect("PrimeraBBDD")

miCursor=miConexion.cursor()

#para la segunda ejecuci[on del programa ya esta linea no hace falta y va a dar error
#miCursor.execute("CREATE TABLE Productos (Nombre_Articulo varchar(50), Precio integer, Seccion varchar(20))")

# Para agregar un unico registro
#miCursor.execute("INSERT INTO Productos VALUES('Balon', 15, 'Deportes')")

#para ingresar varios registros
# variosProductos=[
# 	("Camiseta", 10, "Deportes"),
# 	("Jarron", 90, "Ceramica"),
# 	("Carrito", 20, "Jugueteria")
# ]
# miCursor.executemany("INSERT INTO Productos VALUES (?,?,?)", variosProductos)

#Para consultar data
miCursor.execute("SELECT * FROM Productos")

variosProductos=miCursor.fetchall() #Para traer varios registros

for producto in variosProductos:
	print("Nombre Articulo: ", producto[0], " Precio: ", producto[1])


miConexion.commit()





miConexion.close()