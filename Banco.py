saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato

    try:
        valor = float(entry_valor.get())
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("O depósito foi feito!")
            label_resultado.config(text="Depósito realizado com sucesso!")

        else:
            label_resultado.config(text="Valor inválido!")

    except ValueError:
        label_resultado.config(text="Por favor, insira um valor válido!")

def sacar():
    global saldo, extrato, numero_saques

    try:
        valor = float(entry_valor.get())

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            label_resultado.config(text="Saldo insuficiente!")

        elif excedeu_limite:
            label_resultado.config(text="Saque excede o limite de R$ 500!")

        elif excedeu_saques:
            label_resultado.config(text="Limite de 3 saques atingido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            print("O saque foi feito!")
            label_resultado.config(text="Saque realizado com sucesso!")

        else:
            label_resultado.config(text="Valor inválido!")

    except ValueError:
        label_resultado.config(text="Por favor, insira um valor válido!")


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

janela.title("Banco Digital")

janela.geometry("900x600")

janela.minsize(700, 500)

janela.configure(bg="#F4F7FB")

janela.resizable(True, True)

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

label1 = tk.Label(
    janela,
    text="🏦  Bem-vindo ao Banco!",
    font=("Arial", 24, "bold"),
    bg="#123C73",
    fg="white",
    padx=20,
    pady=15
)

label1.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="ew",
    pady=(0, 25)
)


label_valor = tk.Label(
    janela,
    text="Digite o valor",
    font=("Arial", 13, "bold"),
    bg="#F4F7FB",
    fg="#172033"
)

label_valor.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=20,
    pady=10
)

entry_valor = tk.Entry(
    janela,
    font=("Arial", 14),
    bg="white",
    fg="#172033",
    relief="flat",
    bd=0,
    highlightthickness=2,
    highlightbackground="#D9E2EF",
    highlightcolor="#1E6FD9"
)

entry_valor.grid(
    row=1,
    column=2,
    columnspan=2,
    padx=20,
    pady=10,
    ipady=8,
    sticky="ew"
)

label_resultado = tk.Label(
    janela,
    text="Pronto para realizar uma operação.",
    font=("Arial", 12),
    bg="#F4F7FB",
    fg="#64748B",
    wraplength=700,
    justify="center"
)

label_resultado.grid(
    row=4,
    column=0,
    columnspan=4,
    padx=30,
    pady=25
)

button_depositar = tk.Button(
    janela,
    text="↑  Depositar",
    command=depositar,
    font=("Arial", 11, "bold"),
    bg="#16A085",
    fg="white",
    activebackground="#12866F",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2"
)

button_depositar.grid(
    row=2,
    column=0,
    padx=8,
    pady=20,
    ipady=12,
    sticky="ew"
)


button_sacar = tk.Button(
    janela,
    text="↑  Sacar",
    command=sacar,
    font=("Arial", 11, "bold"),
    bg="#E74C3C",
    fg="white",
    activebackground="#C0392B",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2"
)

button_sacar.grid(
    row=2,
    column=1,
    padx=8,
    pady=20,
    ipady=12,
    sticky="ew"
)


button_extrato = tk.Button(
    janela,
    text="▤  Extrato",
    command=mostrar_extrato,
    font=("Arial", 11, "bold"),
    bg="#1E6FD9",
    fg="white",
    activebackground="#123C73",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2"
)

button_extrato.grid(
    row=2,
    column=2,
    padx=8,
    pady=20,
    ipady=12,
    sticky="ew"
)


button_sair = tk.Button(
    janela,
    text="↪  Sair",
    command=sair,
    font=("Arial", 11, "bold"),
    bg="#64748B",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2"
)

button_sair.grid(
    row=2,
    column=3,
    padx=8,
    pady=20,
    ipady=12,
    sticky="ew"
)

janela.mainloop()