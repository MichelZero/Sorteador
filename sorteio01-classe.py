#
# autores: 
# Michel Silva
#
#data: 10/12/2022

# criando uma classe para gerir um sorteio

# importando a biblioteca random
import random

class Sorteio01:
  """
  Purpose: criar uma classe para gerir um sorteio
  """
  def __init__(self, arquivo): # construtor da classe Sorteio 
    """
    Purpose: inicializar a classe
    """
    self.arquivo = arquivo 
    self.lista = [] 
    self.ganhador = ""
    self.sortear()
  # end def

  def sortear(self):
    """
    Purpose: sortear um nome de um arquivo
    """
    arquivo = open(self.arquivo, "r") # abrindo o arquivo para leitura 
    self.lista = arquivo.readlines() # lendo o arquivo e armazenando na lista
    arquivo.close() # fechando o arquivo
    self.ganhador = random.choice(self.lista) # sorteando um nome da lista 
  # end def

  def getGanhador(self): 
    """
    Purpose: retornar o ganhador
    """
    return self.ganhador 
  # end def


