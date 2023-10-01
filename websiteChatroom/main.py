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

    # --------------------------------------- BACK END --------------------------------------- #
    # ETAPA 4: Quando entrar no chat, o usuário pode enviar e receber mensagens na intranet (BACK) 
    # A mensagem sinalizando que o usuário entrou no chat
    def enviar_mensagem_tunel(mensagem): # ----> o parâmetro mensagem vai receber um dicionário
        mensagem_tipo = mensagem["tipo"]

        # ETAPA 5 (parte2): Envio de mensagens para todos os usuários (BACK) 
        # {Usuario}: {Texto da mensagem}
        if mensagem_tipo == "mensagem":
            mensagem_texto = mensagem["texto"]
            mensagem_usuario = mensagem["usuario"]
            # Adicionar a mensagem no chat p/ todos verem
            chat.controls.append(ft.Text(f"{mensagem_usuario}: {mensagem_texto}"))
        else: # mensagem_tipo == "entrada"
            mensagem_usuario = mensagem["usuario"]
            chat.controls.append(ft.Text(value=f"{mensagem_usuario} entrou no chat", size=12, italic=True, color=ft.colors.LIGHT_BLUE_400))

        pagina.update() # Recarrega a página (necessário para que mudanças ocorram)


    # Criar o túnel de conexão PUB-SUB (Publish & Subscribe)
    # subscribe() é responsável por transmitir essa mensagem a todos que estão conectados na intranet
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # -------------------------------------- FRONT END --------------------------------------- #
     
    # ETAPA 3: Criação do chat (FRONT)
    # O campo e o botão de enviar mensagem devem ser criados
    def fechar_popup_entrar_chat(evento):
        # ETAPA 5 (parte1): Na hora de entrar no chat, envia para o túnel o nome do usuário (BACK)
        pagina.pubsub.send_all({"usuario": campo_usuario.value, "tipo": "entrada"})

        # Adicionar o chat na página
        pagina.add(chat)

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
    
    # Ocorre quando o botão "Enviar" é clicado (FRONT)
    def enviar_mensagem(evento):
        # Envia para o túnel a mensagem que está armazenada no campo - criando um dicionário p/ mandar as duas informações
        pagina.pubsub.send_all({"usuario": campo_usuario.value, "texto": campo_mensagem.value, "tipo": "mensagem"})
        # Limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update() # Recarrega a página

    campo_usuario = ft.TextField(label="Escreva seu nome", autofocus=True, on_submit=fechar_popup_entrar_chat)
    campo_mensagem = ft.TextField(label="Digite uma mensagem", hint_text="Mensagem", autofocus=True, on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_mensagem)

    # ETAPA 2: Criação do Pop Up para inserir o nome de usuário e entrar no chat (FRONT)
    popup = ft.AlertDialog(
        title=ft.Text("Bem vindo(a) ao chat"),                                              # A parte superior da caixa (acima do content)
        modal=True,     # Modal=True --> Não dá pra sair do popup clicando fora. Modal=False, é possível ignorar a janelinha clicando em outro ponto da página.
        content=campo_usuario,                                                              # O corpo da caixa
        actions=[ft.ElevatedButton(text="Entrar", on_click=fechar_popup_entrar_chat)],      # A parte inferior da caixa (abaixo do content)
        on_dismiss=lambda e: print("Chat inicializado")
    )

    def abrir_popup(evento): # ---> "Event Handler" (similar ao JS)
        # Chama o pop up
        pagina.dialog = popup
        popup.open = True

        pagina.update() # Recarrega a página

    # ETAPA 1: Botão "Iniciar Chat" (FRONT)
    botao_iniciar = ft.ElevatedButton(text="Iniciar chat", on_click=abrir_popup)

    # -------------------- DESENHAR NA PÁGINA (ESTÁTICA) ----------------------- #
    # Para adicionar um item na página, é necessário usar a função .add() 
    # O que estiver aqui é o que é desenhado na tela logo que a página é iniciada pela primeira vez
    pagina.add(
        texto,
        botao_iniciar
    )

# Cada nova página seria uma função diferente
def pagina2():
    pass

# FLET-PASSO-3: Função app() Sinaliza qual é a página inicial do app
# É necessário passar a página principal para essa função usando o parâmetro 'target'
ft.app(target=main, view=ft.WEB_BROWSER, port=8000) # Padrão: view=AppView
# Modificando o parâmetro view para 'view=ft.WEB_BROWSER' possibilita visualizar o app como site

# Para abrir no browser ---> Endereços:
    # 127.0.01:8000 ou localhost:8000 (computador host)
    # Endereço IPv4:8000 (computadores na intranet - outros computadores conectados na mesma rede local)
    # Deploy (publicar o site em um domain para deixá-lo acessível em toda a internet usando de um servidor (AWS, Heroku, etc))