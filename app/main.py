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

