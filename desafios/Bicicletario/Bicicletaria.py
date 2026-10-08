class Bicicleta:

  quantidade_de_bicicletas = 0

  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
    Bicicleta.quantidade_de_bicicletas += 1

  def informacoes(self):
    print(f"A bicleta é {self.cor}, o modelo dela é {self.modelo} de {self.ano}, o valor dela está de {self.valor:.2f}")

  def vender(bicicleta):
    print("Bicicleta vendida!")

  def buzinar(self):
    print("Trim Trim")

  def estado(self):
    print("Pedalando")

  def __str__(self):
    return f"{self.modelo} - {self.cor} - {self.ano} - R$ {self.valor:.2f}"
      

'''bicicleta1 = Bicicleta("preta", "Shimano", 2025, 990.90)
bicicleta1.infrmacoes()
bicicleta2 = Bicicleta("Rosa", "Colli", 2023, 880.90)
bicicleta2.infrmacoes()
bicicleta3 = Bicicleta("Branca", "TWT", 2026, 900.90)
bicicleta3.infrmacoes()
bicicleta4 = Bicicleta("Vermelha", "Colli", 2026, 950.90)
bicicleta4.infrmacoes()'''

def menu():

  bicicletas = []

  while True:
      print("Escolha uma opção\n")
      print("Opção 1: Adicionar bicleta")
      print("Opção 2: Informção da bicicleta")
      print("Opção 3: Vender")
      print("Opção 3: Ações")
      print("Opção 4: Sair")
      opcao = input("Opção: ")

      match opcao:
        case "1":
          cor = input("Qual a cor? ")
          modelo = input("Qual o modelo? ")
          ano = input("Qual o ano? ")
          valor = input("Informe o valor:" )
          bicicletas[Bicicleta.quantidade_de_bicicletas] = (Bicicleta(cor, modelo, ano, valor))
        case "2":
          num = int("Entre com um número da bicicleta")
          print(bicicletas[num])
        case "3":
          num = int("Teste da bicleta")
          bicicletas[num].buzinar()
          bicicletas[num].estado()
        case "4":
          num = int(input(""))


if __name__ == "__main__":
  menu()
          