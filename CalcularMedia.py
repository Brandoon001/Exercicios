import tkinter as tk
from tkinter import messagebox
import random


# =========================
# FUNÇÕES
# =========================

def calcular_media(numeros):
    if not numeros:
        return 0

    return sum(numeros) / len(numeros)


def gerar_numeros_aleatorios(qtd, minimo, maximo):
    numeros = []

    for _ in range(qtd):
        numero = random.randint(minimo, maximo)
        numeros.append(numero)

    return numeros


def gerar():
    try:
        quantidade = int(entry_quantidade.get())

        if quantidade <= 0:
            messagebox.showwarning(
                "Valor inválido",
                "Digite uma quantidade maior que zero."
            )
            return

        numeros = gerar_numeros_aleatorios(
            quantidade,
            1,
            100
        )

        media = calcular_media(numeros)

        # Atualiza os números
        text_numeros.config(state="normal")

        text_numeros.delete("1.0", tk.END)

        text_numeros.insert(
            tk.END,
            ", ".join(map(str, numeros))
        )

        text_numeros.config(state="disabled")

        # Atualiza a média
        label_media.config(
            text=f"{media:.2f}"
        )

        # Atualiza a quantidade
        label_quantidade.config(
            text=f"{quantidade} números gerados"
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite apenas números inteiros."
        )


def limpar():
    entry_quantidade.delete(0, tk.END)

    text_numeros.config(state="normal")

    text_numeros.delete("1.0", tk.END)

    text_numeros.insert(
        tk.END,
        "Nenhum número gerado"
    )

    text_numeros.config(state="disabled")

    label_media.config(
        text="0.00"
    )

    label_quantidade.config(
        text="0 números gerados"
    )


# =========================
# JANELA
# =========================

janela = tk.Tk()

janela.title("Calculadora de Média")
janela.geometry("700x550")
janela.resizable(False, False)


# =========================
# CORES
# =========================

FUNDO = "#0F172A"
CARD = "#1E293B"
CARD_SECUNDARIO = "#334155"

AZUL = "#3B82F6"
AZUL_HOVER = "#2563EB"

BRANCO = "#F8FAFC"
CINZA = "#94A3B8"

VERDE = "#22C55E"


janela.configure(bg=FUNDO)


# =========================
# TÍTULO
# =========================

frame_titulo = tk.Frame(
    janela,
    bg=FUNDO
)

frame_titulo.pack(
    pady=(35, 20)
)


titulo = tk.Label(
    frame_titulo,
    text="Calculadora de Média",
    font=("Arial", 26, "bold"),
    bg=FUNDO,
    fg=BRANCO
)

titulo.pack()


subtitulo = tk.Label(
    frame_titulo,
    text="Gere números aleatórios e calcule a média",
    font=("Arial", 11),
    bg=FUNDO,
    fg=CINZA
)

subtitulo.pack(
    pady=(5, 0)
)


# =========================
# CARD PRINCIPAL
# =========================

card = tk.Frame(
    janela,
    bg=CARD,
    padx=30,
    pady=25
)

card.pack(
    padx=50,
    fill="x"
)


# =========================
# QUANTIDADE
# =========================

label_input = tk.Label(
    card,
    text="Quantidade de números",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=BRANCO
)

label_input.pack(
    anchor="w"
)


entry_quantidade = tk.Entry(
    card,
    font=("Arial", 14),
    bg=CARD_SECUNDARIO,
    fg=BRANCO,
    insertbackground=BRANCO,
    relief="flat"
)

entry_quantidade.pack(
    fill="x",
    pady=(8, 18),
    ipady=8
)


# =========================
# BOTÕES
# =========================

frame_botoes = tk.Frame(
    card,
    bg=CARD
)

frame_botoes.pack(
    fill="x"
)


botao_gerar = tk.Button(
    frame_botoes,
    text="🎲  Gerar números",
    font=("Arial", 11, "bold"),
    bg=AZUL,
    fg=BRANCO,
    activebackground=AZUL_HOVER,
    activeforeground=BRANCO,
    relief="flat",
    cursor="hand2",
    command=gerar
)

botao_gerar.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10,
    padx=(0, 5)
)


botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    font=("Arial", 11, "bold"),
    bg=CARD_SECUNDARIO,
    fg=BRANCO,
    activebackground="#475569",
    activeforeground=BRANCO,
    relief="flat",
    cursor="hand2",
    command=limpar
)

botao_limpar.pack(
    side="right",
    fill="x",
    expand=True,
    ipady=10,
    padx=(5, 0)
)


# =========================
# RESULTADO
# =========================

frame_resultado = tk.Frame(
    janela,
    bg=CARD,
    padx=30,
    pady=25
)

frame_resultado.pack(
    padx=50,
    pady=20,
    fill="both",
    expand=True
)


# Título dos números
label_resultado_titulo = tk.Label(
    frame_resultado,
    text="Números gerados",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=BRANCO
)

label_resultado_titulo.pack(
    anchor="w"
)


# =========================
# ÁREA DOS NÚMEROS
# =========================

frame_numeros = tk.Frame(
    frame_resultado,
    bg=CARD
)

frame_numeros.pack(
    fill="both",
    expand=True,
    pady=(10, 15)
)


# Caixa dos números
text_numeros = tk.Text(
    frame_numeros,
    height=3,
    font=("Arial", 12),
    bg=CARD,
    fg=CINZA,
    insertbackground=BRANCO,
    relief="flat",
    wrap="word",
    state="disabled"
)

text_numeros.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================
# SCROLL
# =========================

scroll_numeros = tk.Scrollbar(
    frame_numeros,
    command=text_numeros.yview,
    bg=CARD,
    troughcolor=CARD
)

scroll_numeros.pack(
    side="right",
    fill="y"
)


text_numeros.config(
    yscrollcommand=scroll_numeros.set
)


# =========================
# MÉDIA
# =========================

label_media_titulo = tk.Label(
    frame_resultado,
    text="MÉDIA",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=CINZA
)

label_media_titulo.pack()


label_media = tk.Label(
    frame_resultado,
    text="0.00",
    font=("Arial", 28, "bold"),
    bg=CARD,
    fg=VERDE
)

label_media.pack(
    pady=(3, 0)
)


# =========================
# QUANTIDADE GERADA
# =========================

label_quantidade = tk.Label(
    frame_resultado,
    text="0 números gerados",
    font=("Arial", 9),
    bg=CARD,
    fg=CINZA
)

label_quantidade.pack(
    pady=(10, 0)
)


# =========================
# TEXTO INICIAL
# =========================

text_numeros.config(state="normal")

text_numeros.insert(
    tk.END,
    "Nenhum número gerado"
)

text_numeros.config(state="disabled")


# =========================
# INICIAR PROGRAMA
# =========================

janela.mainloop()