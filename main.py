# Importações para o programa
import pandas as pd
from twilio.rest import Client
accont_sid = "ACabb3b160a59a6aa6da9e5df884fda86b"
auth_token = "10f16c294d64d21ea5c71a1f359160b8"
client = Client(accont_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# ***OBSERVAÇÃO***
# Codigo abaixo lê cada arquivo de Excel
# tabela_vendas_janeiro = pd.read_excel(
#     'C:/Users/isabe/OneDrive - Fatec Centro Paula Souza/Isa/Programação/Python 3/Análise Bônus Viagem/janeiro.xlsx'
# )
# print(tabela_vendas_janeiro)

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(
        # Percorrer de forma dinamica na lista_meses e abrir vários arquivos em Excel
        # f: Formatar String
        f'C:/Users/isabe/OneDrive - Fatec Centro Paula Souza/Isa/Programação/Python 3/Análise Bônus Viagem/{mes}.xlsx'
    )
    # print(tabela_vendas)

    # Para cada arquivo:
    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    # Coluna da tabela do Excel | any() é algum em Inglês
    if (tabela_vendas['Vendas'] > 55000).any():
        # Quem é o vendedor e valor
        # loc ele vai procurar na linha e coluna da tabela (Resposta vai sempre uma tabela)
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']  # values é apenas valor
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'
        )
        # Se for maior que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        message = client.messages.create(
            to="+5511977202151",
            from_="+19895463356",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'
        )
        print(message.sid)
