import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

plt.switch_backend('Agg')

# Carga dos dados
try:
    df_vendas = pd.read_csv('vendas.csv')
except:
    df_vendas = pd.read_csv('vendas - vendas.csv')

# --- EXERCÍCIO 1 ---
# 1. Crie uma nova coluna 'Valor_Total' que seja 'Quantidade' * 'Preco_Unitario'.
df_vendas['Valor_Total'] = df_vendas['Quantidade'] * df_vendas['Preco_Unitario']

# Atribuição solicitada pelo avaliador
df_resultante = df_vendas.copy() 

# Exibição para conferência
print("--- RESPOSTA EXERCÍCIO 1 ---")
print(" ")
print(df_resultante[['Produto', 'Quantidade', 'Preco_Unitario', 'Valor_Total']].head())
print(" ")

# EXERCÍCIO 2

# Configuração para evitar erro de interface gráfica no Linux
plt.switch_backend('Agg')

# --- RESOLUÇÃO ---

# 1. Estatísticas descritivas
print("--- RESPOSTA EXERCÍCIO 2 ---")
print(" ")
print("1. Estatísticas Descritivas (Valor_Total):")
print(df_resultante['Valor_Total'].describe())
print("\n")

# 2. Distribuição por Região
dist_regiao = df_resultante.groupby('Regiao')['Valor_Total'].agg(['mean', 'std'])
print("2. Média e Desvio Padrão por Região:")
print(dist_regiao)
print("\n")

# 3. Gráfico de barras: Valor_Total por Produto
plt.figure(figsize=(10, 6))
vendas_produto = df_resultante.groupby('Produto')['Valor_Total'].sum().sort_values(ascending=False)

# Criamos o gráfico
ax = sns.barplot(
    x=vendas_produto.index, 
    y=vendas_produto.values, 
    hue=vendas_produto.index, 
    palette='viridis', 
    legend=False
)

# ALTERNATIVA ROBUSTA PARA RÓTULOS:
# Iteramos sobre as barras (patches) para colocar os valores manualmente
for i, bar in enumerate(ax.patches):
    valor = vendas_produto.values[i]
    # Formatação Brasileira: R$ 0.000,00
    texto = f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    
    # Adiciona o texto acima da barra
    ax.annotate(texto, 
                (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                ha='center', va='bottom', 
                fontsize=9, xytext=(0, 5), 
                textcoords='offset points')

plt.title('Valor Total de Vendas por Produto')
plt.ylim(0, vendas_produto.max() * 1.15)
plt.tight_layout()
plt.savefig('valor_total_por_produto.png')
plt.close()
print("3. Gráfico 'valor_total_por_produto.png' salvo.\n")

# 4. Boxplot: Valor_Total por Regiao
plt.figure(figsize=(10, 6))
sns.boxplot(x='Regiao', y='Valor_Total', data=df_resultante, hue='Regiao', palette='Set2', legend=False)
plt.title('Distribuição de Valor Total por Região (Boxplot)')
plt.tight_layout()
plt.savefig('boxplot_valor_total_por_regiao.png')
plt.close()
print("4. Boxplot 'boxplot_valor_total_por_regiao.png' salvo.\n")

# 5. Valores acima do percentil 75
percentil_75 = df_resultante['Valor_Total'].quantile(0.75)
valores_acima_75 = df_resultante[df_resultante['Valor_Total'] > percentil_75]

print(f"5. Valores acima do Percentil 75 (Corte: R$ {percentil_75:,.2f}):")
print(valores_acima_75[['Produto', 'Regiao', 'Valor_Total']])
print(" ")

# EXERCÍCIO 3: Modelo Preditivo Básico


# Pré-processamento: Garantir que as colunas numéricas estejam corretas
df_modelo = df_resultante[['Quantidade', 'Preco_Unitario', 'Valor_Total']].copy()

# Definir features (X) e target (y)
X = df_modelo[['Quantidade', 'Preco_Unitario']]
y = df_modelo['Valor_Total']

# --- RESOLUÇÃO DAS PERGUNTAS ---

# 1. Divida os dados em conjuntos de treino (80%) e teste (20%) usando random_state=42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print("1. Divisão de dados concluída (80% treino, 20% teste).")


# 2. Treine um modelo de Regressão Linear Simples
modelo = LinearRegression()
modelo.fit(X_train, y_train)
print("2. Modelo de Regressão Linear treinado com sucesso.")


# 3. Faça previsões no conjunto de teste
y_pred = modelo.predict(X_test)
print("3. Previsões realizadas no conjunto de teste.")


# 4. Calcule o Erro Quadrático Médio (MSE) e o R² do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"4. Métricas do Modelo:")
print(f"   - MSE: {mse:.2f}")
print(f"   - R²: {r2:.2f}\n")


# 5. Explicação e Avaliação do Modelo
print("5. Explicação Técnica:")
explicação = f"""
O MSE (Erro Quadrático Médio) de {mse:.2f} representa a média dos erros ao quadrado; 
quanto menor esse valor, mais próximas as previsões estão dos valores reais. 

O R² (Coeficiente de Determinação) de {r2:.2f} indica que o modelo explica {r2*100:.0f}% 
da variabilidade dos dados. 

Avaliação: Um R² próximo de 1.00 (como o obtido) demonstra que o modelo é excelente para 
prever o faturamento, o que faz sentido técnico, já que o 'Valor_Total' é uma relação 
linear direta de 'Quantidade' e 'Preco_Unitario'.
"""
print(explicação)

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