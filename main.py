import matplotlib.pyplot as plt
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

# Calcular o total de vendas por região
total_vendas_por_regiao = dados.groupby('Region')['Sales'].sum()
print("\nTotal de vendas por região:")
print(total_vendas_por_regiao.round(2))

# Calcular a média de lucro por subcategoria de produto
media_lucro_por_subcategoria = dados.groupby('Sub-Category')['Profit'].mean()
print("\nMédia de lucro por subcategoria:")
print(media_lucro_por_subcategoria.round(2))

# Criar um gráfico de barras para o total de vendas por região
total_vendas_por_regiao.plot(kind='bar', color='skyblue')

plt.title('Total de Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Total de Vendas ($)')
plt.show()

# Criar um gráfico de pizza para percentual de vendas por categoria
total_vendas_por_categoria = dados.groupby('Category')['Sales'].sum()
total_vendas_por_categoria.plot(kind='pie', autopct='%1.1f%%', startangle=90)

plt.title('Percentual de Vendas por Categoria')
plt.show()
