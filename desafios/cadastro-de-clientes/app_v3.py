import sqlite3

from bottle import get, post, redirect, request, route, run, template

DB_NAME = 'clientes.db'
 
def inicializar_banco():
    """Garante a existência da tabela 'clientes' no banco SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()
 
# 1. ROTA PRINCIPAL: Listagem de Clientes e Formulário de Cadastro

@route('/', method=['GET','POST'])
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()
 
    return template('form_clientes_v3', lista_clientes=clientes)
 
# 2. ROTA DE CADASTRO (Novo Cliente)
@route('/cadastrar', method=['GET','POST'])
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
 
# 3. ROTA DE EDIÇÃO - EXIBIR FORMULÁRIO (GET)
@get('/editar/<id:int>')
def exibir_formulario_edicao(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()
 
    if not cliente:
        #print(f'O id informado não existe: {id}')
        redirect('/')
 
    return template('form_editar', cliente=cliente)
 
# 4. ROTA DE EDIÇÃO - SALVAR ALTERAÇÕES (POST)
@post('/editar/<id:int>')
def salvar_edicao(id):
    nome = request.forms.get('nome')
    email = request.forms.get('email')
    telefone = request.forms.get('telefone')
 
    if nome and email:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Atualiza os dados com a instrução SQL UPDATE usando parâmetros seguros
        cursor.execute(
            "UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?;",
            (nome, email, telefone, id)
        )
        conn.commit()
        conn.close()
 
    redirect('/')
 
# 5. ROTA DE EXCLUSÃO
@route('/deletar/<id:int>', method=['GET','POST'])
def deletar(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
    conn.commit()
    conn.close()
    
    redirect('/')
 
if __name__ == '__main__':
    inicializar_banco()
    print("Servidor rodando em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)