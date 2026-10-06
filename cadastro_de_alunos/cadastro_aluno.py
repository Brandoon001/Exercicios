import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random


# ============================================================
# CONFIGURAÇÕES
# ============================================================

ARQUIVO = "alunos.json"

alunos = {}


# ============================================================
# CORES
# ============================================================

COR_PRINCIPAL = "#172554"
COR_SECUNDARIA = "#2563eb"
COR_FUNDO = "#f4f6f8"
COR_BRANCO = "#ffffff"
COR_TEXTO = "#1e293b"
COR_BORDA = "#e2e8f0"
COR_SUCESSO = "#15803d"


# ============================================================
# CARREGAR E SALVAR ALUNOS
# ============================================================

def carregar_alunos():
    global alunos

    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                alunos = json.load(arquivo)

        except (json.JSONDecodeError, OSError):
            alunos = {}


def salvar_alunos():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)


# ============================================================
# GERAR MATRÍCULA
# ============================================================

def gerar_matricula():
    ano = "2026"

    numeros = []

    for matricula in alunos:
        if matricula.startswith(ano):
            try:
                numeros.append(int(matricula[4:]))
            except ValueError:
                pass

    if numeros:
        proximo = max(numeros) + 1
    else:
        proximo = 1

    return f"{ano}{proximo:04d}"


# ============================================================
# GERAR SENHA
# ============================================================

def gerar_senha():
    numeros = random.randint(100000, 999999)

    return f"A{numeros}"


# ============================================================
# JANELA PRINCIPAL
# ============================================================

janela = tk.Tk()

janela.title("Sistema Escolar")
janela.geometry("1100x700")
janela.minsize(950, 650)
janela.configure(bg=COR_FUNDO)


# ============================================================
# ESTILO
# ============================================================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Segoe UI", 10, "bold"),
    padding=10
)

style.configure(
    "TEntry",
    font=("Segoe UI", 10),
    padding=8
)

style.configure(
    "TLabel",
    font=("Segoe UI", 10),
    background=COR_BRANCO,
    foreground=COR_TEXTO
)

style.configure(
    "Titulo.TLabel",
    font=("Segoe UI", 22, "bold"),
    background=COR_PRINCIPAL,
    foreground="white"
)

style.configure(
    "Subtitulo.TLabel",
    font=("Segoe UI", 10),
    background=COR_PRINCIPAL,
    foreground="#bfdbfe"
)

style.configure(
    "Treeview",
    background="white",
    foreground=COR_TEXTO,
    fieldbackground="white",
    rowheight=32,
    font=("Segoe UI", 9)
)

style.configure(
    "Treeview.Heading",
    background=COR_PRINCIPAL,
    foreground="white",
    font=("Segoe UI", 9, "bold"),
    padding=8
)

style.map(
    "Treeview",
    background=[("selected", COR_SECUNDARIA)],
    foreground=[("selected", "white")]
)


# ============================================================
# LIMPAR JANELA
# ============================================================

def limpar_janela():
    for widget in janela.winfo_children():
        widget.destroy()


# ============================================================
# CABEÇALHO
# ============================================================

def criar_cabecalho(titulo, subtitulo):

    cabecalho = tk.Frame(
        janela,
        bg=COR_PRINCIPAL,
        height=110
    )

    cabecalho.pack(fill="x")
    cabecalho.pack_propagate(False)

    tk.Label(
        cabecalho,
        text=titulo,
        bg=COR_PRINCIPAL,
        fg="white",
        font=("Segoe UI", 22, "bold")
    ).pack(
        anchor="w",
        padx=35,
        pady=(20, 0)
    )

    tk.Label(
        cabecalho,
        text=subtitulo,
        bg=COR_PRINCIPAL,
        fg="#bfdbfe",
        font=("Segoe UI", 10)
    ).pack(
        anchor="w",
        padx=37,
        pady=(3, 0)
    )


# ============================================================
# TELA INICIAL
# ============================================================

