def atualizar_dados(con, cur, nome, email, id):
    data = (nome, email, id)
    cur.execute('UPDATE clientes SET nome= ?, email= ? WHERE id = ?;', data)
    con.commit()