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
    chat = ft.Column()
    campo_usuario = ft.TextField(label="Escreva seu nome")
    campo_mensagem = ft.TextField(label="Digite uma mensagem")

    # Adicionar o chat na página
    pagina.add(chat)

    # --------------------------------------- BACK END ---------------------------------------#
    # ETAPA 4: Quando entrar no chat, o usuário pode enviar e receber mensagens na intranet (BACK) 
    # A mensagem sinalizando que o usuário entrou no chat
    def enviar_mensagem_tunel(mensagem): # ----> o parâmetro mensagem vai receber um dicionário
        mensagem_texto = mensagem["texto"]
        mensagem_usuario = mensagem["usuario"]

        # Adicionar a mensagem no chat p/ todos verem
        chat.controls.append(ft.Text(f"{mensagem_usuario}: {mensagem_texto}"))

        pagina.update() # Recarrega a página (necessário para que mudanças ocorram na página)


    # Criar o túnel de conexão PUB-SUB (Publish & Subscribe)
    # subscribe() é responsável por transmitir essa mensagem a todos que estão conectados na intranet
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    # -----------------------------------------------------------------------------------------#
     
    # Ocorre quando o botão "Enviar" é clicado (FRONT)
    def enviar_mensagem(evento):
        # Envia para o túnel a mensagem que está armazenada no campo - criando um dicionário p/ mandar as duas informações
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": campo_usuario.value})
        # Limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update() # Recarrega a página


    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_mensagem)
    
    # ETAPA 3: Criação do chat (FRONT)
    # O campo e o botão de enviar mensagem devem ser criados
    def fechar_popup_entrar_chat(evento):
        # Fechar o Popup
        popup.open = False
        
        # Remover o título e o botão "Iniciar Chat"
        pagina.remove(texto)
        pagina.remove(botao_iniciar)

        pagina.add(ft.Row(      # Inline
            [       
                campo_mensagem, # Criar o campo de mensagem do usuário
                botao_enviar    # Criar o botão de "Enviar Mensagem"
            ]
        ))

        pagina.update() # Recarrega a página


    # ETAPA 2: Criação do Pop Up para inserir o nome de usuário e entrar no chat (FRONT)
    popup = ft.AlertDialog(
        title=ft.Text("Bem vindo(a) ao chat"),                                  # A parte superior da caixa (acima do content)
        modal=True,     # Modal=True --> Não dá pra sair do popup clicando fora. Modal=False, é possível ignorar a janelinha clicando em outro ponto da página.
        content=campo_usuario,                                                  # O corpo da caixa
        actions=[ft.ElevatedButton(text="Entrar", on_click=fechar_popup_entrar_chat)],      # A parte inferior da caixa (abaixo do content)
        on_dismiss=lambda e: print("Chat inicializado")
    )

    def entrar_popup(evento): # ---> "Event Handler" (similar ao JS)
        # Chama o pop up
        pagina.dialog = popup
        popup.open = True

        join_txt = ft.Text("Entrou no chat")
        pagina.add(join_txt)
        pagina.update() # Recarrega a página

    # ETAPA 1: Botão "Iniciar Chat" (FRONT)
    botao_iniciar = ft.ElevatedButton(text="Iniciar chat", on_click=entrar_popup)



    # -------------------- DESENHAR NA PÁGINA (ESTÁTICA) ----------------------- #
    # Para adicionar um item na página, é necessário usar a função .add() 
    # O que estiver aqui é o que é desenhado na tela logo que a página é iniciada pela primeira vez
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




# ETAPA 5: A cada mensagem enviada: (BACK) 
    # Nome: {Texto da mensagem}