def tela_inicial():

    limpar_janela()

    criar_cabecalho(
        "Sistema Escolar",
        "Gerenciamento de alunos"
    )

    centro = tk.Frame(
        janela,
        bg=COR_FUNDO
    )

    centro.pack(
        expand=True
    )

    card = tk.Frame(
        centro,
        bg=COR_BRANCO,
        highlightthickness=1,
        highlightbackground=COR_BORDA,
        padx=50,
        pady=40
    )

    card.pack()

    tk.Label(
        card,
        text="Bem-vindo!",
        bg=COR_BRANCO,
        fg=COR_PRINCIPAL,
        font=("Segoe UI", 24, "bold")
    ).pack(pady=(0, 8))

    tk.Label(
        card,
        text="Escolha uma opção para continuar",
        bg=COR_BRANCO,
        fg="#64748b",
        font=("Segoe UI", 10)
    ).pack(pady=(0, 30))

    ttk.Button(
        card,
        text="👨‍🎓  Cadastrar aluno",
        command=tela_cadastro
    ).pack(
        fill="x",
        pady=6
    )

    ttk.Button(
        card,
        text="🔐  Login do aluno",
        command=tela_login
    ).pack(
        fill="x",
        pady=6
    )

    tk.Label(
        card,
        text=f"Alunos cadastrados: {len(alunos)}",
        bg=COR_BRANCO,
        fg="#64748b",
        font=("Segoe UI", 9)
    ).pack(pady=(25, 0))


# ============================================================
# CRIAR CAMPO
# ============================================================

def criar_campo(parent, texto, linha, coluna, largura=25):

    tk.Label(
        parent,
        text=texto,
        bg=COR_BRANCO,
        fg=COR_TEXTO,
        font=("Segoe UI", 9, "bold")
    ).grid(
        row=linha,
        column=coluna,
        sticky="w",
        padx=10,
        pady=(8, 3)
    )

    entrada = ttk.Entry(
        parent,
        width=largura
    )

    entrada.grid(
        row=linha + 1,
        column=coluna,
        sticky="ew",
        padx=10,
        pady=(0, 8)
    )

    return entrada


# ============================================================
# CADASTRO DO ALUNO
# ============================================================

