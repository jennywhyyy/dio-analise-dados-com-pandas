#!/usr/bin/env python
# coding: utf-8

# ## Desafio de projeto - DIO | Análise de dados com Python e Pandas:

# In[71]:


#importando as bibliotecas que usaremos nas análises:

import pandas as pd
import os as os
import matplotlib.pyplot as plt


# In[11]:


#importando os datasets que serão analisados:

aracaju = pd.read_excel("Aracaju.xlsx")
fortaleza = pd.read_excel("Fortaleza.xlsx")
natal = pd.read_excel("Natal.xlsx")
recife = pd.read_excel("Recife.xlsx")
salvador = pd.read_excel("Salvador.xlsx")
df_vendas = pd.read_excel("AdventureWorks.xlsx")
df_paises = pd.read_csv("Gapminder.csv", sep=";", encoding="latin-1")


# ### Trabalhando a primeira análise ("AdventureWorks.xlsx"):

# In[12]:


#visualizando as primeiras cinco linhas:

df_paises.head()


# In[14]:


#verificando quantas linhas e colunas há:

df_paises.shape


# In[17]:


#verificando quais são os tipos de dados por colunas:

df_paises.dtypes


# In[18]:


#renomeando os nomes das colunas para ficarem em português:

df_paises = df_paises.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})


# In[21]:


#vendo os novos nomes das colunas:

df_paises.columns


# In[22]:


#verificando as 15 primeiras entradas:

df_paises.tail(15)


# In[23]:


#descrevendo os dados(total, média, desvio padrão, mínimo, primeiro, segundo e terceiro quartis e máximpo):

df_paises.describe()


# In[24]:


#verificando a quantidade de entradas únicas na coluna de continentes:

df_paises["continente"].unique()


# In[25]:


#criando um novo dataframe com os dados relativos ao continente da Asia:

df_asia = df_paises.loc[df_paises["continente"] == "Asia"]


# In[26]:


#visualizando as primeiro cinco linhas do dataframe de vendas da Asia:

df_asia.head()


# In[28]:


#verificando quantos países há em cada continente:

df_paises.groupby("continente")["Pais"].nunique()


# In[29]:


#analisando a média de expectativa de vida em cada ano:

df_paises.groupby("Ano")["Expectativa de vida"].mean()


# In[30]:


#calculando a média de PIB por continente:

df_paises.groupby("continente")["PIB"].mean()


# In[31]:


#calculando a soma total de todos os PIB:

df_paises["PIB"].sum()


# 
# 
# 
# 
# 
# ## Trabalhando a segunda análise, com os dataframes de cidades nordestinas ("Aracaju.xlsx", "Fortaleza.xlsx", "Natal.xlsx", "Recife.xlsx", "Salvador.xlsx"):

# In[32]:


#unindo todos os dados em um único dataframe:

df_cidades = pd.concat([aracaju, fortaleza, natal, recife, salvador])


# In[33]:


#exibindo as cinco primeiras linhas:

df_cidades.head()


# In[34]:


#exibindo as cinco últimas linhas:

df_cidades.tail()


# In[35]:


#analisando os tipos de dados das diferentes colunas:

df_cidades.dtypes


# In[36]:


#alterando o tipo de dado da coluna LojaID de inteiro para objeto:

df_cidades["LojaID"] = df_cidades["LojaID"].astype("object")


# In[37]:


#verificando a alteração:

df_cidades.dtypes


# In[43]:


#verificando quais linhas possuem valores nulos:

df_cidades.isnull().sum()


# In[46]:


#criando uma coluna para calcular a receita:

df_cidades["Receita"] = df_cidades["Vendas"].mul(df_cidades["Qtde"])


# In[50]:


#criando uma coluna para o cálculo da proporção entre receita e vendas:

df_cidades["Receita/Vendas"] = df_cidades["Receita"] / df_cidades["Vendas"]


# In[51]:


#visualizando as alterações:

df_cidades.head()


