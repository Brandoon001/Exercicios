from bottle import Bottle, request, redirect, run, static_file
from pathlib import Path
from html import escape
from urllib.parse import quote
from datetime import datetime

app = Bottle()
PASTA = Path(__file__).parent
ARQUIVO = PASTA / "arquivo.txt"
CONDICOES = ("Nova", "Seminova")


class Bicicleta:
    quantidade_de_bicicletas = 0

    def __init__(self, cor, modelo, ano, valor, vendida=False, condicao="Nova"):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.vendida = vendida
        self.condicao = condicao
        Bicicleta.quantidade_de_bicicletas += 1

    def informacoes(self):
        return (f"A bicicleta é {self.cor}, modelo {self.modelo}, "
                f"ano {self.ano}, valor R$ {self.valor:.2f}")

    def vender(self):
        if self.vendida:
            return False
        self.vendida = True
        return True

    def buzinar(self):
        return "Trim Trim!"

    def pedalar(self):
        return f"Você simulou uma pedalada na bicicleta {self.modelo}!"

    def estado(self):
        return self.condicao

    def __str__(self):
        return (f"{self.modelo} - {self.cor} - {self.ano} - "
                f"R$ {self.valor:.2f} - {self.condicao}")


def carregar_bicicletas():
    if not ARQUIVO.exists():
        ARQUIVO.write_text("", encoding="utf-8")
        return []

    lista = []
    with ARQUIVO.open("r", encoding="utf-8") as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            linha = linha.strip()
            if not linha:
                continue
            campos = linha.split(";")

            # Aceita os registros antigos (6 campos) e os novos (7 campos).
            if len(campos) == 6:
                identificador, cor, modelo, ano, valor, status = campos
                condicao = "Nova"
            elif len(campos) == 7:
                identificador, cor, modelo, ano, valor, status, condicao = campos
            else:
                raise ValueError(f"Linha {numero_linha} inválida em arquivo.txt.")

            if status not in ("DISPONIVEL", "VENDIDA"):
                raise ValueError(f"Status inválido na linha {numero_linha}.")
            if condicao not in CONDICOES:
                condicao = "Nova"

            lista.append(Bicicleta(
                cor, modelo, int(ano), float(valor),
                vendida=(status == "VENDIDA"), condicao=condicao
            ))

    Bicicleta.quantidade_de_bicicletas = len(lista)
    return lista


def salvar_bicicletas():
    temporario = ARQUIVO.with_suffix(".tmp")
    with temporario.open("w", encoding="utf-8") as arquivo:
        for numero, b in enumerate(bicicletas, start=1):
            status = "VENDIDA" if b.vendida else "DISPONIVEL"
            arquivo.write(
                f"{numero};{b.cor};{b.modelo};{b.ano};{b.valor:.2f};"
                f"{status};{b.condicao}\n"
            )
    temporario.replace(ARQUIVO)


bicicletas = carregar_bicicletas()


def pagina(conteudo, titulo="Bicicletário", mensagem=""):
    aviso = f'<div class="aviso">{escape(mensagem)}</div>' if mensagem else ""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(titulo)} | BikeManager</title>
<link rel="stylesheet" href="/Style.css">
</head>
<body>
<header class="topo">
<a class="logo" href="/">🚲 Bike<span>Manager</span></a>
<nav><a href="/">Início</a><a href="/bicicletas">Estoque</a><a href="/vendidas">Vendidas</a></nav>
</header>
<main>{aviso}{conteudo}</main>
<footer>BikeManager · Sistema de gerenciamento de bicicletas</footer>
</body>
</html>"""


def campo_condicao(atual="Nova"):
    opcoes = "".join(
        f'<option value="{c}" {"selected" if c == atual else ""}>{c}</option>'
        for c in CONDICOES
    )
    return f"""<div><label for="condicao">Condição da bicicleta</label>
<select id="condicao" name="condicao" required>{opcoes}</select></div>"""


@app.get("/Style.css")
def estilo():
    return static_file("Style.css", root=str(PASTA))


@app.get("/")
def inicio():
    total = len(bicicletas)
    vendidas = sum(b.vendida for b in bicicletas)
    disponiveis = total - vendidas
    conteudo = f"""
