from tkinter import *

# para graficos se usan varias librerias de Python
# Tkinter, WxPython, PyQT, PyGTK
# Tkinter es un puente entre Python y la libreria TCL/TK comun en otros lenguajes

raiz=Tk()
raiz.title("Ventana Ejemplo")
raiz.resizable(1,1) # para validar si se permita redimencionar, 1 True 0 False, ancho y alto
raiz.iconbitmap("") # el icnono debe estar en la carpeta
raiz.geometry("650x350")
raiz.config(bg="blue")
#para que no abra la consola por detras, se debe cambiar la extension
# del archivo de Python de .py a .pyw
raiz.mainloop() # esto mantiene la ventana activa y debe estar de ultimo

