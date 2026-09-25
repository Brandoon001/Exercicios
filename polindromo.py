lista = []

while True:

    entrada = input("Digite uma string (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    lista.append(entrada)

for palindromo in lista:
    if palindromo == palindromo[::-1]:
        print(f"'{palindromo}' é um palíndromo.")
    else:
        print(f"'{palindromo}' não é um palíndromo.")