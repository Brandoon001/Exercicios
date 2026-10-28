import sqlite3

from bottle import get, post, redirect, request, route, run, template

DB_NAME = 'clientes.db'
 
def inicializar_banco():
    """Garante que a tabela 'clientes' esteja criada no banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()
 
# 1. ROTA PRINCIPAL: Lista os clientes e exibe o formulário de cadastro
@get('/')
@route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()
 
    return template('form_clientes', lista_clientes=clientes)
 
# 2. ROTA DE CADASTRO: Recebe os dados do formulário via POST
@post('/cadastrar')
@route('/cadastrar')
def cadastrar():
    nome = request.forms.get('nome')
    email = request.forms.get('email')
    telefone = request.forms.get('telefone')
 
    if nome and email:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?);", (nome, email, telefone))
        conn.commit()
        conn.close()
 
    redirect('/')
 
# 3. ROTA DE EXCLUSÃO: Remove o registro do banco pelo ID
@get('/deletar/<id:int>')
@route('/deletar/<id:int>')
def deletar(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
    conn.commit()
    conn.close()
    
    redirect('/')
 
if __name__ == '__main__':
    # Inicializa a estrutura da tabela
    inicializar_banco()
    
    print("Iniciando o servidor Bottle em http://localhost:8080 ...")
    # Inicia o servidor HTTP embutido
    run(host='localhost', port=8080, debug=True, reloader=True)