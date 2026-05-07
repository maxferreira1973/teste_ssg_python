# Teste Técnico - Especialista de Dados 📊

Este repositório contém a resolução do desafio técnico de análise de dados, abrangendo manipulação de dados com Pandas, visualização estatística e modelagem preditiva com Scikit-Learn.

## 🛠️ Tecnologias Utilizadas
- **Python 3.12**
- **Pandas**: Processamento e manipulação de DataFrames.
- **Scikit-Learn**: Implementação de Regressão Linear e métricas de avaliação.
- **Matplotlib & Seaborn**: Geração de gráficos com backend para ambientes Linux (Agg).
- **Ambiente Virtual (venv)**: Isolamento de dependências.

## 📋 Detalhamento dos Exercícios (1 a 5)

O projeto foi estruturado para responder aos cinco pontos principais do enunciado:

**1. Cálculo de Faturamento (Exercício 1)**
* **O que foi feito:** Criação da coluna `Valor_Total`.
* **Lógica:** Realizada a multiplicação das colunas `Quantidade` e `Preco_Unitario`. Esta etapa é a base para todas as métricas financeiras subsequentes.

**2. Performance por Produto (Exercício 2)**
* **O que foi feito:** Cálculo do faturamento total agrupado por `Produto`.
* **Lógica:** Utilizei o método `.groupby()` para consolidar as vendas, permitindo identificar quais itens geram maior receita para a operação.

**3. Liderança de Mercado (Exercício 3)**
* **O que foi feito:** Identificação do produto com maior quantidade vendida.
* **Lógica:** Agrupamento por soma de quantidades e aplicação do método `.idxmax()` para localizar automaticamente o produto líder em volume.

**4. Filtragem Regional e de Valor (Exercício 4)**
* **O que foi feito:** Filtro de vendas da Região **'Norte'** com valor superior a **R$ 30,00**.
* **Lógica:** Aplicação de filtros lógicos compostos (operador `&`). Esta análise demonstra a capacidade de extrair insights específicos de nichos geográficos e faixas de preço.

**5. Tratamento de Séries Temporais (Exercício 5)**
* **O que foi feito:** Extração do mês da venda.
* **Lógica:** Conversão da coluna para o tipo `datetime` e extração do atributo `.month`. Essencial para entender a sazonalidade e o comportamento das vendas ao longo do ano.

## 📈 Visualização e Modelagem
* **Gráfico:** Foi gerado um gráfico de barras (`grafico_vendas.png`) com rótulos de dados formatados no padrão brasileiro (`R$ 0.000,00`) para facilitar a leitura.
* **Modelo Preditivo:** Implementação de Regressão Linear com um **R² de 0.88**, indicando que o modelo explica 88% da variabilidade dos dados.

## 🚀 Como Executar
1. Clone o repositório.
2. Crie o ambiente virtual: `python3 -m venv venv`.
3. Ative o ambiente: `source venv/bin/activate`.
4. Instale as dependências: `pip install pandas numpy scikit-learn matplotlib seaborn`.
5. Execute o script: `python3 solucao.py`.

---
Desenvolvido por **[Seu Nome]** para o processo seletivo de Especialista de Dados.