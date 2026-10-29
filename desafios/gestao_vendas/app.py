import sqlite3
import pandas as pd

# Abre (ou cria) o banco de dados local
conn = sqlite3.connect("gestao_produtos.db")
cursor = conn.cursor()
print("Conexão estabelecida com sucesso!")

# Criação opcional das tabelas base (Categoria e Produto) caso não existam
cursor.execute('''
CREATE TABLE IF NOT EXISTS Categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL,
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);
''')
conn.commit()

def tabela_vendas(conexao):
    conexao.execute("PRAGMA foreign_keys = ON;")
    cursor_vendas = conexao.cursor()
    cursor_vendas.execute('''
    CREATE TABLE IF NOT EXISTS Vendas (
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL CHECK(quantidade > 0),
        data_venda TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
        FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
    );
    ''')
    conexao.commit()
    print("Tabela 'Vendas' criada com sucesso!")

tabela_vendas(conn)

def registrar_venda(conexao, id_produto, quantidade):
    """Baixa o estoque e registra a venda na mesma transação."""
    with conexao:  # commit se der certo, rollback se der erro
        conexao.execute(
            "UPDATE Produto SET estoque = estoque - ? WHERE id_produto = ?;",
            (quantidade, id_produto),
        )
        conexao.execute(
            "INSERT INTO Vendas (id_produto, quantidade) VALUES (?, ?);",
            (id_produto, quantidade),
        )

novas_vendas = [(1, 3), (2, 2), (1, 4), (3, 1), (4, 5), (5, 10)]

for id_produto, quantidade in novas_vendas:
    try:
        registrar_venda(conn, id_produto, quantidade)
    except sqlite3.IntegrityError as erro:
        print(f"Venda recusada ({id_produto}, {quantidade}): {erro}")

# Corrigido: O print agora está fora do loop
print("Processamento de vendas concluído.")

def exibir_ranking_vendas(conexao):
    query_ranking = """
    SELECT
        p.nome AS Produto,
        c.nome_categoria AS Categoria,
        p.preco AS Preco_Unitario,
        SUM(v.quantidade) AS Qtd_Vendida,
        SUM(v.quantidade * p.preco) AS Faturamento_Total,
        p.estoque AS Estoque_Restante
    FROM Produto p
    LEFT JOIN Vendas v ON p.id_produto = v.id_produto
    LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
    GROUP BY p.id_produto, p.nome, c.nome_categoria
    ORDER BY Qtd_Vendida DESC;
    """
    
    df_vendas = pd.read_sql_query(query_ranking, conexao)
    
    # Produtos sem nenhuma venda aparecem com NULL; troque por zero
    df_vendas["Qtd_Vendida"] = df_vendas["Qtd_Vendida"].fillna(0).astype(int)
    df_vendas["Faturamento_Total"] = df_vendas["Faturamento_Total"].fillna(0.0)
    
    print("\n--- RANKING DE VENDAS POR PRODUTO ---")
    print(df_vendas.to_string(index=False))

# Exibe o ranking consolidado
exibir_ranking_vendas(conn)

# Encerramento seguro da conexão ao final do script
cursor.close()
conn.close()
print("Conexão encerrada com segurança.")