import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

plt.switch_backend('Agg')

try:
    df_vendas = pd.read_csv('vendas.csv')
except:
    df_vendas = pd.read_csv('vendas - vendas.csv')

# EXERCÍCIO 1
df_vendas['Valor_Total'] = df_vendas['Quantidade'] * df_vendas['Preco_Unitario']
print("--- RESPOSTA EXERCÍCIO 1 ---")
print("Coluna 'Valor_Total' criada.\n")

# EXERCÍCIO 2
vendas_por_produto = df_vendas.groupby('Produto')['Valor_Total'].sum()
print("--- RESPOSTA EXERCÍCIO 2 ---")
print(vendas_por_produto, "\n")

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=vendas_por_produto.index, y=vendas_por_produto.values, errorbar=None)
labels = [f'R$ {val:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') for val in vendas_por_produto.values]
ax.bar_label(ax.containers[0], labels=labels, padding=3)
plt.title('Valor Total de Vendas por Produto')
plt.ylim(0, vendas_por_produto.max() * 1.1)
plt.savefig('grafico_vendas.png')

# EXERCÍCIO 3
produto_mais_vendido = df_vendas.groupby('Produto')['Quantidade'].sum().idxmax()
print("--- RESPOSTA EXERCÍCIO 3 ---")
print(f"Produto mais vendido: {produto_mais_vendido}\n")

# EXERCÍCIO 4
vendas_norte_30 = df_vendas[(df_vendas['Regiao'] == 'Norte') & (df_vendas['Valor_Total'] > 30)]
print("--- RESPOSTA EXERCÍCIO 4 ---")
print(f"Total Norte > 30: {len(vendas_norte_30)}\n")

# EXERCÍCIO 5
df_vendas['Data_Venda'] = pd.to_datetime(df_vendas['Data_Venda'])
df_vendas['Mes_Venda'] = df_vendas['Data_Venda'].dt.month
print("--- RESPOSTA EXERCÍCIO 5 ---")
print(df_vendas[['Data_Venda', 'Mes_Venda']].head(), "\n")

# MODELO
X = df_vendas[['Quantidade', 'Preco_Unitario']]
y = df_vendas['Valor_Total']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = LinearRegression().fit(X_train, y_train)
print("--- MÉTRICAS ---")
print(f"R²: {r2_score(y_test, modelo.predict(X_test)):.2f}")