import sqlite3

# Conectar ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# Criar a tabela clientes (se não existir)
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
"""
)

# Inserir alguns dados
cursor.executemany(
    """
INSERT INTO clientes (nome, idade) VALUES (?, ?)
""",
    [("João", 30), ("Maria", 25), ("José", 40)],
)

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()
