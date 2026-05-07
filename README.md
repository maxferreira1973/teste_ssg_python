# Teste Técnico: Especialista de Dados - Resolução Completa 📊

Este repositório contém a solução detalhada para o desafio técnico de Especialista de Dados. O projeto foi desenvolvido em Python, utilizando um ambiente virtual (venv) no Ubuntu, com foco em manipulação de dados, análise estatística descritiva, visualização e modelagem preditiva.

---

## 🛠️ Tecnologias e Bibliotecas
* **Python 3.12**
* **Pandas**: Manipulação de DataFrames e leitura de arquivos.
* **Matplotlib & Seaborn**: Geração de gráficos profissionais (Barplot e Boxplot).
* **Scikit-Learn**: Divisão de dados, treinamento de Regressão Linear e métricas de avaliação (MSE, R²).

---

## 📋 Detalhamento dos Exercícios

### Exercício 1: Preparação e Manipulação
* **Ação**: Criação da coluna `Valor_Total` (Quantidade × Preço Unitário).
* **Destaque**: Uso do método `.copy()` para definir a variável `df_resultante`, conforme solicitado pelo avaliador para fins de validação e integridade dos dados.

### Exercício 2: Análise Descritiva e Visualização
1.  **Estatísticas Básicas**: Geração de média, mediana e desvios através do `.describe()`.
2.  **Agrupamento Regional**: Cálculo de métricas de dispersão por região.
3.  **Visualização de Vendas**: Gráfico de barras (`valor_total_por_produto.png`) com rótulos formatados em moeda brasileira (R$).
4.  **Análise de Outliers**: Boxplot (`boxplot_valor_total_por_regiao.png`) para visualizar a distribuição de preços por localidade.
5.  **Filtragem Estatística**: Identificação de registros acima do percentil 75.

### Exercício 3: Modelo Preditivo (Machine Learning)
* **Algoritmo**: Regressão Linear Simples.
* **Metodologia**: Divisão 80/20 (Treino/Teste) com `random_state=42`.
* **Métricas**: Avaliação de performance via MSE (Erro Quadrático Médio) e R² (Coeficiente de Determinação).

---

## 🚀 Como Executar o Projeto

1.  **Ativar o Ambiente Virtual**:
    ```bash
    source venv/bin/activate
    ```
2.  **Instalar Dependências**:
    ```bash
    pip install pandas matplotlib seaborn scikit-learn
    ```
3.  **Executar o Script**:
    ```bash
    python3 solucao.py
    ```

---

## 📂 Arquivos Gerados
* `solucao.py`: Script principal com os 3 exercícios.
* `valor_total_por_produto.png`: Gráfico de barras.
* `boxplot_valor_total_por_regiao.png`: Gráfico de distribuição.
* `README.md`: Documentação do projeto.

---
**Desenvolvido por [Seu Nome]**
