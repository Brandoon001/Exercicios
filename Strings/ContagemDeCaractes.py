'''
Contagem de vogais e consoantes
Escreva um programa que 
conta o número de vogais e consoantes em uma string.

Algortimo Checklist:
- [x] Receber o texto para contar as vogais e consoantes
- [x] Percorrer o texto contando cada vogal
- [x] Percorrer o texto contando cada consoante
- [x] Mostrar o resultado
'''

# Receber o texto para contar as vogais
texto = input('Digite o texto: ')
vogais_no_texto = 0
consoantes_no_texto = 0

# Percorrer o texto contando cada caractere
for caractere in texto:
    if caractere in 'aeiouAEIOU':
        vogais_no_texto += 1;
    # Percorrer o texto contando cada consoante
    if caractere.lower() in 'bcdfghjlmnpqrstvxzyk':
        consoantes_no_texto += 1

print(f'O texto "{texto}" tem {vogais_no_texto} vogais')
print(f'e tem {consoantes_no_texto} consoantes')
