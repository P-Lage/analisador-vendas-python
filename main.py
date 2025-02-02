import pandas as pd

caminho_arquivo = 'Sample - Superstore.csv'
dados = pd.read_csv(caminho_arquivo)

print("Primeiras linhas do dataset:")
print(dados.head())

print("\nInformações do dataset:")
print(dados.info())

print("\nColunas disponíveis:")
print(dados.columns)

# Calcular o total de vendas
total_vendas = dados['Sales'].sum()
print(f"\nTotal de vendas: ${total_vendas:.2f}")

# Calcular a média de vendas por categoria de produto
media_vendas_por_categoria = dados.groupby('Category')['Sales'].mean()
print("\nMédia de vendas por categoria:")
print(media_vendas_por_categoria.round(2))

# Calcular o total de vendas por produto
total_vendas_por_produto = dados.groupby('Product Name')['Sales'].sum()

# Identificar o produto mais vendido
produto_mais_vendido = total_vendas_por_produto.idxmax()
total_do_produto_mais_vendido = total_vendas_por_produto.max()

print(f"\nO produto mais vendido foi: {produto_mais_vendido} com $\
      {total_do_produto_mais_vendido:.2f} em vendas.")
