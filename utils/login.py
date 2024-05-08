import sqlite3

class Login:
    def __init__(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT NOT NULL, senha TEXT NOT NULL)")
        conn.commit()
        

    def validar_login(self, usuario, senha):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        consulta = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
        cursor.execute(consulta, (usuario, senha))
        resultado = cursor.fetchone()

        if resultado:
            print("Login válido")
            return True
        else:
            print("Usuário ou senha incorretos")
            return False

    def verificar_Tipo_Usuario(self, usuario, senha):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        consulta_Tipo_Usuario = "SELECT tipo_usuario FROM usuarios WHERE usuario = ? AND senha = ?"
        cursor.execute(consulta_Tipo_Usuario, (usuario, senha))
        resultado = cursor.fetchone()

        if resultado[0] == 'admin':
            var = 'admin'
        elif resultado[0] == 'user':
            var = 'user'

        return var
        
        
        
        

        


