import sqlite3
import pandas as pd

# Abre (ou cria) o banco de dados local
conn = sqlite3.connect("gestao_produtos.db")
cursor = conn.cursor()
print("Conexão estabelecida com sucesso!")

def criar_tabelas():
    # O SQLite só verifica chaves estrangeiras se você pedir, a cada conexão
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.executescript('''
    DROP TABLE IF EXISTS Vendas;
    DROP TABLE IF EXISTS Produto;
    DROP TABLE IF EXISTS Categoria;
    
    CREATE TABLE Categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_categoria TEXT NOT NULL
    );
    
    CREATE TABLE Produto (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL CHECK(preco >= 0.0),
        estoque INTEGER NOT NULL CHECK(estoque >= 0),
        id_categoria INTEGER,
        FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
    );
    ''')
    
    conn.commit()
    print("Tabelas 'Categoria' e 'Produto' criadas com sucesso!")

# Cria as tabelas (descomente se for a primeira execução)
criar_tabelas()

def inserir_registros():
    categorias_iniciais = [
        ("Eletrônicos",),
        ("Móveis",),
        ("Vestuário",),
    ]
    
    produtos_iniciais = [
        ("Smartphone", 1500.00, 10, 1),
        ("Notebook", 3500.00, 5, 1),
        ("Sofá", 800.00, 3, 2),
        ("Cadeira de Escritório", 350.00, 12, 2),
        ("Camisa Polo", 80.00, 25, 3),
        ("Calça Jeans", 120.00, 15, 3),
    ]
    
    cursor.executemany(
        "INSERT INTO Categoria (nome_categoria) VALUES (?);", categorias_iniciais
    )
    cursor.executemany(
        "INSERT INTO Produto (nome, preco, estoque, id_categoria) VALUES (?, ?, ?, ?);",
        produtos_iniciais,
    )
    
    conn.commit()
    print(f"{len(categorias_iniciais)} categorias e {len(produtos_iniciais)} produtos inseridos.")

# Insere os dados iniciais
inserir_registros()

def listar_produtos():
    cursor.execute("SELECT id_produto, nome, preco, estoque FROM Produto;")
    linhas = cursor.fetchall()
   
    print("\n--- Lista de Produtos Cadastrados ---")
    for id_p, nome, preco, estoque in linhas:
        print(f"ID: {id_p} | Produto: {nome} | Preço: R$ {preco:.2f} | Estoque: {estoque}")

listar_produtos()

def atualizar_produto(preco, nome):
    cursor.execute(
        "UPDATE Produto SET preco = ? WHERE nome = ?;", (preco, nome)
    )
    print("Linhas atualizadas:", cursor.rowcount)
    conn.commit()

def deletar_produto(nome):
    cursor.execute("DELETE FROM Produto WHERE nome = ?;", (nome,))
    print("Linhas excluídas:", cursor.rowcount)
    conn.commit()

# Exemplos de uso opcionais:
# atualizar_produto(1600, "Smartphone")
# deletar_produto("Calça Jeans")

def estoque_categoria_sql():
    query_estoque_categoria = """
    SELECT
        c.nome_categoria,
        COUNT(p.id_produto) AS total_produtos,
        SUM(p.preco * p.estoque) AS valor_total_estoque
    FROM Categoria c
    JOIN Produto p ON c.id_categoria = p.id_categoria
    GROUP BY c.nome_categoria
    ORDER BY valor_total_estoque DESC;
    """
    
    cursor.execute(query_estoque_categoria)
    print("\n--- Valor Total de Estoque por Categoria ---")
    for categoria, qtd, valor in cursor.fetchall():
        print(f"Categoria: {categoria} | Variedade: {qtd} item(ns) | Valor em Estoque: R$ {valor:.2f}")

estoque_categoria_sql()

def listar_produtos_pelo_valor(valor):
    """Liste os produtos com estoque menor que valor, do menor para o maior estoque."""
    cursor.execute("SELECT nome, estoque FROM Produto WHERE estoque < ? ORDER BY estoque;", (valor,))
    print(f'\nProdutos com estoque menor que {valor}:')
    print(cursor.fetchall())

listar_produtos_pelo_valor(10)

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

# Processamento das novas vendas (fora da função registrar_venda)
novas_vendas = [(1, 3), (2, 2), (1, 4), (3, 1), (4, 5), (5, 10)]

for id_prod, qtd in novas_vendas:
    try:
        registrar_venda(conn, id_prod, qtd)
    except sqlite3.IntegrityError as erro:
        print(f"Venda recusada ({id_prod}, {qtd}): {erro}")

print("Processamento de vendas concluído.")

def exibir_ranking_vendas_SQL(conexao):
    query_campeao = """
        SELECT
            p.id_produto,
            p.nome AS produto,
            c.nome_categoria AS categoria,
            SUM(v.quantidade) AS total_unidades_vendidas,
            SUM(v.quantidade * p.preco) AS faturamento_total
        FROM Vendas v
        INNER JOIN Produto p ON v.id_produto = p.id_produto
        INNER JOIN Categoria c ON p.id_categoria = c.id_categoria
        GROUP BY p.id_produto, p.nome, c.nome_categoria
        ORDER BY total_unidades_vendidas DESC
        LIMIT 1;
        """
 
    cur = conexao.cursor()
    cur.execute(query_campeao)
    resultado = cur.fetchone()
    
    if resultado:
        id_p, nome, categoria, total_qtd, faturamento = resultado
        print("\n--- PRODUTO MAIS VENDIDO ---")
        print(f"Produto: {nome} (ID: {id_p})")
        print(f"Categoria: {categoria}")
        print(f"Unidades vendidas: {total_qtd}")
        print(f"Faturamento gerado: R$ {faturamento:.2f}")

# Exibe o produto mais vendido passando a conexão
exibir_ranking_vendas_SQL(conn)

def exibir_ranking_vendas_pandas(conexao):
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

exibir_ranking_vendas_pandas(conn)

# Encerramento seguro da conexão ao final do script
cursor.close()
conn.close()
print("\nConexão encerrada com segurança.")