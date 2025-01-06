import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

Base_Dados = pd.read_csv('StudentsPerformance.csv')

#Renomeando as colunas
Base_Dados.rename(columns={
    'gender': 'Gênero',
    'race/ethnicity': 'Etinía',
    'parental level of education': 'Nivel Educação Parental',
    'test preparation course': 'Curso preparatório',
    'math score': 'Nota Matemática',
    'reading score': 'Nota Letras',
    'writing score': 'Nota Redação',
    'lunch': 'Bolsa'
}, inplace= True)

plt.figure(figsize=(30, 25), facecolor= '#faf9d4')
g = gridspec.GridSpec(9, 3)
plt.suptitle('Análise da Performance dos Estudantes', fontsize=37, fontweight='semibold', y= 0.95)

axes1 = plt.subplot(g[:3, 0])

axes2 = plt.subplot(g[0, 1])
axes3 = plt.subplot(g[1, 1])
axes4 = plt.subplot(g[2, 1])

axes5 = plt.subplot(g[:3, 2])

def mediaNotasPor(ax, colunaEscolhida):
    Parental_Math = Base_Dados.groupby(by= [colunaEscolhida]).mean('Nota Matemática')['Nota Matemática'].reset_index()
    Parental_Read = Base_Dados.groupby(by= [colunaEscolhida]).mean('Nota Letras')['Nota Letras'].reset_index()
    Parental_Writ = Base_Dados.groupby(by= [colunaEscolhida]).mean('Nota Redação')['Nota Redação'].reset_index()

    FigMathParent = Parental_Math['Nota Matemática'].sort_values(ascending= False)
    FigReadParent = Parental_Read['Nota Letras'].sort_values(ascending= False)
    FigWritParent = Parental_Writ['Nota Redação'].sort_values(ascending= False)
    EixoX = Base_Dados[colunaEscolhida].unique()


    ax.plot(EixoX, FigMathParent, color= 'red', marker= 'o', ms= '4', mec= '#000', markerfacecolor= 'w', label= 'Matemática')
    ax.plot(EixoX, FigReadParent, color= 'blue', marker= 'o', ms= '4', mec= '#000', markerfacecolor= 'w', label= 'Letras')
    ax.plot(EixoX, FigWritParent, color= 'green', marker= 'o', ms= '4', mec= '#000', markerfacecolor= 'w', label= 'Redação')

    ax.legend(loc= 'best')

def boxplot(ax, coluna, Materia):
    sns.boxplot(ax=ax, data= Base_Dados, x=Materia , y= coluna)
    
def pizza(ax, coluna): # Adicionando ax como argumento para especificar onde o gráfico será plotado
    pct = round(Base_Dados[coluna].value_counts(normalize=True) * 100, 1)
    pct = pct.values.tolist()

    label = Base_Dados[coluna].unique().tolist()

    explode = [0.05]
    for _ in range(len(label) - 1):
        explode.append(0)

    wedges, _, autotexts = ax.pie(pct, labels=label, autopct='%1.1f%%', explode=explode) # Alterado texts para _

    for w in wedges:
        w.set_linewidth(0.5)
        w.set_edgecolor('black')

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color('white')
        autotext.set_fontweight('semibold')

    colors = ['#ac4bbf', '#28b9de']
    if coluna == 'Gênero':
        for w, color in zip(wedges, colors):
            w.set_color(color)

mediaNotasPor(axes1, 'Nivel Educação Parental')

boxplot(axes2, 'Nivel Educação Parental', 'Nota Matemática')
boxplot(axes3, 'Nivel Educação Parental', 'Nota Letras')
boxplot(axes4, 'Nivel Educação Parental', 'Nota Redação')

pizza(axes5, 'Nivel Educação Parental')

axes6= plt.subplot(g[3:6, 0])

axes7= plt.subplot(g[3, 1])
axes8= plt.subplot(g[4, 1])
axes9= plt.subplot(g[5, 1])

axes10= plt.subplot(g[3:6, 2])

#Adicionar gráfico
mediaNotasPor(axes6, 'Gênero')

boxplot(axes7, 'Gênero', 'Nota Matemática')
boxplot(axes8, 'Gênero', 'Nota Letras')
boxplot(axes9, 'Gênero', 'Nota Redação')

pizza(axes10, 'Gênero')

axes11= plt.subplot(g[6:9, 0])

axes12= plt.subplot(g[6, 1])
axes13= plt.subplot(g[7, 1])
axes14= plt.subplot(g[8, 1])

axes15= plt.subplot(g[6:9, 2])

mediaNotasPor(axes11, 'Curso preparatório')

boxplot(axes12, 'Curso preparatório', 'Nota Matemática')
boxplot(axes13, 'Curso preparatório', 'Nota Letras')
boxplot(axes14, 'Curso preparatório', 'Nota Redação')

pizza(axes15, 'Curso preparatório')

axes2.set_ylabel('')
axes3.set_ylabel('')
axes4.set_ylabel('')
axes7.set_ylabel('')
axes8.set_ylabel('')
axes9.set_ylabel('')
axes12.set_ylabel('')
axes13.set_ylabel('')
axes14.set_ylabel('')

axes1.set_title('Médias das notas', loc= 'left')
axes2.set_title('Nível de Educação Parental', fontsize= 20, fontweight= 'semibold')
axes7.set_title('Gênero', fontsize= 20, fontweight= 'semibold')
axes12.set_title('Curso Preparatório', fontsize= 20, fontweight= 'semibold')

plt.subplots_adjust(hspace=0.7, wspace=0.3)
plt.show()
