class Animal:
  def fazer_som(self):
    pass

class Cachorro(Animal):
  def som(self):
    return (f"{self.nome} late")

class Gato(Animal):
  def som(self):
    return (f"{self.nome} mia")

class Chimera(Cachorro, Gato):
  def som(self):
    return (f"{self.nome} faz um som estranho")

def fazer_som(animal):
  print(animal.som)

fazer_som(Cachorro())
fazer_som(Gato())
fazer_som(Chimera())