def tela_cadastro():

    limpar_janela()

    criar_cabecalho(
        "Cadastro de aluno",
        "Preencha os dados abaixo para realizar seu cadastro"
    )

    principal = tk.Frame(
        janela,
        bg=COR_FUNDO
    )

    principal.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    formulario = tk.Frame(
        principal,
        bg=COR_BRANCO,
        highlightthickness=1,
        highlightbackground=COR_BORDA
    )

    formulario.pack(
        fill="both",
        expand=True
    )

    tk.Label(
        formulario,
        text="Dados pessoais",
        bg=COR_BRANCO,
        fg=COR_PRINCIPAL,
        font=("Segoe UI", 14, "bold")
    ).grid(
        row=0,
        column=0,
        columnspan=4,
        sticky="w",
        padx=20,
        pady=(15, 5)
    )

    # Linha 1
    entrada_nome = criar_campo(
        formulario,
        "Nome completo",
        1,
        0,
        30
    )

    entrada_sexo = criar_campo(
        formulario,
        "Sexo",
        1,
        1,
        15
    )

    entrada_data = criar_campo(
        formulario,
        "Data de nascimento",
        1,
        2,
        20
    )

    entrada_cpf = criar_campo(
        formulario,
        "CPF",
        1,
        3,
        20
    )

    # Linha 2
    entrada_endereco = criar_campo(
        formulario,
        "Endereço",
        3,
        0,
        30
    )

    entrada_cidade = criar_campo(
        formulario,
        "Cidade",
        3,
        1,
        20
    )

    entrada_uf = criar_campo(
        formulario,
        "UF",
        3,
        2,
        10
    )

    entrada_cep = criar_campo(
        formulario,
        "CEP",
        3,
        3,
        15
    )

    # Linha 3
    entrada_pai = criar_campo(
        formulario,
        "Nome do pai",
        5,
        0,
        30
    )

    entrada_mae = criar_campo(
        formulario,
        "Nome da mãe",
        5,
        1,
        30
    )

    entrada_fone = criar_campo(
        formulario,
        "Telefone",
        5,
        2,
        20
    )

    entrada_rg = criar_campo(
        formulario,
        "RG",
        5,
        3,
        20
    )

    # Informação
    tk.Label(
        formulario,
        text=(
            "A matrícula e a senha serão geradas automaticamente "
            "após o cadastro."
        ),
        bg=COR_BRANCO,
        fg="#64748b",
        font=("Segoe UI", 9)
    ).grid(
        row=7,
        column=0,
        columnspan=4,
        sticky="w",
        padx=30,
        pady=(10, 5)
    )

    # Botões
    botoes = tk.Frame(
        formulario,
        bg=COR_BRANCO
    )

    botoes.grid(
        row=8,
        column=0,
        columnspan=4,
        sticky="e",
        padx=20,
        pady=15
    )

    ttk.Button(
        botoes,
        text="Voltar",
        command=tela_inicial
    ).pack(
        side="left",
        padx=5
    )

    def realizar_cadastro():

        nome = entrada_nome.get().strip()
        sexo = entrada_sexo.get().strip()
        endereco = entrada_endereco.get().strip()
        cidade = entrada_cidade.get().strip()
        uf = entrada_uf.get().strip()
        pai = entrada_pai.get().strip()
        mae = entrada_mae.get().strip()
        fone = entrada_fone.get().strip()
        cep = entrada_cep.get().strip()
        rg = entrada_rg.get().strip()
        cpf = entrada_cpf.get().strip()
        data_nascimento = entrada_data.get().strip()

        if not nome:
            messagebox.showwarning(
                "Atenção",
                "Digite o nome do aluno."
            )
            entrada_nome.focus()
            return

        if not cpf:
            messagebox.showwarning(
                "Atenção",
                "Digite o CPF do aluno."
            )
            entrada_cpf.focus()
            return

        # Verifica CPF duplicado
        for aluno in alunos.values():

            if aluno["cpf"] == cpf:

                messagebox.showerror(
                    "CPF já cadastrado",
                    "Já existe um aluno cadastrado com este CPF."
                )

                entrada_cpf.focus()

                return

        # Gera automaticamente
        matricula = gerar_matricula()
        senha = gerar_senha()

        aluno = {
            "nome": nome,
            "sexo": sexo,
            "endereco": endereco,
            "cidade": cidade,
            "uf": uf.upper(),
            "pai": pai,
            "mae": mae,
            "fone": fone,
            "cep": cep,
            "rg": rg,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "matricula": matricula,
            "senha": senha
        }

        alunos[matricula] = aluno

        salvar_alunos()

        messagebox.showinfo(
            "Cadastro realizado!",
            f"Aluno cadastrado com sucesso!\n\n"
            f"Nome: {nome}\n"
            f"Matrícula: {matricula}\n"
            f"Senha inicial: {senha}\n\n"
            f"Guarde essas informações para realizar o login."
        )

        tela_login()

    ttk.Button(
        botoes,
        text="Cadastrar aluno",
        command=realizar_cadastro
    ).pack(
        side="left",
        padx=5
    )

    entrada_nome.focus()


# ============================================================
# TELA DE LOGIN
# ============================================================

def tela_login():

    limpar_janela()

    criar_cabecalho(
        "Login do aluno",
        "Acesse sua área acadêmica"
    )

    centro = tk.Frame(
        janela,
        bg=COR_FUNDO
    )

    centro.pack(
        expand=True
    )

    card = tk.Frame(
        centro,
        bg=COR_BRANCO,
        highlightthickness=1,
        highlightbackground=COR_BORDA,
        padx=45,
        pady=40
    )

    card.pack()

    tk.Label(
        card,
        text="Área do aluno",
        bg=COR_BRANCO,
        fg=COR_PRINCIPAL,
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(0, 8))

    tk.Label(
        card,
        text="Entre utilizando sua matrícula e senha",
        bg=COR_BRANCO,
        fg="#64748b",
        font=("Segoe UI", 9)
    ).pack(pady=(0, 25))

    tk.Label(
        card,
        text="Matrícula",
        bg=COR_BRANCO,
        fg=COR_TEXTO,
        font=("Segoe UI", 9, "bold")
    ).pack(anchor="w")

    entrada_matricula = ttk.Entry(
        card,
        width=35
    )

    entrada_matricula.pack(
        pady=(5, 15)
    )

    tk.Label(
        card,
        text="Senha",
        bg=COR_BRANCO,
        fg=COR_TEXTO,
        font=("Segoe UI", 9, "bold")
    ).pack(anchor="w")

    entrada_senha = ttk.Entry(
        card,
        width=35,
        show="•"
    )

    entrada_senha.pack(
        pady=(5, 20)
    )

    def realizar_login():

        matricula = entrada_matricula.get().strip()
        senha = entrada_senha.get().strip()

        if not matricula or not senha:

            messagebox.showwarning(
                "Atenção",
                "Digite a matrícula e a senha."
            )

            return

        aluno = alunos.get(matricula)

        if aluno is None:

            messagebox.showerror(
                "Login inválido",
                "Matrícula não encontrada."
            )

            return

        if aluno["senha"] != senha:

            messagebox.showerror(
                "Login inválido",
                "Senha incorreta."
            )

            return

        tela_aluno(aluno)

    ttk.Button(
        card,
        text="Entrar",
        command=realizar_login
    ).pack(
        fill="x"
    )

    ttk.Button(
        card,
        text="Voltar",
        command=tela_inicial
    ).pack(
        fill="x",
        pady=(8, 0)
    )

    entrada_matricula.focus()

    entrada_matricula.bind(
        "<Return>",
        lambda evento: entrada_senha.focus()
    )

    entrada_senha.bind(
        "<Return>",
        lambda evento: realizar_login()
    )


