from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from vehiculo import *
from plaza import *
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

def scrollPersonas(event, num):
  lbnombre.yview("scroll", int(num), "units")
  lbapellidos.yview("scroll", int(num), "units")
  lbentrada.yview("scroll", int(num), "units")
  lbsalida.yview("scroll", int(num), "units")

def scrollVehiculos(event, num):
  lbmatricula.yview("scroll", int(num), "units")
  lbpersonas.yview("scroll", int(num), "units")
  lbentradave.yview("scroll", int(num), "units")
  lbsalidave.yview("scroll", int(num), "units")
  lbtarifa.yview("scroll", int(num), "units")

def botonRegistrar():
  if(plazaComercial.getPersonas()+int(vspinbox.get()) <= int(plazaComercial.getMaximo())):
    if(opciones.current() == 0):
      if(vnombre.get() != "" and vapellido.get() != ""):
        lbnombre.insert(lbnombre.size()+1, vnombre.get())
        lbapellidos.insert(lbapellidos.size()+1, vapellido.get())
        lbentrada.insert(lbentrada.size()+1, time.strftime("%H:%M"))
        lbsalida.insert(lbsalida.size()+1, "--:--")
        plazaComercial.addPersona(1)
        lpersonasplazav.config(text=str(plazaComercial.getPersonas()))
        lvisitantesv.config(text=str(plazaComercial.getVisitantes()))
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
        automovil = vehiculo(vnombre.get(), int(vspinbox.get()), int(time.strftime("%H%M")))
        vehiculos.append(automovil)
        plazaComercial.addAutos()
        plazaComercial.addMatricula(vnombre.get())
        plazaComercial.addPersona(int(vspinbox.get()))
        lpersonasplazav.config(text=str(plazaComercial.getPersonas()))
        lvehiculoplazav.config(text=str(plazaComercial.getAutos()))
        lvisitantesv.config(text=str(plazaComercial.getVisitantes()))
        vnombre.set("")
        vspinbox.set("1")

      elif(vnombre.get() == ""):
        enombre.focus()
  else:
    messagebox.showinfo(message="Capacidad máxima de personas alcanzada", title="MAXIMO ALCANZADO")

def salida():
  pindices = [lbnombre.curselection(), lbapellidos.curselection()]
  vindice = lbmatricula.curselection() 
  if(len(pindices[0]) != 0):
    lbsalida.delete(pindices[0])
    lbsalida.insert(pindices[0], time.strftime("%H:%M"))
    plazaComercial.subPersona(1)
    lpersonasplazav.config(text=str(plazaComercial.getPersonas()))
    lbnombre.itemconfig(pindices[0], fg="gray", bg="gainsboro")
    lbapellidos.itemconfig(pindices[0], fg="gray", bg="gainsboro")
    lbentrada.itemconfig(pindices[0], fg="gray", bg="gainsboro")
    lbsalida.itemconfig(pindices[0], fg="gray", bg="gainsboro")

  elif(len(pindices[1]) != 0):
    lbsalida.delete(pindices[1])
    lbsalida.insert(pindices[1], time.strftime("%H:%M"))
    plazaComercial.subPersona(1)
    lpersonasplazav.config(text=str(plazaComercial.getPersonas()))
    lbnombre.itemconfig(pindices[1], fg="gray", bg="gainsboro")
    lbapellidos.itemconfig(pindices[1], fg="gray", bg="gainsboro")
    lbentrada.itemconfig(pindices[1], fg="gray", bg="gainsboro")
    lbsalida.itemconfig(pindices[1], fg="gray", bg="gainsboro")


  elif(len(vindice) != 0):
    lbsalidave.delete(vindice)
    lbsalidave.insert(vindice, time.strftime("%H:%M"))
    vehiculos[vindice[0]].setHoraSalida(int(time.strftime("%H%M")))
    vehiculos[vindice[0]].calcularImporte()
    lbtarifa.delete(vindice)
    lbtarifa.insert(vindice, "$" + str(vehiculos[vindice[0]].getImporte()))
    plazaComercial.subAutos()
    plazaComercial.subPersona(int(lbpersonas.get(vindice)))
    lpersonasplazav.config(text=str(plazaComercial.getPersonas()))
    lvehiculoplazav.config(text=str(plazaComercial.getAutos()))
    lbmatricula.itemconfig(vindice, fg="gray", bg="gainsboro")
    lbpersonas.itemconfig(vindice, fg="gray", bg="gainsboro")
    lbentradave.itemconfig(vindice, fg="gray", bg="gainsboro")
    lbsalidave.itemconfig(vindice, fg="gray", bg="gainsboro")
    lbtarifa.itemconfig(vindice, fg="gray", bg="gainsboro")

def buscar():
  ventanaBuscar = Toplevel(root)
  ventanaBuscar.title("Buscar")
  ventanaBuscar.geometry("225x150")

  def ejecutarBusqueda():
    indice = plazaComercial.buscarMatricula(vmatri.get())
    if(indice != False):
      lbmatricula.see(indice)
      lbpersonas.see(indice)
      lbentradave.see(indice)
      lbsalidave.see(indice)
      lbmatricula.itemconfig(indice, bg="dodgerblue")
      lbpersonas.itemconfig(indice, bg="dodgerblue")
      lbentradave.itemconfig(indice, bg="dodgerblue")
      lbsalidave.itemconfig(indice, bg="dodgerblue")
      lbtarifa.itemconfig(indice, bg="dodgerblue")
      ventanaBuscar.destroy()
    else:
      label.config(text="Matricula no encontrada, intente de nuevo")

  vmatri = StringVar()
  label = Label(ventanaBuscar, text="Ingresa la matricula")
  label.pack(pady=10)
  entry = Entry(ventanaBuscar, textvariable=vmatri)
  entry.pack()
  boton = Button(ventanaBuscar, text="Confirmar", command=ejecutarBusqueda)
  boton.pack(pady=10)
  

