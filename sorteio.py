#
# autores: 
# Michel Silva
#

# sorteia um numero entre 1 e 100
import random

numero = random.randint(1, 100)
print()
print(f"O numero sorteado foi {numero}")


# sorteia um nome de uma lista
lista = ["Davi", "Dani", "Joao", "Maria", "Jose", "Pedro", "Ana", "Paulo"]

nome = random.choice(lista)

print(f"O nome sorteado foi {nome}")


# criar uma função que sorteie um nome de uma lista
def sortear(lista):
    nome = random.choice(lista)
    return nome
  
print(f"O nome sorteado foi {sortear(lista)}")


# crie uma função para cara ou coroa  
def cara_coroa():
    opcao = random.choice(["cara", "coroa"])
    return opcao
  

# criar uma função para jogar dados
def dados():
  """
  Purpose: jogar dados
  """
  dado = random.randint(1, 6)
  return dado


# função corteio por um arquivo
def sorteio_arquivo(nomeArquivo):
  """
  Purpose: sorteia um nome de um arquivo
  """
  arquivo = open(nomeArquivo, "r")
  nomes = arquivo.readlines()
  arquivo.close()
  return random.choice(nomes)