# ============================================================
# ÁREA DO ALUNO
# ============================================================

def tela_aluno(aluno):

    limpar_janela()

    criar_cabecalho(
        "Área do aluno",
        f"Bem-vindo, {aluno['nome']}"
    )

    principal = tk.Frame(
        janela,
        bg=COR_FUNDO
    )

    principal.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    # Card de identificação
    identificacao = tk.Frame(
        principal,
        bg=COR_PRINCIPAL,
        padx=25,
        pady=20
    )

    identificacao.pack(
        fill="x",
        pady=(0, 20)
    )

    tk.Label(
        identificacao,
        text=aluno["nome"],
        bg=COR_PRINCIPAL,
        fg="white",
        font=("Segoe UI", 20, "bold")
    ).pack(anchor="w")

    tk.Label(
        identificacao,
        text=f"Matrícula: {aluno['matricula']}",
        bg=COR_PRINCIPAL,
        fg="#bfdbfe",
        font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(4, 0))

    # Dados
    dados = tk.Frame(
        principal,
        bg=COR_BRANCO,
        highlightthickness=1,
        highlightbackground=COR_BORDA
    )

    dados.pack(
        fill="both",
        expand=True
    )

    tk.Label(
        dados,
        text="Meus dados",
        bg=COR_BRANCO,
        fg=COR_PRINCIPAL,
        font=("Segoe UI", 14, "bold")
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="w",
        padx=25,
        pady=(20, 15)
    )

    campos = [
        ("Nome", aluno["nome"]),
        ("Matrícula", aluno["matricula"]),
        ("Sexo", aluno["sexo"]),
        ("Data de nascimento", aluno["data_nascimento"]),
        ("CPF", aluno["cpf"]),
        ("RG", aluno["rg"]),
        ("Telefone", aluno["fone"]),
        ("Endereço", aluno["endereco"]),
        ("Cidade", aluno["cidade"]),
        ("UF", aluno["uf"]),
        ("CEP", aluno["cep"]),
        ("Pai", aluno["pai"]),
        ("Mãe", aluno["mae"])
    ]

    for i, (campo, valor) in enumerate(campos):

        linha = (i // 2) + 1
        coluna = i % 2

        bloco = tk.Frame(
            dados,
            bg=COR_BRANCO
        )

        bloco.grid(
            row=linha,
            column=coluna,
            sticky="ew",
            padx=25,
            pady=7
        )

        tk.Label(
            bloco,
            text=campo,
            bg=COR_BRANCO,
            fg="#64748b",
            font=("Segoe UI", 8, "bold")
        ).pack(anchor="w")

        tk.Label(
            bloco,
            text=valor if valor else "Não informado",
            bg=COR_BRANCO,
            fg=COR_TEXTO,
            font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(2, 0))

    dados.grid_columnconfigure(0, weight=1)
    dados.grid_columnconfigure(1, weight=1)

    # Botão sair
    ttk.Button(
        principal,
        text="Sair da conta",
        command=tela_inicial
    ).pack(
        anchor="e",
        pady=(15, 0)
    )


# ============================================================
# INICIALIZAÇÃO
# ============================================================

carregar_alunos()

tela_inicial()

janela.mainloop()