# Sistema de Gerenciamento de Biblioteca:
# Desenvolva um sistema onde você possa adicionar livros, buscar livros pelo título ou autor, emprestar e devolver livros. 
# Use classes para representar livros, membros e a biblioteca em si.

import classes
import PySimpleGUI as sg

# Layout da interface gráfica
layout = [
    [sg.Text('Nome do Livro:'), sg.InputText(key='nome')],
    [sg.Text('Autor do Livro:'), sg.InputText(key='autor')],
    [sg.Text('Ano de Publicação:'), sg.InputText(key='ano_publi')], #botar pra int
    [sg.Button('Adicionar Livro')]
]

# Criando a janela da aplicação
window = sg.Window('Adicionar Livro', layout)

# Loop para eventos da janela
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Adicionar Livro':
        nome = values['nome']
        autor = values['autor']
        ano_publi = values['ano_publi']

        addlivro = classes.Livros.adicionarLivro(classes.Livros(nome,autor,int(ano_publi)))

        if addlivro:
            sg.popup('Livro adicionado com sucesso!')
            window['nome'].update('')
            window['autor'].update('')
            window['ano_publi'].update('')
        else:
            sg.popup('Esse livro ja foi cadastrado!')


window.close()





