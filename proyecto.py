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
    spersonas.config(state="readonly")
    eapellido.config(state=DISABLED)
    vapellido.set(" ")
  elif(opciones.current() == 0):
    lnombre.config(text="Nombre: ")
    spersonas.config(state=DISABLED)
    eapellido.config(state=NORMAL)
    vspinbox.set("1")
  lnombre.after(200, modificarInterfaz)

def botonRegistrar():
  if(opciones.current() == 0):
    if(vnombre.get() != "" and vapellido.get() != ""):
      lbnombre.insert(lbnombre.size()+1, vnombre.get())
      lbapellidos.insert(lbapellidos.size()+1, vapellido.get())
      lbentrada.insert(lbentrada.size()+1, time.strftime("%H:%M"))
      lbsalida.insert(lbsalida.size()+1, "--:--")
      vnombre.set("")
      vapellido.set("")

    elif(vnombre.get() == ""):
      enombre.focus()

    elif(vapellido.get() == ""):
      eapellido.focus()
  
  elif(opciones.current() == 1):
    if(vnombre.get() != ""):
      lbmatricula.insert(lbmatricula.size()+1, vnombre.get())
      lbpersonas.insert(lbpersonas.size()+1, vspinbox.get())
      lbentradave.insert(lbentradave.size()+1, time.strftime("%H:%M"))
      lbsalidave.insert(lbsalidave.size()+1, "--:--")
      lbtarifa.insert(lbtarifa.size()+1, "$--.--")
      vnombre.set("")
      vspinbox.set("1")
      automovil = vehiculo(vnombre.get(), int(vspinbox.get()), int(time.strftime("%H%M")))
      vehiculos.append(automovil)
    elif(vnombre.get() == ""):
      enombre.focus()

def salida():
  
  if(opciones.current() == 0):
    indice = lbnombre.curselection()
    lbsalida.delete(indice)
    lbsalida.insert(indice, time.strftime("%H:%M"))

  elif(opciones.current() == 1):
    indice = lbmatricula.curselection()
    lbsalidave.delete(indice)
    lbsalidave.insert(indice, time.strftime("%H:%M"))
    vehiculos[indice[0]].setHoraSalida(int(time.strftime("%H%M")))
    vehiculos[indice[0]].calcularImporte()
    lbtarifa.delete(indice)
    lbtarifa.insert(indice, "$" + str(vehiculos[indice[0]].getImporte()))

#ROOT 
root = Tk()
root.title("Control de plaza")
root.resizable(True, True)
root.geometry("700x600")
root.config(bg="whitesmoke")
#OBJETOS
plazaComercial = plaza()
vehiculos = []
personas = []
#VARIABLES
vopcion = StringVar()
vspinbox = StringVar()
vspinbox.set("1")
vnombre = StringVar()
vapellido = StringVar()
#LABELS
ltipo = Label(root, text="Tipo: ")

lnombre = Label(root, text="Nombre: ")
lapellido = Label(root, text="Apellidos: ")

lpersonas = Label(root, text="Personas: ")
lhora = Label(root, text="Hora: ")
lhora_actual = Label(root)

lnombreslb = Label(root, text="NOMBRES:")
lapellidoslb = Label(root, text="APELLIDOS:")
lentradalb = Label(root, text="HORA DE ENTRADA:")
lsalidalb = Label(root, text="HORA DE SALIDA:")

lmatriculalb = Label(root, text="MATRICULAS:")
lpersonaslb = Label(root, text="PERSONAS:")
lentradavelb = Label(root, text="HORA DE ENTRADA:")
lsalidavelb = Label(root, text="HORA DE SALIDA:")
ltarifalb = Label(root, text="TARIFA:")
#ENTRYS
enombre = Entry(root, textvariable=vnombre)
eapellido = Entry(root, textvariable=vapellido)
#SPINBOX
spersonas = Spinbox(root, from_=1, to=30, state="readonly", textvariable=vspinbox)
#COMBOBOX
opciones = ttk.Combobox(root, width=15, textvariable=vopcion)
opciones['values'] = (' Persona',
                      ' Vehiculo')
opciones.current(0)
#LISTBOX
lbnombre = Listbox(root)
lbapellidos = Listbox(root)
lbentrada = Listbox(root) 
lbsalida = Listbox(root)

lbmatricula = Listbox(root)
lbpersonas = Listbox(root)
lbentradave = Listbox(root)
lbsalidave = Listbox(root)
lbtarifa = Listbox(root)
#BUTTONS
bregistrar = Button(root, text="REGISTRAR", command=botonRegistrar)
bsalida = Button(root, text="MARCAR SALIDA", command=salida)
#GRIDS
ltipo.grid(pady=10, row=0, column=0)
opciones.grid(pady=10, row=0, column=1)
lnombre.grid(pady=10, row=1, column=0)
enombre.grid(pady=10, row=1, column=1)
lapellido.grid(pady=10, row=1, column=2)
eapellido.grid(pady=10, row=1, column=3)
bregistrar.grid(pady=10, padx=15, row=1, column=4)
lpersonas.grid(pady=10, row=2, column=0)
spersonas.grid(pady=10, row=2, column=1)
lhora.grid(pady=10, row=2, column=2)
lhora_actual.grid(pady=10, row=2, column=3)
bsalida.grid(pady=10, row=2, column=4)
lnombreslb.grid(pady=10,row=3, column=0)
lapellidoslb.grid(pady=10, row=3, column=1)
lentradalb.grid(pady=10, row=3, column=2)
lsalidalb.grid(pady=10, row=3, column=3)
lbnombre.grid(pady=10, padx=5, row=4, column=0)
lbapellidos.grid(pady=10, padx=5, row=4, column=1)
lbentrada.grid(pady=10, padx=5, row=4, column=2)
lbsalida.grid(pady=10, padx=5, row=4, column=3)
lmatriculalb.grid(pady=10, row=5, column=0)
lpersonaslb.grid(pady=10, row=5, column=1)
lentradavelb.grid(pady=10, row=5, column=2)
lsalidavelb.grid(pady=10, row=5, column=3)
ltarifalb.grid(pady=10, row=5, column=4)
lbmatricula.grid(pady=10, padx=5, row=6, column=0)
lbpersonas.grid(pady=10, padx=5, row=6, column=1)
lbentradave.grid(pady=10, padx=5, row=6, column=2)
lbsalidave.grid(pady=10, padx=5, row=6, column=3)
lbtarifa.grid(pady=10, padx=5, row=6, column=4)
#INVOCACIONES DEF
reloj()
modificarInterfaz()

root.mainloop()