#ROOT 
root = Tk()
root.title("Control de plaza")
root.resizable(True, True)
root.geometry("725x600")
root.config(bg="whitesmoke")
#OBJETOS
plazaComercial = plaza()
vehiculos = []
#VARIABLES
vopcion = StringVar()
vspinbox = StringVar()
vspinbox.set("1")
vnombre = StringVar()
vapellido = StringVar()
vbuscar = StringVar()
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

lpersonasplaza = Label(root, text="Personas en la plaza: ")
lpersonasplazav = Label(root)
lvehiculoplaza = Label(root, text="Vehiculos en la plaza: ")
lvehiculoplazav = Label(root)
lvisitantes = Label(root, text="Total de visitantes: ")
lvisitantesv = Label(root)
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
#SCROLLBARS
#barnombre = Scrollbar(root)
#barapellidos = Scrollbar(root)
#barentrada = Scrollbar(root)
#barsalida = Scrollbar(root)

#barmatricula = Scrollbar(root)
#barpersonas = Scrollbar(root)
#barentradave = Scrollbar(root)
#barsalidave = Scrollbar(root)
#bartarifa = Scrollbar(root)
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
#BINDINGS
lbnombre.bind("<Up>", lambda e: scrollPersonas(e, -1))
lbapellidos.bind("<Up>", lambda e: scrollPersonas(e, -1))
lbentrada.bind("<Up>", lambda e: scrollPersonas(e, -1))
lbsalida.bind("<Up>", lambda e: scrollPersonas(e, -1))
lbnombre.bind("<Down>", lambda e: scrollPersonas(e, 1))
lbapellidos.bind("<Down>", lambda e: scrollPersonas(e, 1))
lbentrada.bind("<Down>", lambda e: scrollPersonas(e, 1))
lbsalida.bind("<Down>", lambda e: scrollPersonas(e, 1))

lbmatricula.bind("<Up>", lambda e: scrollVehiculos(e, -1))
lbpersonas.bind("<Up>", lambda e: scrollVehiculos(e, -1))
lbentradave.bind("<Up>", lambda e: scrollVehiculos(e, -1))
lbsalidave.bind("<Up>", lambda e: scrollVehiculos(e, -1))
lbentradave.bind("<Up>", lambda e: scrollVehiculos(e, -1))
lbmatricula.bind("<Down>", lambda e: scrollVehiculos(e, 1))
lbpersonas.bind("<Down>", lambda e: scrollVehiculos(e, 1))
lbentradave.bind("<Down>", lambda e: scrollVehiculos(e, 1))
lbsalidave.bind("<Down>", lambda e: scrollVehiculos(e, 1))
lbentradave.bind("<Down>", lambda e: scrollVehiculos(e, 1))

#BUTTONS
bregistrar = Button(root, text="REGISTRAR", command=botonRegistrar)
bsalida = Button(root, text="MARCAR SALIDA", command=salida)
bbusqueda = Button(root, text="BUSCAR", command=buscar)
#GRIDS
ltipo.grid(pady=10, row=0, column=0)
opciones.grid(pady=10, row=0, column=1)
bregistrar.grid(pady=10, padx=15, row=0, column=2)
bsalida.grid(pady=10, row=0, column=3)
bbusqueda.grid(pady=10, row=0, column=4)
lnombre.grid(pady=10, row=1, column=0)
enombre.grid(pady=10, row=1, column=1)
lapellido.grid(pady=10, row=1, column=2)
lpersonasplaza.grid(pady=10, row=1, column=4)
lpersonasplazav.grid(pady=10, row=1, column=5)
eapellido.grid(pady=10, row=1, column=3)
lpersonas.grid(pady=10, row=2, column=0)
spersonas.grid(pady=10, row=2, column=1)
lhora.grid(pady=10, row=2, column=2)
lhora_actual.grid(pady=10, row=2, column=3)
lvehiculoplaza.grid(pady=10, row=2, column=4)
lvehiculoplazav.grid(pady=10, row=2, column=5)
lnombreslb.grid(pady=10,row=3, column=0)
lapellidoslb.grid(pady=10, row=3, column=1)
lentradalb.grid(pady=10, row=3, column=2)
lsalidalb.grid(pady=10, row=3, column=3)
lvisitantesv.grid(pady=10, row=3, column=5)
lvisitantes.grid(pady=10, row=3, column=4)
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
#PACKS
#barnombre.grid(column=1)
#barapellidos.grid(column=1)
#barentrada.grid(column=1)
#barsalida.grid(column=1)
#barmatricula.grid(column=1)
#barpersonas.grid(column=1)
#barentradave.grid(column=1)
#barsalidave.grid(column=1)
#CONFIGS
#barnombre.config(command=lbnombre.yview)
#barapellidos.config(command=lbapellidos.yview)
#barentrada.config(command = lbentrada.yview)
#barsalida.config(command=lbsalida.yview)
#barmatricula.config(command=lbmatricula.yview)
#barpersonas.config(command = lbpersonas.yview)
#barentradave.config(command = lbentradave.yview)
#barsalidave.config(command=lbsalidave.yview)
#INVOCACIONES DEF
reloj()
modificarInterfaz()
root.mainloop()