# In[52]:


#calculando a receita mais alta:

df_cidades["Receita"].max()


# In[53]:


#calculando a receita mais baixa:

df_cidades["Receita"].min()


# In[54]:


#visualizando as cinco receitas mais altas:

df_cidades.nlargest(5, "Receita")


# In[55]:


#visualizando as cinco receitas mais baixas:

df_cidades.nsmallest(5, "Receita")


# In[56]:


#Verificando as somas da receita por cada cidade:

df_cidades.groupby("Cidade")["Receita"].sum()


# In[58]:


#criando três novas colunas, referente aos dias, meses e anos das vendas:

df_cidades["Dia_Venda"], df_cidades["Mes_Venda"], df_cidades["Ano_Venda"] = (df_cidades["Data"].dt.day, df_cidades["Data"].dt.month, df_cidades["Data"].dt.year)


# In[59]:


#verificando as alterações:

df_cidades.head()


# In[60]:


#visualizando a data mais antiga:

df_cidades["Data"].min()


# In[61]:


#criando uma coluna referente ao trimeste da venda:

df_cidades["Trimestre_Venda"] = df_cidades["Data"].dt.quarter


# In[62]:


#visualizando a alteração:

df_cidades.head()


# In[64]:


#selecionando as vendas ocorridas no mês de março do ano de 2019:

vendas_marco_19 = df_cidades.loc[(df_cidades["Data"].dt.year == 2019) & (df_cidades["Data"].dt.month == 3)]


# In[65]:


#visualizando os dados:

vendas_marco_19.sample(20)


# #### Visualização dos dados:

# In[67]:


#criando o gráfico de barras: 

df_cidades["LojaID"].value_counts(ascending = False).plot.bar()


# In[68]:


#criando um gráfico de barras horizontais, decrescente:

df_cidades["LojaID"].value_counts().plot.barh()


# In[69]:


#criando outro gráfico de barras, crescente:

df_cidades["LojaID"].value_counts(ascending = True).plot.barh()


# In[70]:


#criando um gráfico de pizza sobre os valores da receita por ano:

df_cidades.groupby(df_cidades["Data"].dt.year)["Receita"].sum().plot.pie()


# In[74]:


# plotando o gráfico sobre o total de vendas por cidade:

df_cidades["Cidade"].value_counts().plot.bar(title = "Total de vendas por cidade:")
plt.xlabel("Cidade")
plt.ylabel("Total de vendas")


# In[76]:


#criando o gráfico que relaciona o total de produtos vendidos aos meses:

df_cidades.groupby(df_cidades["Mes_Venda"])["Qtde"].sum().plot(title = "Total de produtos vendidos x Mês")
plt.xlabel("Mês")
plt.ylabel("Total de produtos vendidos")
plt.legend()


# In[80]:


#plotando o gráfico de produtos vendidos por mês no ano de 2019:

vendas_2019 = df_cidades[df_cidades["Ano_Venda"] == 2019]

