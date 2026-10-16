import sqlite3
 
# 1. Abre a conexão com o arquivo do banco de dados (ou cria se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')
 
# 2. Cria o objeto cursor para enviar comandos SQL
cursor = conn.cursor()
 
print("Conexão estabelecida com sucesso!")


# Executa a criação da tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
    );
''')


 
# Salva permanentemente a inserção no arquivo do banco
conn.commit()
print(f"{cursor.rowcount} registros inseridos com sucesso!")
 
# Confirma a alteração estrutural no banco
conn.commit()
print("Tabela 'clientes' pronta para uso!")

# Lista de tuplas com os dados de exemplo
novos_clientes = [
    ("Ana Silva", "ana.silva@example.com", "11 99999-0001"),
    ("Bruno Souza", "bruno.souza@example.com", "11 99999-0002"),
    ("Carla Pereira", "carla.pereira@example.com", "11 99999-0003")
]
 
# Inserção em lote usando placeholders (?)
cursor.executemany(
    "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?);",
    novos_clientes
)

# Executa a consulta
cursor.execute("SELECT id, nome, email, telefone FROM clientes;")
 
# Recupera todas as linhas encontradas
resultados = cursor.fetchall()
 
print("\n--- Lista de Clientes ---")
for id_, nome, email, telefone in resultados:
    print(f"ID: {id_} | Nome: {nome} | E-mail: {email} | Telefone: {telefone}")