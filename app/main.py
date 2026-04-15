import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'meu_banco_de_dados.db')
cur = con.cursor()

cur.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(200), email VARCHAR(150))")