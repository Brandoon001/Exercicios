class Animal:
    """Virtual PET ou Tamagotchi"""
    def __init__(self, nome="", classe="", familia="", idade=0, calorias=0, forca=0):
        self.nome = nome
        self.classe = classe
        self.familia = familia
        self.idade = idade
        self.calorias = calorias
        self.forca = forca
        self.estado = True  # True significa vivo, False significa morto
        self.nascer()

    def nascer(self):
        self.nome = input("Digite o nome do animal: ")
        self.classe = input("Digite a classe do animal: ")
        self.familia = input("Digite a família do animal: ")
        self.idade = int(input("Digite a idade do animal: "))
        self.calorias = int(input("Digite a quantidade de calorias do animal: "))
        self.forca = int(input("Digite a força do animal: "))
        self.estado = True
        print(f"{self.nome} nasceu!")

    def morrer(self):
        self.estado = False
        print(f"{self.nome} morreu!")

    def comer(self, calorias):
        self.testar_estado()
        if self.estado:
            if self.calorias < 100:  # Supondo que 100 seja o limite de calorias
                self.calorias += calorias
                self.forca -= 5  # Comer retira um pouco de força
                print(f"{self.nome} comeu e agora tem {self.calorias} calorias e {self.forca} de força.")
            else:
                print(f"{self.nome} está cheio e não pode comer mais.")
        else:
            print(f"{self.nome} está morto e não pode comer.")

    def correr(self, calorias_perdidas, forca_perdida):
        self.testar_estado()
        if self.estado:
            if self.calorias >= calorias_perdidas and self.forca >= forca_perdida:
                self.calorias -= calorias_perdidas
                self.forca -= forca_perdida
                print(f"{self.nome} correu e agora tem {self.calorias} calorias e {self.forca} de força.")
            else:
                print(f"{self.nome} não tem energia suficiente para correr.")
        else:
            print(f"{self.nome} está morto e não pode correr.")

    def dormir(self, calorias_perdidas, forca_ganha):
        self.testar_estado()
        if self.estado:
            self.calorias -= calorias_perdidas
            self.forca += forca_ganha
            print(f"{self.nome} dormiu e agora tem {self.calorias} calorias e {self.forca} de força.")
        else:
            print(f"{self.nome} está morto e não pode dormir.")

    def testar_estado(self):
        if self.calorias <= 0 or self.forca <= 0:
            self.morrer()


def menu(animal1):
  while True:
    print("\nEscolha uma ação:")
    print("1. Comer")
    print("2. Correr")
    print("3. Dormir")
    print("4. Sair")

    escolha = input("Digite o número da ação desejada: ")

    match escolha:
        case "1":
            animal1.comer(10)  # Exemplo de quantidade de calorias para comer
        case "2":            
            animal1.correr(5, 5)  # Exemplo de quantidade de calorias e força perdidas ao correr
        case "3":
            animal1.dormir(5, 10)  # Exemplo de quantidade de calorias perdidas e força ganha ao dormir
        case "4":
            print("Saindo do jogo...")
            break


def main():
    animal1 = Animal()
    menu(animal1)


if __name__ == "__main__":
    main()