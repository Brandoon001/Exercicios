# Escreva um programa que conta o número de palavras em uma frase.
frase = input('Digite uma frase: ')
palavras = frase.split()
quantidade = len(palavras)
print(f'A frase contém {quantidade} palavras.')