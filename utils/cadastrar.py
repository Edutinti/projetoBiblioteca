import sqlite3

class Cadastro:
    def __init__(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT NOT NULL, senha TEXT NOT NULL, tipo_usuario TEXT NOT NULL)")
        conn.commit()
     

    def cadastroPessoa(self, usuario, senha, tipo_usuario='user'):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, senha, tipo_usuario) VALUES (?, ?, ?)", (usuario, senha, tipo_usuario))
        conn.commit()
        conn.close()