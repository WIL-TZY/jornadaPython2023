# Conversão de analise.ipynb para python script
# Biblioteca para usar display()
from IPython.display import display
# %% [markdown]
# # Análise de Dados preliminar com Python & Jupyter Notebooks
# 
# ### Case - Cancelamento de Clientes
# 
# Uma empresa hipotética com mais de 800 mil clientes deseja investigar por que a maioria de seus clientes registrados na base total são inativos (ou seja, cancelaram o serviço).
# 
# Essa análise de dados tem intuito de identificar os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.
# 
# Base de dados: cancelamentos.csv

# %%
# É possível fazer a instalação de pacotes diretamente nos notebooks, como se fosse um terminal. Basta clicar no botão e rodar.
# !pip install pandas   ---> Biblioteca bastante usada para manipular base de dados.
# !pip install numpy    ---> Fornece suporte para matrizes e arrays grandes e multidimensionais, juntamente com uma coleção de funções matemáticas para operar nessas matrizes.
# !pip install openpyxl ---> Uma biblioteca Python para leitura e gravação de arquivos Excel (XLSX).
# !pip install plotly   ---> Possibilita a criação de gráficos para a visualização de dados interativos e dinâmicos. É uma biblioteca conhecida por sua facilidade de uso.

# HTML export (with graphs)
# import plotly.io as pio
# pio.renderers.default = 'notebook'

# PDF export (with graphs)
# !pip install Pyppeteer
# !pyppeteer-install

# %%
# ETAPA 1: Importar e visualizar a base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")
# "Informação que não ajuda, atrapalha". É importante remover a coluna dos IDs dos usuários, visto que não ajuda na análise
tabela = tabela.drop(columns="CustomerID")

# Visualizar a base de dados
print("Visualização da base de dados (sem modificações): ")
display(tabela) # Função especial do Jupyte Notebooks

# %%
# ETAPA 2: Tratar problemas da base de dados

# Com o método .info() é possível encontrar valores vazios e valores do tipo errado na tabela
display(tabela.info()) 

# Joga fora todas as linhas que tem algum valor vazio
tabela = tabela.dropna() 

# Agora a tabela foi adequadamente tratada e está pronta p/ ser analisada
display(tabela.info()) 

# %%
# ETAPA 3: Primeira verificação -> Descobrir o percentual de clientes que cancelou

# Na coluna "cancelou" da tabela, value_counts() agrupa valores em categoria (int64)
display( tabela["cancelou"].value_counts() )

# Com o parâmetro 'normalize' verdadeiro, a função retorna em porcentagem (float64)
# Normalizar: indice_total / indice_de_valor_especifico 
# Logo, 499993 / 881659 --> para quem cancelou & 381666 / 881659 para quem não cancelou
display( tabela["cancelou"].value_counts(normalize=True) ) 

# EXTRA: Visualizando em porcentuual ao invés de float (usando o método .map() do Python)
#  .map("{:.1%}".format) --> Códigos de formatação são escritos como string "{:.1%}"
# "{:.1%}" --> Significa: Mostre o resultado como percentual e com apenas uma casa depois da vírgula
# OBS: É melhor não usar pois transforma o tipo de dado em objeto, o que não permite realizar cálculos


# CONCLUSÃO: Mais de 50% dos clientes cancelaram

# %% [markdown]
# ## Percentual de clientes que cancelaram suas assinaturas: 56%

# %%
# Que tipo de contrato (mensal, trimestral, anual) tende a ser mais cancelado?
display( tabela["duracao_contrato"].value_counts() ) 
display( tabela["duracao_contrato"].value_counts(normalize=True).map("{:.1%}".format) ) 

# %%
# Agrupamento (uma tabelinha já com os dados calculados de cada categoria que ajuda com a análise)

# Fazendo a média de cada coluna numérica
tabela_agrupada = tabela.groupby("duracao_contrato").mean(numeric_only=True)

display(tabela_agrupada)

# %% [markdown]
# ## O tipo de assinatura mais cancelada é a mensal (100% de cancelamento)
# CONCLUSÃO: Todos os clientes do contrato mensal cancelaram.
# 
# CAUSA: Provavelmente porque o plano não oferece benefícios satisfatórios.
# 
# SUGESTÃO: Oferecer desconto nos contratos anuais/trimestrais (pois eles são melhores). Ou melhorar os benefícios do contrato mensal.

