import pandas as pd

# Leitura de dados

dados = pd.read_csv('dados_vendas.csv')
print(dados.head())

# Cálculo do total de vendas

total_vendas = dados['Vendas'].sum()
print(f"Total de vendas: {total_vendas}")

# Cálculo da média de vendas por produto

media_vendas_por_produto = dados.groupby('Produto')['Vendas'].mean().round(2)
print("\nMédia de vendas por produto:")
for produto, media in media_vendas_por_produto.items():
    print(f"{produto}: {media} vendas/mês")

# Cálculo do total de vendas por produto

total_vendas_por_produto = dados.groupby('Produto')['Vendas'].sum()

# Determinando o produto mais vendido

produto_mais_vendido = total_vendas_por_produto.idxmax()
total_do_produto_mais_vendido = total_vendas_por_produto.max()
print(f"\nO produto mais vendido foi: {produto_mais_vendido} com \
{total_do_produto_mais_vendido} vendas.")

# Criando a parte de visualização dos dados

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

total_vendas_por_produto.plot(kind='bar', color='skyblue')

plt.title('Total de Vendas por Produto', fontsize=16)
plt.xlabel('Produto', fontsize=12)
plt.ylabel('Total de Vendas', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()