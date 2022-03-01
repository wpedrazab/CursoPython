import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute("UPDATE Productos SET Precio=99 where Nombre_Articulo ='Pelota'")

miCursor.execute("SELECT * FROM Productos")

variosProductos=miCursor.fetchall() #Para traer varios registros

print(variosProductos)

miCursor.execute("DELETE FROM Productos where ID = 4")

miCursor.execute("SELECT * FROM Productos")

variosProductos=miCursor.fetchall() #Para traer varios registros

print(variosProductos)


miConexion.commit()
miConexion.close()