# %%
# Agora que já se sabe porque as pessoas do plano mensal cancelaram, é hora de excluí-las da tabela para analisar outras causas de cancelamento adjacentes
# Excluindo a coluna do contrato mensal e armazenando em uma nova variável (tabela_filtrada)

# A variável exclui_mensal conterá um valor booleano (True ou False) para cada linha da coluna "duracao_contrato" da tabela
exclui_mensal = tabela["duracao_contrato"] != "Monthly"

# "True" : Não são do plano mensal 
# "False" : São do plano mensal
display(exclui_mensal) 

# %%
# Comparando tabelas

# A tabela resultante só vai mostrar as linhas que retornarem "True" na operação realizada pela variável exclui_mensal 
tabela_filtrada = tabela[exclui_mensal] # Com o pandas é possível passar uma condição dentro dos colchetes
#OBS: Aqui não seria possível usar o método .drop(), pois ele só funciona com colunas e "Monthly" é uma categoria presente em linhas

print("Tabela normal (com Monthly):")
display(tabela)

print("Tabela filtrada (sem Monthly):")
display(tabela_filtrada) # A tabela mostrada excluiu todas as linhas com contrato mensal

# %%
# Comparando os cancelamentos
 
# Antes (56% Cancelados ---> Com Monthly incluso)
display( tabela["cancelou"].value_counts(normalize=True) ) 

# Depois (46% Cancelados ---> Sem Monthly incluso)
display( tabela_filtrada["cancelou"].value_counts(normalize=True) ) 

# %%
# Just to allow HTML export
import plotly.io as pio
pio.renderers.default = 'notebook'

# %%
# ETAPA 4: Visualizando a causa dos cancelamentos com a ajuda de gráficos

# ------------- Rode esse bloco de código para gerar os gráficos ------------- #

# Criar gráficos para fazer a análise com o a ferramenta express da biblioteca plotly
import plotly.express as px

# Ver os diferentes tipos de gráficos oferecidos pelo plotly: https://plotly.com/python/
# O gráfico que será usado aqui é o histograma

# Criando um sample de DataFrame p/ passar as cores
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Definindo um color map customizável
color_map = {
    'A': 'red',
    'B': 'green',
    'C': 'blue'
}

# x='Category', y='Value', color='Category'
for coluna in tabela.columns:
    # Criar o gráfico
    grafico = px.histogram(tabela_filtrada, x=coluna, color="cancelou", color_discrete_map=color_map, text_auto=True)

    # Exibir o gráfico
    grafico.show()


# %% [markdown]
# ## Após a análise do gráfico, percebeu-se 3 principais causas de cancelamento.
# 
# ### 1- Assinatura mensal
# Todos os clientes do contrato mensal cancelaram. Provavelmente porque o plano não oferece benefícios satisfatórios.
# 
# ### 2- Quantidade de ligações feitas para o Call Center
# Acima de 4 ligações feitas para o call center, o cliente tende a cancelar. Sendo que acima de 6 ligações, todos os clientes cancelaram.
# 
# 
# ### 3- Dias de atraso no pagamento da fatura
# Acima de 20 dias de atraso, todos os clientes cancelaram.
# 

# %%
# Novamente, é hora de eliminar os casos em que já se obteve conclusões acerca do cancelamento
condicao_callcenter = tabela_filtrada["ligacoes_callcenter"] <= 4
condicao_atraso = tabela_filtrada["dias_atraso"] <= 20

# Ficando agora com a tabela que só inclui aquelas resultados que não ligaram pro call center mais de 4 vezes
tabela_filtrada = tabela_filtrada[condicao_callcenter]
tabela_filtrada = tabela_filtrada[condicao_atraso]

display( tabela_filtrada["cancelou"].value_counts(normalize=True) )

# %% [markdown]
# # Conclusões da análise 
# 
# De acordo com a simulação acima, retiradas as três principais causas, a média de cancelamentos cairia para apenas 26% (comparado com a taxa inicial de 53%).
# 
# Agora sim a taxa de cancelamentos está muito mais saudável e dentro do esperado.
