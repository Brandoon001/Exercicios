while True:

    entrada = input("Digite uma string (ou 'sair' para encerrar): ")

    if entrada.lower() == "sair":
        break

    lista = []
    palavras = entrada.split()

    for palavra in palavras:
        lista.append(palavra.capitalize())

    frase_capitalizada = " ".join(lista)

    print("-" * 22)
    print(f"Frase: {entrada}")
    print(f"Frase capitalizada: {frase_capitalizada}")