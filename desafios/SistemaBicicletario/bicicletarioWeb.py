
from pathlib import Path
from html import escape

from bicicletario import Bicicleta
from bottle import get, post, request, run


PASTA = Path(__file__).resolve().parent
ARQUIVO = PASTA / "bicicletas.txt"


@get("/")
def index():
    return """
        <h1>Sistema de Bicicletário</h1>
        <a href="/cadastro">Adicionar bicicleta</a><br><br>
        <a href="/mostrar">Mostrar bicicletas</a><br><br>
        <a href="/acoes">Ações da bicicleta</a>
    """


@get("/cadastro")
def cadastro_de_bicicleta():
    return """
        <h1>Cadastro de bicicleta</h1>

        <form action="/process" method="post">
            Cor: <input type="text" name="cor" required><br><br>
            Modelo: <input type="text" name="modelo" required><br><br>
            Ano: <input type="number" name="ano" required><br><br>
            Valor: <input type="number" name="valor"
                          min="0" step="0.01" required><br><br>

            <input type="submit" value="Cadastrar">
        </form>

        <br><a href="/">Voltar ao início</a>
    """


def salvar_bicicleta(bicicletas):
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        for bicicleta in bicicletas:
            linha = (
                f"{bicicleta.cor}|"
                f"{bicicleta.modelo}|"
                f"{bicicleta.ano}|"
                f"{bicicleta.valor}\n"
            )
            arquivo.write(linha)


def carregar_bicicletas():
    bicicletas = []

    if not ARQUIVO.exists():
        return bicicletas

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha:
                continue

            dados = linha.split("|")

            if len(dados) != 4:
                continue

            cor, modelo, ano, valor = dados

            bicicletas.append(
                Bicicleta(cor, modelo, ano, valor)
            )

    return bicicletas


@post("/process")
def index_process():
    cor = request.forms.get("cor", "").strip()
    modelo = request.forms.get("modelo", "").strip()
    ano = request.forms.get("ano", "").strip()
    valor = request.forms.get("valor", "").strip()

    if not all([cor, modelo, ano, valor]):
        return "Erro: preencha todos os campos."

    try:
        ano = int(ano)
        valor = float(valor)
    except ValueError:
        return "Erro: informe um ano inteiro e um valor numérico."

    bicicleta = Bicicleta(cor, modelo, ano, valor)

    salvar_bicicleta([bicicleta])

    return f"""
        <h1>Bicicleta cadastrada com sucesso!</h1>
        <p>Cor: {escape(cor)}</p>
        <p>Modelo: {escape(modelo)}</p>
        <p>Ano: {ano}</p>
        <p>Valor: R$ {valor:.2f}</p>

        <a href="/cadastro">Cadastrar outra bicicleta</a><br><br>
        <a href="/mostrar">Ver bicicletas cadastradas</a><br><br>
        <a href="/">Voltar ao início</a>
    """


@get("/mostrar")
def mostrar_bicicletas():
    bicicletas = carregar_bicicletas()

    if not bicicletas:
        return """
            <h1>Nenhuma bicicleta cadastrada.</h1>
            <a href="/cadastro">Cadastrar bicicleta</a><br><br>
            <a href="/">Voltar ao início</a>
        """

    linhas = ""

    for i, bicicleta in enumerate(bicicletas, start=1):
        linhas += f"""
            <tr>
                <td>{i}</td>
                <td>{escape(str(bicicleta.cor))}</td>
                <td>{escape(str(bicicleta.modelo))}</td>
                <td>{escape(str(bicicleta.ano))}</td>
                <td>R$ {escape(str(bicicleta.valor))}</td>
            </tr>
        """

    return f"""
        <h1>Bicicletas cadastradas</h1>

        <table border="1" cellpadding="8">
            <tr>
                <th>Nº</th>
                <th>Cor</th>
                <th>Modelo</th>
                <th>Ano</th>
                <th>Valor</th>
            </tr>
            {linhas}
        </table>

        <br><a href="/cadastro">Cadastrar bicicleta</a><br><br>
        <a href="/">Voltar ao início</a>
    """


@get("/acoes")
def acoes_bicicleta():
    return """
        <h1>Teste da bicicleta</h1>
        <p>Esta funcionalidade ainda precisa ser implementada.</p>
        <a href="/">Voltar ao início</a>
    """


run(host="localhost", port=8080, debug=True)
