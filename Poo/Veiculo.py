class Veiculo:

  quantidade_veiculos = 0

  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    Veiculo.quantidade_veiculos += 1
 
  def exibir_informacoes(self):
    print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

meu_carro = Veiculo("Toyota", "Corolla", 2020)
outro_carro = Veiculo("Honda", "Civic",2015)
minha_bicicleta = Veiculo("Colli", "RX33", 2024)
meu_carro.exibir_informacoes()
outro_carro.exibir_informacoes()
minha_bicicleta.exibir_informacoes()
print(f"tenho {Veiculo.quantidade_veiculos} veículos")