vendas_2019.groupby(vendas_2019["Mes_Venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total de produtos vendidos")
plt.legend()


# In[81]:


#plotando o histograma da quantidade de produtos vendidos:

plt.hist(df_cidades["Qtde"], color = "blue")


# In[83]:


#agrupando os valores das receitas e dias de vendas em 2019;

plt.scatter(x = vendas_2019["Dia_Venda"], y = vendas_2019["Receita"])


# ## Trabalhando a terceira e última análise ("AdventureWorks.xlsx"):

# In[84]:


#visualizando as 5 primeiras linhas do dataframe:

df_vendas.head()


# In[86]:


#verificando a quantidade de linhas e colunas:

df_vendas.shape


# In[88]:


#verificando os tipos de dados:

df_vendas.dtypes


# In[89]:


#checando se há dados nulos no dataframe:

df_vendas.isnull().sum()


# In[90]:


#calculando o valor total da receita:

df_vendas["Valor Venda"].sum()


# In[92]:


#criando uma nova coluna, relativa aos custos totais das vendas:

df_vendas["custo_total"] = df_vendas["Custo Unitário"].mul(df_vendas["Quantidade"])


# In[94]:


#verificando a mudança:

df_vendas.head()


# In[96]:


#verificando o valor total dos custos:

df_vendas["custo_total"].sum()


# In[97]:


#criando uma coluna relativa ao lucro obtido, baseado na diferença entre a receita e o custo:

df_vendas["lucro"] = df_vendas["Valor Venda"] - df_vendas["custo_total"]


# In[98]:


#verificando a nova mudança:

df_vendas.head()


# In[99]:


#calculando o valor total do lucro:

df_vendas["lucro"].sum()


# In[104]:


#criando uma nova coluna, relativa aos números de dias que os pedidos levaram da venda até o envio:

df_vendas["tempo_envio"] = (df_vendas["Data Envio"] - df_vendas["Data Venda"]).dt.days


# In[105]:


#verificando a nova inserção:

df_vendas.head()


# In[106]:


#calculando a média do tempo de envio de cada marca:

df_vendas.groupby("Marca")["tempo_envio"].mean()


# In[107]:


#calculando o lucro de cada marca, por ano:

df_vendas.groupby([df_vendas["Data Venda"].dt.year, "Marca"])["lucro"].sum()


# In[108]:


#criando um novo dataframe, com o index zerado, relativo aos dados de ano de venda, marca e lucro:

df_lucro_anual = df_vendas.groupby([df_vendas["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()


# In[109]:


#visualizando as cinco primeiras entradas do novo dataframe:

df_lucro_anual.head()


# In[110]:


#analisando a quantidade vendida de cada tipo distinto de produto, em ordem decrescente:

df_vendas.groupby("Produto")["Quantidade"].sum().sort_values(ascending = False)


# In[111]:


#plotando o gráfico que relaciona a quantidade de vendas ao produto:

df_vendas.groupby("Produto")["Quantidade"].sum().sort_values(ascending = True).plot.barh(title = "Total de produtos vendidos")
plt.xlabel("Total de vendas")
plt.ylabel("Produto")


# In[112]:


#plotando um gráfico para comparar os lucros de cada ano:

df_vendas.groupby(df_vendas["Data Venda"].dt.year)["lucro"].sum().plot.bar(title = "Lucro por ano")
plt.xlabel("Ano")
plt.ylabel("Receita")


# In[115]:


#criando um novo dataframe, apenas com os dados do ano de 2009:

df_vendas_2009 = df_vendas[df_vendas["Data Venda"].dt.year == 2009]


# In[116]:


#observando o novo dataframe criado:

df_vendas_2009.head()


# In[117]:


#plotando um gráfico para a relação entre os lucros e os meses do ano de 2009:

df_vendas_2009.groupby(df_vendas_2009["Data Venda"].dt.month)["lucro"].sum().plot(title = "Lucro por mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")


# In[120]:


#criando o gráfico da relação entre as marcas e seus respectivos lucros, no ano de 2009:

df_vendas_2009.groupby("Marca")["lucro"].sum().plot.bar(title = "Lucro por marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = 'horizontal')


# In[121]:


#plotando o gráfico da relação entre os lucros por classes, em 2009:

df_vendas_2009.groupby("Classe")["lucro"].sum().plot.bar(title = "Lucro por classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")


# In[122]:


#plotando o boxplot relativo ao tempo de envio:

plt.boxplot(df_vendas["tempo_envio"])


# In[123]:


#criando o histograma relativo ao tempo de envio:

plt.hist(df_vendas["tempo_envio"])


# In[124]:


#calculando o menor tempo de envio:

df_vendas["tempo_envio"].min()


# In[125]:


#calculando o maior tempo de envio:

df_vendas["tempo_envio"].max()


# In[126]:


#identificando os dados do outlier:

df_vendas[df_vendas["tempo_envio"] == 20]


# In[ ]:




