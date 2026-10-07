class Pessoa:
  pessoa = 0
  def __init__(self, nome, idade):

    self.nome = nome
    self.idade = idade
    Pessoa.população += 1

  def __str__(self):
    return (f"Olá meu nome é {self.self.nome} e eu tenho {self.idade} anos")

  def __del__(delf):
    return (f"Essa pessoa não se encontra no momento")

p1 = Pessoa("Alice", 20)
p2 = Pessoa("Zeca", 25)
print(Pessoa.população)