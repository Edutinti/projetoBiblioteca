# Sistema de Gerenciamento de Biblioteca:
# Desenvolva um sistema onde você possa adicionar livros, buscar livros pelo título ou autor, deletar livro do banco de dados como login ADM
# Use classes para representar livros, membros e a biblioteca em si.

import classes
import PySimpleGUI as sg

# Layout da interface gráfica
layout = [
    [sg.Text('Nome do Livro:'), sg.InputText(key='nome')],
    [sg.Text('Autor do Livro:'), sg.InputText(key='autor')],
    [sg.Text('Ano de Publicação:'), sg.InputText(key='ano_publi')],
    [sg.Button('Adicionar Livro')],
    [sg.Button('Procurar livro')]
]

# Criando a janela da aplicação
window = sg.Window('Adicionar Livro', layout)


window2aberta = False
# Loop para eventos da janela
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Adicionar Livro':
        nome = values['nome']
        autor = values['autor']
        ano_publi = values['ano_publi']
        int(ano_publi)
        livro = classes.Livros(nome,autor,int(ano_publi))
        addlivro = classes.Livros.adicionarLivro(livro)

        if addlivro:
            sg.popup('Livro adicionado com sucesso!')
            window['nome'].update('')
            window['autor'].update('')
            window['ano_publi'].update('')
        else:
            sg.popup('Esse livro ja foi cadastrado!')
    
    if event == 'Procurar livro':
        window.hide()

        layout_secundario = [
            [sg.Text('Nome do Livro:'), sg.InputText(key='nomeLivro')],
            [sg.Text('Autor do Livro:'), sg.InputText(key='autorLivro')],
            [sg.Multiline(size=(60, 5), key='output', disabled=True)],
            [sg.Button('Procurar')],
            [sg.Button('Voltar')]
        ]

        window2 = sg.Window('Procurar Livros', layout_secundario)

        while True:
            event1, values1 = window2.read()

            if event1 == 'Procurar':
                nome1 = values1['nomeLivro']
                autor1 = values1['autorLivro']
                procurarLivro = classes.Livros.consultarLivros(nome1,autor1)    
                window2['output'].update(procurarLivro)
            elif event1 == sg.WINDOW_CLOSED or event1 == 'Voltar':
                window.un_hide()
                window2.close()
                break

window.close()





