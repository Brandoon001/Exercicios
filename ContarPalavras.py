lista = []

while True:

    entrada = input("Digite uma string (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    lista.append(entrada)

for frase in lista:
  palavras = frase.split()
  print("-" * 22)
  print(f"Frase: {frase}")
  print(f"Quantidade de palavras: {len(palavras)}")