class vehiculo():

  def __init__(self):
    self.__matricula:str
    self.__personas:int
    self.__horaLlegada:int
    self.__horaSalida:int
    self.__tiempo:int
    self.__importe:float
  
  def setMatricula(self, matricula:str):
    self.__matricula = matricula
  
  def setPersonas(self, personas:int):
    self.__personas = personas

  def setHoraLlegada(self, horaLlegada):
    self.__horaLlegada = horaLlegada

  def setHoraSalida(self, horaSalida):
    self.__horaSalida = horaSalida

  def setTiempo(self, tiempo):
    self.__tiempo = tiempo
  
  def setImporte(self, importe):
    self.__importe = importe
  
  def getMatricula(self):
    return self.__matricula
  
  def getPersonas(self):
    return self.__personas
  
  def getHoraLlegada(self):
    return self.__horaLlegada

  def getHoraSalida(self):
    return self.__horaSalida

  def getTiempo(self):
    return self.__tiempo

  def getImporte(self):
    return self.__importe

  def registrar(self, matricula, hora, personas):
    self.setMatricula(matricula)
    self.setHoraLlegada(hora)
    self.personas(personas)

  def calcularImporte(self):
    self.setTiempo(abs(self.getHoraLlegada()-self.getHoraSalida()))
    tarifa = 20
    self.setImporte((self.getTiempo()/100)*tarifa)

  def salida(self, hora):
    self.setHoraSalida(hora)
    
  