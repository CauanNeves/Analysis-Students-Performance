# Análise da Performance dos Estudantes

## Descrição
Este projeto realiza uma análise exploratória dos dados de desempenho dos estudantes a partir de um conjunto de dados chamado **StudentsPerformance.csv**. A análise é visualizada por meio de gráficos interativos, permitindo identificar padrões e correlações entre variáveis como gênero, nível educacional dos pais, participação em cursos preparatórios e desempenho nas disciplinas de Matemática, Leitura e Redação.

## Pré-requisitos
Antes de executar o código, certifique-se de ter as seguintes bibliotecas instaladas:

- `pandas`
- `matplotlib`
- `seaborn`
- `numpy`

Você pode instalá-las usando o pip:
```bash
pip install pandas matplotlib seaborn numpy
```

## Estrutura do Projeto
- **Base_Dados:** Carregamento e pré-processamento do conjunto de dados.
- **Renomeação de Colunas:** As colunas são renomeadas para facilitar a leitura e a interpretação.
- **Funções de Visualização:**
  - `mediaNotasPor`: Gráficos de linha para exibir médias das notas.
  - `boxplot`: Boxplots para representar a distribuição das notas.
  - `pizza`: Gráficos de pizza para exibir proporções.
- **Visualizações Principais:**
  - Análise por Nível de Educação Parental
  - Análise por Gênero
  - Análise por Curso Preparatório

## Uso
1. Certifique-se de que o arquivo **StudentsPerformance.csv** está no mesmo diretório que o script.
2. Execute o script Python:
```bash
python script.py
```
3. Os gráficos serão exibidos automaticamente.

## Saídas Geradas
- Gráficos de linha mostrando a média das notas.
- Boxplots comparando distribuições das notas.
- Gráficos de pizza representando distribuições de categorias.


## Autor
Desenvolvido por Cauan Neves
