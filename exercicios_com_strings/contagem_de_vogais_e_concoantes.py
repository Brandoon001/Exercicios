lista = []

while True:

    entrada = input("Digite uma string (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    
    lista.append(entrada)

vogais = 0
consoantes = 0

for string in lista:
    for caractere in string.lower():
        if caractere in "aeiou":
            vogais += 1
        elif caractere.isalpha():
            consoantes += 1

print(f"Strings digitadas: {lista}")
print(f"Quantidade de vogais: {vogais}")
print(f"Quantidade de consoantes: {consoantes}")