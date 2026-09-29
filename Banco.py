saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

opcao = input("Escolha uma opção: ").lower()

def depositar():
    global saldo, extrato

    valor = float(entry_valor.get())

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("O depósito foi feito!")
        label_resultado.config(text="Depósito realizado com sucesso!")

    else:
        label_resultado.config(text="Valor inválido!")

def sacar():
    global saldo, extrato, numero_saques

    valor = float(entry_valor.get())

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        label_valor.config(text="Saldo insuficiente!")

    elif excedeu_limite:
        label_valor.config(text="Saque excede o limite de R$ 500!")

    elif excedeu_saques:
        label_valor.config(text="Limite de 3 saques atingido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

        print("O saque foi feito!")
        label_valor.config(text="Saque realizado com sucesso!")

    else:
        label_valor.config(text="Valor inválido!")


def mostrar_extrato():
    if not extrato:
        texto = f"Não foram realizadas movimentações.\nSaldo: R$ {saldo:.2f}"
    else:
        texto = f"{extrato}\nSaldo: R$ {saldo:.2f}"

    print(texto)
    label_resultado.config(text=texto)


def sair():
    print("Obrigado por utilizar nosso banco!")
    janela.destroy()

##----------------------------------------------------------------------------##

import tkinter as tk
janela = tk.Tk()

janela.title("Bem vindo ao banco!")
janela.geometry("600x350")
janela.configure(bg="lightblue")

label1 = tk.Label(
    janela,
    text="Bem vindo ao banco!",
    font=("Arial", 16),
    bg="lightblue",
    fg="black"
)

label1.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=25
)

label_valor = tk.Label(
    janela,
    text="Digite o valor:",
    font=("Arial", 12),
    bg="lightblue",
    fg="black"
)

label_valor.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)

entry_valor = tk.Entry(
    janela,
    font=("Arial", 12)
)

entry_valor.grid(
    row=1,
    column=2,
    columnspan=2,
    padx=10
)

button_depositar = tk.Button(
    janela,
    text="Depositar",
    command=depositar,
    activebackground="yellow"
)

button_depositar.grid(
    row=2,
    column=0,
    padx=5,
    pady=20
)

button_sacar = tk.Button(
    janela,
    text="Sacar",
    command=sacar,
    activebackground="yellow"
)

button_sacar.grid(
    row=2,
    column=1,
    padx=5,
    pady=20
)

button_extrato = tk.Button(
    janela,
    text="Extrato",
    command=mostrar_extrato,
    activebackground="yellow"
)

button_extrato.grid(
    row=2,
    column=2,
    padx=5,
    pady=20
)

button_sair = tk.Button(
    janela,
    text="Sair",
    command=sair,
    activebackground="yellow"
)

button_sair.grid(
    row=2,
    column=3,
    padx=5,
    pady=20
)

label_resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 12),
    bg="lightblue",
    fg="black",
    justify="left"
)

label_resultado.grid(
    row=3,
    column=0,
    columnspan=4,
    pady=20
)

janela.mainloop()