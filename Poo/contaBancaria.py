class ContaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo

  def depositar(self,valor):
    if valor < 0:
      print("Saldo insuficiente")
    else:
      self.__saldo += valor

  def sacar(self, valor):
    if valor < 0:
      print("Valor insuficiente")
    else:
      self.__saldo -= valor

  def obter_saldo(self):
    return self.__saldo

conta = ContaBancaria(1000)
conta.depositar(900)
conta.sacar(500)
print(conta.obter_saldo())