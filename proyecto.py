from tkinter import *
from vehiculo import *
from plaza import *
from persona import *
#ROOT 
root = Tk()
root.title("Control de plaza")
root.resizable(True, True)
root.geometry("700x500")
root.config(bg="whitesmoke")
#PRIMERA VENTANA
btn1 = Button(root, text="Entrada", width=40, height=10).pack(side=LEFT, padx=30)
btn2 = Button(root, text="Salida", width=40, height=10).pack(side=RIGHT, padx=30)

root.mainloop()