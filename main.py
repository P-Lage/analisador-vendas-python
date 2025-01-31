import pandas as pd

dados = pd.read_csv('dados_vendas.csv')
print(dados.head())

total_vendas = dados['Vendas'].sum()
print(f"Total de vendas: {total_vendas}")
