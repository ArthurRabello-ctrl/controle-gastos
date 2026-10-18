import sqlite3


def criar_tabelas():
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            tipo TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lancamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias (id)
        )
    """)

    conexao.commit()
    conexao.close()

def inserir_categoria(nome, tipo):
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO categorias (nome, tipo) VALUES (?, ?)",
        (nome, tipo),
    )

    conexao.commit()
    conexao.close()


def buscar_id_categoria(nome):
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM categorias WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()

    conexao.close()

    if resultado is None:
        return None
    return resultado[0]


def inserir_lancamento(data, descricao, valor, nome_categoria):
    categoria_id = buscar_id_categoria(nome_categoria)

    if categoria_id is None:
        return False

    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO lancamentos (data, descricao, valor, categoria_id) VALUES (?, ?, ?, ?)",
        (data, descricao, valor, categoria_id),
    )

    conexao.commit()
    conexao.close()
    return True

def listar_lancamentos():
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT l.id, l.data, l.descricao, l.valor, c.nome, c.tipo
        FROM lancamentos AS l
        JOIN categorias AS c ON l.categoria_id = c.id
        ORDER BY l.data DESC
    """)
    linhas = cursor.fetchall()

    conexao.close()
    return linhas


def listar_por_tipo(tipo):
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT l.id, l.data, l.descricao, l.valor, c.nome, c.tipo
        FROM lancamentos AS l
        JOIN categorias AS c ON l.categoria_id = c.id
        WHERE c.tipo = ?
        ORDER BY l.data DESC
    """, (tipo,))
    linhas = cursor.fetchall()

    conexao.close()
    return linhas

def total_por_categoria(tipo, mes):
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT c.nome, SUM(l.valor) AS total, COUNT(*) AS quantidade
        FROM lancamentos AS l
        JOIN categorias AS c ON l.categoria_id = c.id
        WHERE c.tipo = ? AND strftime('%Y-%m', l.data) = ?
        GROUP BY c.nome
        ORDER BY total DESC
    """, (tipo, mes))
    linhas = cursor.fetchall()

    conexao.close()
    return linhas


def total_por_tipo(tipo, mes):
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(l.valor), 0)
        FROM lancamentos AS l
        JOIN categorias AS c ON l.categoria_id = c.id
        WHERE c.tipo = ? AND strftime('%Y-%m', l.data) = ?
    """, (tipo, mes))
    total = cursor.fetchone()[0]

    conexao.close()
    return total

def listar_categorias():
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT nome, tipo FROM categorias ORDER BY tipo, nome")
    linhas = cursor.fetchall()

    conexao.close()
    return linhas