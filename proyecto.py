from tkinter import *
from tkinter import ttk
from vehiculo import *
from plaza import *
from persona import *
import time
#DEF
def reloj():
  lhora_actual.config(text=time.strftime("%H:%M:%S"))
  lhora_actual.after(200,reloj)
def modificarInterfaz():
  if(opciones.current() == 1):
    lnombre.config(text="Matricula: ")
    epersonas.config(state=NORMAL)
    eapellido.config(state=DISABLED)
  elif(opciones.current() == 0):
    lnombre.config(text="Nombre")
    epersonas.config(state=DISABLED)
    eapellido.config(state=NORMAL)

#ROOT 
root = Tk()
root.title("Control de plaza")
root.resizable(True, True)
root.geometry("700x500")
root.config(bg="whitesmoke")
#VARIABLES
opcion = StringVar()
vnombre = StringVar()
vapellido = StringVar()
vpersonas = IntVar()
#LABELS
ltipo = Label(root, text="Tipo: ")
lnombre = Label(root, text="Nombre: ")
lapellido = Label(root, text="Apellido: ")
lpersonas = Label(root, text="Personas: ")
lhora = Label(root, text="Hora: ")
lhora_actual = Label(root)
#ENTRYS
enombre = Entry(root)
eapellido = Entry(root)
epersonas = Entry(root)
#COMBOBOX
opciones = ttk.Combobox(root, width=15, textvariable=opcion)
opciones['values'] = (' Persona',
                      ' Vehiculo')
opciones.current(0)
#BOTON
cambio = Button(root, text="Confirmar", command=modificarInterfaz)
cambio.grid(row=0, column=2)
#GRIDS
ltipo.grid(pady=10, row=0, column=0)
opciones.grid(pady=10, row=0, column=1)
lnombre.grid(pady=10, row=1, column=0)
enombre.grid(pady=10, row=1, column=1)
lapellido.grid(pady=10, row=1, column=2)
eapellido.grid(pady=10, row=1, column=3)
lpersonas.grid(pady=10, row=2, column=0)
epersonas.grid(pady=10, row=2, column=1)
lhora.grid(pady=10, row=2, column=2)
lhora_actual.grid(pady=10, row=2, column=3)
#INVOCACIONES DEF
reloj()
modificarInterfaz()

root.mainloop()
