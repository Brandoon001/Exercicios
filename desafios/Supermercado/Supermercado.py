from pathlib import Path

itens = {}

pasta_atual = Path(__file__).parent.absolute()
print(pasta_atual)

def abrir(nome):
    return open(pasta_atual / nome, 'r', encoding='utf-8')

def salvar_lista(itens):
    with open(pasta_atual / 'lista_de_compras.txt', 'w', encoding='utf-8') as lista_compras:
        for item, valor in itens.items():
            lista_compras.write(f"{item}: R$ {valor:.2f}\n")
    print("Lista de compras salva com sucesso.")

def carregar_lista():
    itens_carregados = {}
    try:
        with abrir(pasta_atual / 'lista_de_compras.txt') as lista_compras:
            for linha in lista_compras:
                item, valor = linha.strip().split(': R$ ')
                itens_carregados[item] = float(valor)
    except FileNotFoundError:
        print("Arquivo de lista de compras não encontrado. Iniciando com uma lista vazia.")
    return itens_carregados

def exibir_lista(itens):
    if not itens:
        print("A lista de compras está vazia.")
    else:
        print("Lista de Compras:")
        for item, valor in itens.items():
            print(f"{item}: R$ {valor:.2f}")
        print(f"Total: R$ {sum(itens.values()):.2f}")

def carregar_lista():
    itens_carregados = {}
    try:
        with abrir('lista_de_compras.txt') as lista_compras:
            for linha in lista_compras:
                item, valor = linha.strip().split(': R$ ')
                itens_carregados[item] = float(valor)
    except FileNotFoundError:
        print("Arquivo de lista de compras não encontrado. Iniciando com uma lista vazia.")
    return itens_carregados

itens = carregar_lista()
total = sum(itens.values())

def adicionar_item(item, valor):
    global total

    if item in itens:
        total -= itens[item]

    itens[item] = valor
    total += valor

    print(
        f"Item {item} adicionado com valor "
        f"R$ {valor:.2f}. "
        f"Total atualizado: R$ {total:.2f}"
    )

def remover_item(item):
    if item in itens:
        valor = itens.pop(item)
        global total
        total -= valor
        print(f"Item {item} removido com valor R$ {valor:.2f}. Total atualizado: R$ {total:.2f}")
    else:
        print(f"Item {item} não encontrado na lista.")

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista de compras")
    print("4. Salvar lista de compras")
    print("5. Sair")
    return int(input("Escolha uma opção: "))

def main():
    while True:
        opcao = exibir_menu()
        match opcao:
            case 1:
                item = input("Digite o nome do item: ")
                valor = float(input("Digite o valor do item: "))
                adicionar_item(item, valor)
            case 2:
                item = input("Digite o nome do item a ser removido: ")
                remover_item(item)
            case 3:
                exibir_lista(itens)
            case 4:
                salvar_lista(itens)
            case 5:
                print("Saindo...")
            case _:
                print("Opção inválida. Tente novamente.")
                break  

if __name__ == "__main__":
    main()