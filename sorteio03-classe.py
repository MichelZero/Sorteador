#
# autores: 
# Michel Silva
#
#data: 10/12/2022

# criar uma classe em python para gerir um sorteio, os 
# dados devem ser lidos de um arquivo.

# Para criar uma classe em Python que gere um sorteio a partir de
# dados lidos de um arquivo, você pode seguir os seguintes passos:

# 1. Crie uma classe chamada Sorteio que receba um argumento 
# nome_arquivo, que é o nome do arquivo que contém os dados do sorteio.

# 2. Defina um método chamado sortear que realizará o sorteio. 
# Este método deve ler os dados do arquivo usando a função open do 
# Python e armazená-los em uma lista.

# 3. Use a função random.choice do módulo random do Python para
# sortear um item da lista de dados e armazená-lo em uma variável.

# 4. Imprima o resultado do sorteio usando a função print.

# Abaixo, segue um exemplo de como a classe Sorteio pode ser implementada:



# importando a biblioteca random
import random

class Sorteio:
  def __init__(self, nome_arquivo):
    self.nome_arquivo = nome_arquivo

  def sortear(self):
    # Abrir o arquivo e ler os dados
    with open(self.nome_arquivo, 'r') as arquivo:
      dados = arquivo.readlines()

    # Sortear um item da lista de dados
    sorteado = random.choice(dados)

    # Imprimir o resultado
    print(f'O resultado do sorteio é: {sorteado}')


############################################################
# Criar uma instância da classe Sorteio, passando o nome do arquivo de dados como argumento
sorteio = Sorteio('nomes.txt')

# Realizar o sorteio
sorteio.sortear()


