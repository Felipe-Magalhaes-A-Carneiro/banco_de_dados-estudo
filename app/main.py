import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'meu_banco_de_dados.db')
cur = con.cursor()

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

# criamos a função de deletar
def deletar_dados(con, cur, id):
    data = (id, )
    cur.execute('DELETE FROM clientes WHERE id = ?;', data)
    con.commit()

# inserir_dados(con, cur, "Ana", "ana.silvana@mail.com")

# atualizar_dados(con, cur, "Felipe Magalhães", "felipe.araujo@mail.com", 1)

deletar_dados(con, cur, 2)