#
# autores: 
# Michel Silva
#
#data: 10/12/2022

# criando uma classe para gerir um sorteio

# importando a biblioteca random
import random

class Sorteio02:
  def __init__(self, participantes, premios) -> None:
    self.participantes = participantes
    self.premios = premios
    self.sortear()
    
  def sortear(self):
    self.ganhador = random.choice(self.participantes)
    self.premio = random.choice(self.premios)
    
  def imprimirResultado(self):
    print(f"O ganhador foi {self.ganhador} e o premio foi {self.premio}")
    

################################
# teste da classe Sorteio02
sorteio = Sorteio02(["Davi", "Dani", "Joao", "Maria", "Jose", "Pedro", "Ana", "Paulo"], ["TV", "Notebook", "Celular", "Carro", "Moto"])

# realizando o sorteio
sorteio.sortear()

# imprimindo o resultado
sorteio.imprimirResultado()