<section class="hero"><p class="etiqueta">PAINEL DE CONTROLE</p>
<h1>Gerencie suas bicicletas.</h1>
<p>Controle o estoque, cadastre modelos e acompanhe as vendas.</p></section>
<section class="cards">
<article class="card"><p>Total de bicicletas</p><strong>{total}</strong></article>
<article class="card"><p>Disponíveis</p><strong>{disponiveis}</strong></article>
<article class="card"><p>Vendidas</p><strong>{vendidas}</strong></article></section>
<section class="painel" id="cadastro"><h2>＋ Cadastrar bicicleta</h2>
<form action="/adicionar" method="post" class="form-grid">
<div><label for="cor">Cor</label><input id="cor" name="cor" maxlength="60" placeholder="Ex.: Preto" required></div>
<div><label for="modelo">Modelo</label><input id="modelo" name="modelo" maxlength="100" placeholder="Ex.: Mountain Bike" required></div>
<div><label for="ano">Ano</label><input id="ano" name="ano" type="number" min="1885" max="{datetime.now().year + 1}" required></div>
<div><label for="valor">Valor (R$)</label><input id="valor" name="valor" type="number" min="0.01" step="0.01" placeholder="1299.90" required></div>
{campo_condicao()}
<div class="campo-completo"><button class="botao principal" type="submit">Cadastrar bicicleta</button>
<a class="botao secundario" href="/bicicletas">Consultar estoque</a></div>
</form></section>"""
    return pagina(conteudo, "Painel", request.query.get("msg", ""))


def validar_dados():
    cor = request.forms.get("cor", "").strip()
    modelo = request.forms.get("modelo", "").strip()
    ano = int(request.forms.get("ano", ""))
    valor = float(request.forms.get("valor", "").replace(",", "."))
    condicao = request.forms.get("condicao", "Nova")
    if (not cor or not modelo or len(cor) > 60 or len(modelo) > 100
            or any(x in cor + modelo for x in (";", "\n", "\r"))
            or ano < 1885 or ano > datetime.now().year + 1
            or valor <= 0 or condicao not in CONDICOES):
        raise ValueError("Dados inválidos")
    return cor, modelo, ano, valor, condicao


@app.post("/adicionar")
def adicionar():
    try:
        cor, modelo, ano, valor, condicao = validar_dados()
    except (ValueError, TypeError):
        return redirect("/?msg=" + quote("Dados inválidos. Confira os campos."))
    bicicletas.append(Bicicleta(cor, modelo, ano, valor, condicao=condicao))
    Bicicleta.quantidade_de_bicicletas = len(bicicletas)
    salvar_bicicletas()
    return redirect("/?msg=" + quote("Bicicleta cadastrada com sucesso!"))


def montar_tabela(lista):
    if not lista:
        return '<p class="vazio">Nenhuma bicicleta encontrada.</p>'
    linhas = ""
    for indice, b in lista:
        status = ('<span class="status vendida">Vendida</span>' if b.vendida
                  else '<span class="status disponivel">Disponível</span>')
        acoes = f'<a class="botao secundario" href="/detalhes/{indice}">Detalhes</a>'
        acoes += f'<a class="botao secundario" href="/editar/{indice}">Editar</a>'
        acoes += f"""<form action="/excluir/{indice}" method="post"
onsubmit="return confirm('Deseja excluir esta bicicleta?')">
<button class="botao secundario" type="submit">Excluir</button></form>"""
        if not b.vendida:
            acoes += f"""<form action="/vender/{indice}" method="post"
onsubmit="return confirm('Confirmar a venda?')">
<button class="botao principal" type="submit">Vender</button></form>"""
        linhas += f"""<tr><td>{indice + 1}</td><td>{escape(b.modelo)}</td>
<td>{escape(b.cor)}</td><td>{b.ano}</td><td>R$ {b.valor:.2f}</td>
<td>{escape(b.condicao)}</td><td>{status}</td><td><div class="acoes">{acoes}</div></td></tr>"""
    return f"""<div class="tabela-wrap"><table><thead><tr>
<th>#</th><th>Modelo</th><th>Cor</th><th>Ano</th><th>Valor</th>
<th>Condição</th><th>Status</th><th>Ações</th></tr></thead>
<tbody>{linhas}</tbody></table></div>"""


def pagina_lista(lista, titulo):
    conteudo = f"""<section class="hero"><p class="etiqueta">GERENCIAMENTO</p>
<h1>{escape(titulo)}</h1><p>Consulte os registros armazenados no arquivo de texto.</p></section>
<section class="painel"><h2>{len(lista)} bicicleta(s)</h2>{montar_tabela(lista)}
<br><a class="botao secundario" href="/">Voltar ao painel</a></section>"""
    return pagina(conteudo, titulo, request.query.get("msg", ""))


@app.get("/bicicletas")
def listar_bicicletas():
    return pagina_lista(list(enumerate(bicicletas)), "Estoque de bicicletas")


@app.get("/vendidas")
def listar_vendidas():
    return pagina_lista([(i, b) for i, b in enumerate(bicicletas) if b.vendida],
                        "Bicicletas vendidas")


@app.post("/vender/<indice:int>")
def vender(indice):
    if indice < 0 or indice >= len(bicicletas):
        return redirect("/bicicletas?msg=" + quote("Bicicleta não encontrada"))
    if not bicicletas[indice].vender():
        return redirect("/bicicletas?msg=" + quote("Bicicleta já vendida"))
    salvar_bicicletas()
    return redirect("/vendidas?msg=" + quote("Venda registrada com sucesso!"))


@app.get("/detalhes/<indice:int>")
def detalhes(indice):
    if indice < 0 or indice >= len(bicicletas):
        return redirect("/bicicletas")
    b = bicicletas[indice]
    status = "Vendida" if b.vendida else "Disponível"
    conteudo = f"""
