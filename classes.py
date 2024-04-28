import sqlite3

class Livros:
    def __init__(self, nome, autor, ano_publi):
        self.nome = nome
        self.autor = autor
        self.ano_publi = ano_publi

        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, autor TEXT NOT NULL, ano_publi INT CHECK (ano_publi BETWEEN 1000 AND 9999))")
        
        conn.commit()

        cursor.close()
        conn.close()

    def adicionarLivro(self):
        podeAdd = True
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute("SELECT nome FROM livros")
        resultados = cursor.fetchall()

        nomes = []  
        for nome in resultados:
            nomes.append(nome[0])  

        if self.nome in nomes:
            print(f"O livro com o nome {self.nome} ja foi cadastrado")
            podeAdd = False
            
        else:
            cursor.execute("INSERT INTO livros (nome, autor, ano_publi) VALUES (?, ?, ?)", (self.nome, self.autor, self.ano_publi))
            conn.commit()
            print("livro cadastrado")
            podeAdd = True

        cursor.close()
        conn.close()

        return podeAdd
        
    def consultarLivros(self):
        pass
            