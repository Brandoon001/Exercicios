class Copo:
  def __init__(self, volume):
    self.volume = volume
 
  def encher(self):
    print("O copo está cheio.")
 
  def beber(self):
    print("Você bebeu a água.")

  def __del__(self):
    print("Copo caiu e quebrou.")
 
meu_copo = Copo(250)
meu_copo.encher()
meu_copo.beber()
del meu_copo
