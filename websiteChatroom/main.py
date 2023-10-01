'''Flet 
Ferramenta fullstack do Python capaz de construir aspectos do Front End e do Back End simultaneamente.

Ou seja, com o Flet é possível utilizar o mesmo código para fazer uma aplicação que rode na web, no desktop e até em mobile.

O Flet é interligado com o Flutter, a linguagem de programação da Google multi-plataforma.
'''

# -------------------- ETAPA 0: Configurar o Flet ----------------------- #
# FLET-PASSO-1: instalar e importar 
# Comando p/ instalar o Flet ---> pip install flet
import flet as ft


# FLET-PASSO-2: Modelo de execução do Flet --- Função main() deverá receber a página web principal como parâmetro
def main(pagina):
    texto = ft.Text("Chatroom")
    novo_texto = ft.Text("Novo texto")
    # botao = ft.IconButton()
    # alerta = ft.AlertDialog()


    # Para adicionar um item na página, é necessário usar a função .add() 
    pagina.add(texto)
    pagina.add(novo_texto)


# Cada página será uma função diferente
def pagina2():
    pass

# FLET-PASSO-3: Função app() Sinaliza qual é a página inicial do app
# É necessário passar a página principal para essa função usando o parâmetro 'target'
ft.app(target=main, view=ft.WEB_BROWSER) # Padrão: view=AppView
# Modificando o parâmetro view para ft.WEB_BROWSER possibilita visualizar o app como site
# Endereço: localhost:53933


# ETAPA1: Botão "Iniciar Chat" (FRONT)

# ETAPA2: Pop Up para inserir o nome de usuário e entrar no chat (FRONT)

# ETAPA3: Quando entrar no chat: (BACK) 
    # A mensagem sinalizando que o usuário entrou no chat
    # O campo e o botão de enviar mensagem devem ser criados

# ETAPA4: A cada mensagem enviada: (BACK) 
    # Nome: {Texto da mensagem}
