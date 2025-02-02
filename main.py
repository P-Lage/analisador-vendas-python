import pandas as pd

caminho_arquivo = 'Sample - Superstore.csv'
dados = pd.read_csv(caminho_arquivo)

print("Primeiras linhas do dataset:")
print(dados.head())

print("\nInformações do dataset:")
print(dados.info())

print("\nColunas disponíveis:")
print(dados.columns)
