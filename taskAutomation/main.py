import os
import time
import pyautogui    # Comando CLI: pip install pyautogui
import pandas       # Comando CLI: pip install pandas numpy openpyxl
'''
Comandos pyautogui:
### pyautogui.click -> Clicar com o mouse
### pyautogui.write -> Escrever um texto
### pyautogui.press -> Aperta 1 tecla
### pyautogui.hotkey -> Atalho (combinação de teclas)
'''

# ---- Entrar no sistema da empresa ---- #

# Espera 0.5 segundos antes de executar cada ação (referente ao pyautogui)
pyautogui.PAUSE = 0.5

# Abrir o Chrome
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# Configurando a janela: Comando do Windows para maximizar a janela atual
pyautogui.hotkey('win', 'up')

# Entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# time.sleep faz parte da biblioteca time, que é nativa do python
time.sleep(1.5)

# ---- Fazer login ---- #
pyautogui.press("tab") # Passando pro campo de email
# pyautogui.click(670, 393, clicks=2)
pyautogui.write("exemplo@gmail.com")
pyautogui.press("tab") # Passando pro campo de senha
pyautogui.write("123456")
pyautogui.press("tab") # Passando pro botão de login
pyautogui.press("enter")
time.sleep(2.5) # Esperando o site carregar

# ---- Importar a base de dados de produtos usando a biblioteca pandas ---- #

# Pegando o endereço absoluto do diretório em que esse script se encontra
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construindo o endereço absoluto do arquivo CSV
csv_file_path = os.path.join(script_dir, 'produtos.csv')

# Read the CSV using the absolute path
tabela = pandas.read_csv(csv_file_path)
# tabela = pandas.read_csv("./produtos.csv")
# print(tabela)

# ---- Repetir o cadastro para todos os produtos (percorrendo cada linha existente na tabela) ---- #
for linha in tabela.index: # para colunas, seria: tabelas.column
    # ---- Cadastrar produto ---- #
    #pyautogui.click(x=660, y=276)

    # Pegando o código único de cada produto e armazenando na variável código 
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    # Resetando o TAB
    pyautogui.click(x=181, y=493)
    pyautogui.press("tab") 
    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab") 
    pyautogui.write(str(marca))
    pyautogui.press("tab") 
    pyautogui.write(str(tipo))
    pyautogui.press("tab") 
    pyautogui.write(str(categoria))
    pyautogui.press("tab") 
    pyautogui.write(str(preco))
    pyautogui.press("tab") 
    pyautogui.write(str(custo))
    pyautogui.press("tab") 
    # Campo obs
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(50000) # positivo: sobe | negativo: desce

"""
Representação reduzida da tabela produtos.csv

         codigo       marca        tipo  categoria  preco_unitario  custo               obs
0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
..          ...         ...         ...        ...             ...    ...               ...
288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN
"""