<section class="hero"><p class="etiqueta">DETALHES DO PRODUTO</p>
<h1>{escape(b.modelo)}</h1><p>Confira os dados e experimente a bicicleta.</p></section>
<section class="painel detalhes">
<p><strong>Cor:</strong> {escape(b.cor)}</p><p><strong>Modelo:</strong> {escape(b.modelo)}</p>
<p><strong>Ano:</strong> {b.ano}</p><p><strong>Valor:</strong> R$ {b.valor:.2f}</p>
<p><strong>Condição:</strong> {escape(b.estado())}</p><p><strong>Status:</strong> {status}</p>
<h2>Experimentar bicicleta</h2><p>Simule os testes antes da compra.</p>
<div class="acoes">
<form action="/testar-buzina/{indice}" method="post"><button class="botao principal" type="submit">🔔 Testar buzina</button></form>
<form action="/testar-pedalada/{indice}" method="post"><button class="botao secundario" type="submit">🚲 Testar pedalada</button></form></div>
<p><strong>Som da buzina:</strong> {escape(b.buzinar())}</p>
<a class="botao secundario" href="/editar/{indice}">Editar bicicleta</a>
<a class="botao secundario" href="/bicicletas">Voltar ao estoque</a></section>"""
    return pagina(conteudo, "Detalhes", request.query.get("msg", ""))


@app.post("/testar-buzina/<indice:int>")
def testar_buzina(indice):
    if indice < 0 or indice >= len(bicicletas):
        return redirect("/bicicletas")
    mensagem = f"Teste de buzina realizado: {bicicletas[indice].buzinar()}"
    return redirect(f"/detalhes/{indice}?msg={quote(mensagem)}")


@app.post("/testar-pedalada/<indice:int>")
def testar_pedalada(indice):
    if indice < 0 or indice >= len(bicicletas):
        return redirect("/bicicletas")
    mensagem = bicicletas[indice].pedalar()
    return redirect(f"/detalhes/{indice}?msg={quote(mensagem)}")


@app.get("/editar/<indice:int>")
def editar_pagina(indice):
    if indice < 0 or indice >= len(bicicletas):
        return redirect("/bicicletas")
    b = bicicletas[indice]
    conteudo = f"""
<section class="painel"><h1>Editar bicicleta</h1>
<form action="/editar/{indice}" method="post" class="form-grid">
<div><label for="cor">Cor</label><input id="cor" name="cor" value="{escape(b.cor, quote=True)}" maxlength="60" required></div>
<div><label for="modelo">Modelo</label><input id="modelo" name="modelo" value="{escape(b.modelo, quote=True)}" maxlength="100" required></div>
<div><label for="ano">Ano</label><input id="ano" name="ano" type="number" min="1885" max="{datetime.now().year + 1}" value="{b.ano}" required></div>
<div><label for="valor">Valor (R$)</label><input id="valor" name="valor" type="number" min="0.01" step="0.01" value="{b.valor:.2f}" required></div>
{campo_condicao(b.condicao)}
<div class="campo-completo"><button class="botao principal" type="submit">Salvar alterações</button>
<a class="botao secundario" href="/bicicletas">Cancelar</a></div>
</form></section>"""
    return pagina(conteudo, "Editar bicicleta", request.query.get("msg", ""))


@app.post("/editar/<indice:int>")
def editar(indice):
    if indice < 0 or indice >= len(bicicletas):
        return redirect("/bicicletas")
    try:
        cor, modelo, ano, valor, condicao = validar_dados()
    except (ValueError, TypeError):
        return redirect(f"/editar/{indice}?msg={quote('Dados inválidos. Confira os campos.')}")
    b = bicicletas[indice]
    b.cor, b.modelo, b.ano, b.valor, b.condicao = cor, modelo, ano, valor, condicao
    salvar_bicicletas()
    return redirect("/bicicletas?msg=" + quote("Bicicleta atualizada com sucesso!"))


@app.post("/excluir/<indice:int>")
def excluir(indice):
    if indice < 0 or indice >= len(bicicletas):
        return redirect("/bicicletas?msg=" + quote("Bicicleta não encontrada"))
    del bicicletas[indice]
    Bicicleta.quantidade_de_bicicletas = len(bicicletas)
    salvar_bicicletas()
    return redirect("/bicicletas?msg=" + quote("Bicicleta excluída com sucesso!"))


if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8080, debug=True, reloader=True)
