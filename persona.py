class persona():
  def __init__(self, nombre, horaEntrada, apellido):
    self.__nombre = nombre
    self.__horaEntrada = horaEntrada
    self.__apellido = apellido
    self.__horaSalida = 0
  
  def getNombre(self):
    return self.__nombre
  
  def getFirma(self):
    return self.__firma
  
  def getHoraEntrada(self):
    return self.__horaEntrada
  
  def getHoraSalida(self):
    return self.__horaSalida

  def setNombre(self, nombre):
    self.__nombre = nombre

  def setHoraEntrada(self, hora):
    self.__horaEntrada = hora
  
  def setHoraSalida(self, hora):
    self.__horaSalida = hora
  
  def setApellido(self, apellido):
    self.__apellido = apellido
  
  def registrar(self, nombre, apellido, hora):
    self.setNombre(nombre)
    self.setApellido(apellido)
    self.setHoraEntrada(hora)
  
  def marcarSalida(self, hora):
    self.setHoraSalida(hora)
