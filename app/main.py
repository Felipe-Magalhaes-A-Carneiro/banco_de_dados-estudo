import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'meu_banco_de_dados.db')
cur = con.cursor()
cur.row_factory = sqlite3.Row

def criar_tabela(cur):
    cur.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(200), email VARCHAR(150))")
    con.commit()
    

def inserir_dados(con, cur, nome, email):
    data = (nome, email)
    cur.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', (data))
    con.commit()


def atualizar_dados(con, cur, nome, email, id):
    data = (nome, email, id)
    cur.execute('UPDATE clientes SET nome= ?, email= ? WHERE id = ?;', data)
    con.commit()


def deletar_dados(con, cur, id):
    data = (id, )
    cur.execute('DELETE FROM clientes WHERE id = ?;', data)
    con.commit()


def inserir_muitos_dados(con, cur, dados):
    cur.executemany('INSERT INTO clientes (nome, email) VALUES (?,?);', dados)
    con.commit()

# criamos a função para retornar APENAS UM cliente:
def consultar_cliente(cur, id):
    cur.execute('SELECT * FROM clientes WHERE id= ?', (id, ))

    return cur.fetchone()

# criamos a função para retornar TODOS os clientes:
def consultar_todos_clientes(cur):
    cur.execute('SELECT * FROM clientes')
    results = cur.fetchall()

    for row in results:
        print(row)

def listar_por_ordem_todos_clientes(cur):
    cur.execute('SELECT * FROM clientes ORDER BY nome;')
    results = cur.fetchall()

    for row in results:
        print(row)


# inserir_dados(con, cur, "Ana", "ana.silvana@mail.com")

# atualizar_dados(con, cur, "Felipe Magalhães", "felipe.araujo@mail.com", 1)

# deletar_dados(con, cur, 2)

#dados = [("Maria", "maria.belem@mail.com"),("José", "jose.belem@mail.com"),("Guilherme", "guilherme.bd@mail.com"),("Ana", "ana.silvana@mail.com"),]

#inserir_muitos_dados(con, cur, dados)


# Consultando APENAS UM cliente
cliente = consultar_cliente(cur, 1)
print(dict(cliente)) # fazermos com que o 'cliente' se torne um dicionario

# Retornemos uma mensagem customizada com o uso do Row
print(f"Seja bem-vindo(a) ao sistema, {cliente[1]}") 


# clientes = consultar_todos_clientes(cur)
# print(clientes)


# clientes_por_nome = listar_por_ordem_todos_clientes(cur)
# print(clientes_por_nome)