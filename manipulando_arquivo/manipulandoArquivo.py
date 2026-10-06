from pathlib import Path

pasta_atual = Path(__file__).parent.absolute()
print(pasta_atual)

def abrir(nome):
  return open(pasta_atual / nome, 'r', encoding='utf-8')

'''with abrir('lista_de_compras.txt') as lista_de_compras:
  print(lista_de_compras.read())'''

'''with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
#usando for para percorrer o arquivo
  for linha in lista_de_compras:
    print(linha.strip())
    #usando while para percorrer o arquivo
  linha = lista_de_compras.readline()
  while linha != "":
    print(linha, end="")
    linha = lista_de_compras.readline()'''

'''with abrir('lista_de_compras.txt') as lista_de_compras:
  linhas = lista_de_compras.readlines()
  print(f"O terceiro item da lista é: {linhas[2]}")
  for linha in linhas:
    print(linha.strip(), end=",")

itens_ja_comprados = ['ovos', 'leite']
 
with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    itens_lista_compras = lista_compras.readlines()
 
with open(pasta_atual / 'lista_de_compras_atualizada.txt', 'w') as lista_atualizada:
    for item in itens_lista_compras:
      if item.strip() not in itens_ja_comprados:
        lista_atualizada.write(item)
        print(f"Item {item.strip()} adicionado à lista atualizada.")'''

'''itens_ja_comprados = ['ovos', 'refrigerante']
 
with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    itens_lista_compras = [item for item in lista_compras.readlines() \
    if not item.replace('\n', '') in itens_ja_comprados]
 
with open(pasta_atual / 'lista_de_compras_atualizada.txt', 'w') as lista_atualizada:
    lista_atualizada.writelines(itens_lista_compras)
    print(f"Lista atualizada: {itens_lista_compras}")'''

itens_para_adicionar = ['farinha', 'açúcar', 'fermento']

with open(pasta_atual / 'lista_de_compras.txt', 'a') as lista_compras:
    for item in itens_para_adicionar:
        lista_compras.write(f"\n{item}")
        print(f"Item {item} adicionado à lista de compras.")


    

