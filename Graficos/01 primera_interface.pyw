from tkinter import *

# para graficos se usan varias librerias de Python
# Tkinter, WxPython, PyQT, PyGTK
# Tkinter es un puente entre Python y la libreria TCL/TK comun en otros lenguajes

raiz=Tk()
raiz.title("Ventana Ejemplo")
raiz.resizable(1,1) # para validar si se permita redimencionar, 1 True 0 False, ancho y alto
raiz.iconbitmap("favicon.ico") # el icnono debe estar en la carpeta
#raiz.geometry("650x350") opcional, ya que la raiz se adapta al frame
raiz.config(bg="blue")
#para que no abra la consola por detras, se debe cambiar la extension
# del archivo de Python de .py a .pyw

miFrame=Frame() #construimos el frame
#miFrame.pack(side="left", anchor="n") # debemos empaquetarlo en la ventana
miFrame.pack(fill="y", expand="true") # fill puede ser both
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=15)
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")

# todo lo que se aplica al frame se puede aplicar a la raiz

raiz.mainloop() # esto mantiene la ventana activa y debe estar de ultimo

