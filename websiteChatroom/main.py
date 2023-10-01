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
    nome_usuario = ft.TextField()

    # ETAPA2: Criar o Pop Up para inserir o nome de usuário e entrar no chat (FRONT)
    popup = ft.AlertDialog(
        title=ft.Text("Bem vindo(a) ao chat"),          # A parte superior da caixa (como um "header")
        modal=True,                                     # shape do popup
        content=nome_usuario,                           # O corpo da caixa
        actions=[ft.ElevatedButton(text="Entrar")],     # A parte inferior da caixa
        on_dismiss=lambda e: print("Popup finalizado")
    )

    def entrar_chat(evento): # ---> "Event Handler" (similar ao JS)
        pagina.dialog = popup
        popup.open = True
        pagina.update() # Recarrega a página

        join_txt = ft.Text("Entrou no chat")
        pagina.add(join_txt)

    # ETAPA1: Botão "Iniciar Chat" (FRONT)
    botao_iniciar = ft.ElevatedButton(text="Iniciar chat", on_click=entrar_chat)



    # -------------------- DESENHAR NA PÁGINA ----------------------- #
    # Para adicionar um item na página, é necessário usar a função .add() 
    pagina.add(
        texto,
        botao_iniciar
    )


# Cada página será uma função diferente
def pagina2():
    pass

# FLET-PASSO-3: Função app() Sinaliza qual é a página inicial do app
# É necessário passar a página principal para essa função usando o parâmetro 'target'
ft.app(target=main, view=ft.WEB_BROWSER) # Padrão: view=AppView
# Modificando o parâmetro view para 'view=ft.WEB_BROWSER' possibilita visualizar o app como site
# Endereço: localhost:53933





# ETAPA3: Quando entrar no chat: (BACK) 
    # A mensagem sinalizando que o usuário entrou no chat
    # O campo e o botão de enviar mensagem devem ser criados

# ETAPA4: A cada mensagem enviada: (BACK) 
    # Nome: {Texto da mensagem}
