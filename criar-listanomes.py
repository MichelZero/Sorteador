#
# autores: 
# Michel Silva
#
# criar uma lista de nomes
# ler uma lista de nomes

def listaNomes(tarefa):
  """
  Purpose: criar ou ler uma lista com nomes
  """
  if tarefa == "criar":
    with open("nomes.txt", "w") as arquivo:
      arquivo.write("Davi, Dani, Joao, Maria, Jose, Pedro, Ana, Paulo")
  elif tarefa == "ler":
    with open("nomes.txt", "r") as arquivo:
      nomes = arquivo.read()
      return nomes.split(", ")
# end def
  
listaNomes("criar")
lista01 = listaNomes("ler")
print(lista01)

####################################################
# importando o modulo de sorteio
from sorteio import sorteio_arquivo

ganhador = sorteio_arquivo("nomes.txt")
print(f"O ganhador foi {ganhador}")
