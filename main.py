# Sistema de Gerenciamento de Biblioteca:
# Desenvolva um sistema onde você possa adicionar livros, buscar livros pelo título ou autor, deletar livro pelo nome do banco de dados (como login ADM)
# Use classes para representar livros, membros.

from utils import livros
from utils import login
from utils import cadastrar
import PySimpleGUI as sg


# *****LOGIN*****
layot = [
    [sg.Text('Login'), sg.Input(key='login')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Button('Entrar')],
    [sg.Button('Cadastrar')]
]

janela_login = sg.Window('Login', layot)

cadastro_aberto = False

while True:
    event, values = janela_login.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    elif event == 'Entrar':
        usuario = values['login']
        senha = values['senha']
        loginStr = str(usuario)
        senhaStr = str(senha)

        entrar = login.Login()
        retornoFuncao = entrar.validar_login(loginStr, senhaStr)
        janela_login['login'].update('')
        janela_login['senha'].update('')
# *****LOGIN*****


# *****JANELA PRINCIPAL, PROCURAR LIVRO*****
        if retornoFuncao:
            verificar_Tipo_Usuario = entrar.verificar_Tipo_Usuario(loginStr, senhaStr)
            janela_login.close()

            layoutProcLivro = []

            if verificar_Tipo_Usuario == 'admin':

                layoutProcLivro = [
                    [sg.Text('Nome do Livro:'), sg.InputText(key='nomeLivro')],
                    [sg.Text('Autor:'), sg.InputText(key='autor')],
                    [sg.Multiline(size=(60, 5), key='output', disabled=True)],
                    [sg.Button('Procurar')],
                    [sg.Button('Cadastrar Livro'),sg.Button('Deletar Livro')],
                ]

            elif verificar_Tipo_Usuario == 'user':
                layoutProcLivro = [
                    [sg.Text('Nome do Livro:'), sg.InputText(key='nomeLivro')],
                    [sg.Text('Autor:'), sg.InputText(key='autor')],
                    [sg.Multiline(size=(60, 5), key='output', disabled=True)],
                    [sg.Button('Procurar')],
                ]

            
            janela_Procurar_Livro = sg.Window('Procurar Livro', layoutProcLivro)

            while True:
                eventProc, valuesProc = janela_Procurar_Livro.read()    

                if eventProc == sg.WINDOW_CLOSED:
                    break
   
                elif eventProc == 'Procurar':
                    nome1 = valuesProc['nomeLivro']
                    autor1 = valuesProc['autor']
                    procurarLivro = livros.Livros.consultarLivros(nome1,autor1)    
                    janela_Procurar_Livro['output'].update(procurarLivro)
                
                elif eventProc == 'Cadastrar Livro':
                    janela_Procurar_Livro.hide()

                    layoutCadLivro = [
                        [sg.Text('Nome do Livro:'), sg.InputText(key='nome')],
                        [sg.Text('Autor do Livro:'), sg.InputText(key='autor')],
                        [sg.Text('Ano de Publicação:'), sg.InputText(key='ano_publi')],
                        [sg.Button('Adicionar')],
                        [sg.Button('Voltar')]
                    ]

                    
                    janela_Cadastro_Livro = sg.Window('Adicionar Livro', layoutCadLivro)

                    while True:
                        eventCadLivro, valuesCadLivro = janela_Cadastro_Livro.read()

                        if eventCadLivro == sg.WINDOW_CLOSED:
                            break
                        elif eventCadLivro == 'Adicionar':
                            nome = valuesCadLivro['nome']
                            autor = valuesCadLivro['autor']
                            ano_publi = valuesCadLivro['ano_publi']
                            int(ano_publi)
                            livro = livros.Livros(nome,autor,int(ano_publi))
                            addlivro = livros.Livros.adicionarLivro(livro)

                            if addlivro:
                                sg.popup('Livro adicionado com sucesso!')
                                janela_Cadastro_Livro['nome'].update('')
                                janela_Cadastro_Livro['autor'].update('')
                                janela_Cadastro_Livro['ano_publi'].update('')
                            else:
                                sg.popup('Esse livro ja foi cadastrado!')

                        elif eventCadLivro == "Voltar":
                            janela_Cadastro_Livro.close()
                            janela_Procurar_Livro.un_hide()

                elif eventProc == 'Deletar Livro':
                    x = sg.popup_get_text('Qual livro desejas deletar?')
                    deletarLivro = livros.Livros.deletarLivros(x)

                    if deletarLivro:
                        sg.popup('Livro deletado')
                    else:
                        sg.popup('Livro não encontrado')


    elif event == 'Cadastrar':
        janela_login.hide()
        cadastro = cadastrar.Cadastro()

        layot_cadastro = [
        [sg.Text('Novo Login'), sg.Input(key='novoLogin')],
        [sg.Text('Nova Senha'), sg.Input(key='novaSenha', password_char='*')],
        [sg.Button('Salvar Cadastro')],
        [sg.Button('Cancelar')]
        ]

        janela_cadastro = sg.Window('Cadastro', layot_cadastro)

        cadastro_aberto = True

        if cadastro_aberto:
            event1, values1 = janela_cadastro.read()

            if event1 == sg.WIN_CLOSED or event1 == 'Cancelar':
                janela_cadastro.close()
                janela_login.un_hide()
                cadastro_aberto = False
            
            elif event1 == 'Salvar Cadastro':
                sg.popup('Cadastro realizado com sucesso!')
                cadLogin = values1['novoLogin']
                cadSenha = values1['novaSenha']

                cadLoginStr = str(cadLogin)
                cadSenhaStr = str(cadSenha)

                cadastro.cadastroPessoa(cadLoginStr, cadSenhaStr)

                janela_cadastro.close()
                janela_login.un_hide()
                cadastro_aberto = False

                   

                   

              

janela_login.close()

