class plaza():

  def __init__(self):
    self.__autos = 0
    self.__personas = 0
    self.__maximo = 200
    self.__visitantes = 0
    self.__matriculas = []

  def setMaximo(self, maximo):
    self.__maximo = maximo
  
  def getAutos(self):
    return self.__autos
  
  def getPersonas(self):
    return self.__personas
  
  def getMaximo(self):
    return self.__maximo
  
  def getVisitantes(self):
    return self.__visitantes

  def addMatricula(self, matricula):
    self.__matriculas.append(matricula)

  def addPersona(self, personas):
    self.__personas += personas
    self.__visitantes += personas
  
  def addAutos(self):
    self.__autos += 1

  def subPersona(self, personas):
    self.__personas -= personas
  
  def subAutos(self):
    self.__autos -= 1
  
  def buscarMatricula(self, matricula):
    for x in self.__matriculas:
      if(x == matricula):
        print("Vehiculo encontrado")
        return x
    print("Vehiculo no encontrado")

  def hayLugar(self):
    if(self.__personas <= self.__maximo):
      return True
    else:
      return False