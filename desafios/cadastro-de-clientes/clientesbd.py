import sqlite3


def criar_coxexao():
    # 1. Abre a conexão com o arquivo do banco de dados (ou cria se não existir)
    conn = sqlite3.connect('clientes.db')
    
    # 2. Cria o objeto cursor para enviar comandos SQL
    cursor = conn.cursor()
    #print("Conexão estabelecida com sucesso!")
    return cursor, conn


def criar_bd():
    """Criar um banco de dados local, construir uma tabela de clientes"""
    cursor, conn = criar_coxexao()
    
    # Executa a criação da tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT
        );
    ''')
    
    # Confirma a alteração estrutural no banco
    conn.commit()
    #print("Tabela 'clientes' pronta para uso!")

def inserir_clientes():
    # Lista de tuplas com os dados de exemplo
    novos_clientes = [
        ("Pedro", "pedro@example.com", "11 99999-0001"),
        ("Fernando", "fernando@example.com", "11 99999-0002"),
        ("Alana", "alana@example.com", "11 99999-0003")
    ]
 
    # Inserção em lote usando placeholders (?)
    cursor, conn = criar_coxexao()
    cursor.executemany(
        "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?);",
        novos_clientes
    )
 
    # Salva permanentemente a inserção no arquivo do banco
    conn.commit()
    print(f"{cursor.rowcount} registros inseridos com sucesso!")

#criar_bd()
inserir_clientes()