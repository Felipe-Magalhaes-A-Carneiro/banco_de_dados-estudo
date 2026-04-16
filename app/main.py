import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'meu_banco_de_dados.db')
cur = con.cursor()

# Agora é necessário comentar o código abaixo para que o Python não tente criar a tabela novamente:
# cur.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(200), email VARCHAR(150))")

# INSERINDO dados na tabela criada:
data = ("Felipe", "felipe.araujo@mail.com")
cur.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', (data))

# Envia as alterações para o banco de dados:
con.commit()