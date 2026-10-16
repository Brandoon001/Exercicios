from bicicletario import Bicicleta
from bottle import get, post, request, route, run, template


@route('/')
@get('/')
def index():
    return template('menu_bicicletas')


@route('/cadastro')
def cadastro_de_bicicleta():
    return template('form_bicicletas')


def carregar_bicicletas():
    """Lê o arquivo txt"""
    bicicletas = []
    with open('bicicletas.txt', 'r', encoding='utf-8') as file:
        for linha in file:
                    partes = linha.strip().split('|')
                    valor_float = float(partes[3])
                    bicicletas.append(Bicicleta(partes[0],partes[1],partes[2],valor_float))
    return bicicletas

def salvar_bicicleta(bicicletas):
    with open('bicicletas.txt', 'w', encoding='utf-8') as file:
        for bicicleta in bicicletas:
            linha = f'{bicicleta.cor}|{bicicleta.modelo}|{bicicleta.ano}|{bicicleta.valor}\n'
            file.write(linha)

@post('/process')
def index_process():    
    bicicletas = carregar_bicicletas()

    cor = request.forms.get('cor')
    modelo = request.forms.get('modelo')
    ano = request.forms.get('ano')
    valor = request.forms.get('valor')
    bicicletas.append(Bicicleta(cor, modelo, ano, valor))
    
    # Salvar em um arquivo txt, ou em um banco de dados sqlite
    salvar_bicicleta(bicicletas)
    message = f'A bicicleta {modelo} {cor}, de {ano} com valor {valor} foi adicionada!'

    return message

@route('/mostrar')
def mostrar_bicicletas():
    bicicletas = carregar_bicicletas()

    return template('mostrar_bicicletas', bicicletas=bicicletas)


run(host='localhost', port=8080)