import pandas as pd

dados = {
    'Estado':['Santa Catarina', 'Bahia', 'Rio de Janeiro'],
    'Ano':[2004,2005,2006],
    'Taxa de Desemprego':[1.5,1.7,1.6]
}

dataframe = pd.DataFrame(dados)
# print(dataframe.head(),type(dataframe))
# print(pd.DataFrame(dados,columns=['Estado','Taxa de Desemprego','Ano']))

dataframe2 = pd.DataFrame(
    dados,columns=['Estado', 'Taxa de Desemprego','Taxa Crescimento','Ano'],
    index=['estado_1','estado_2','estado_3'])
# print(dataframe2)
# print(f'\n{dataframe2.values}')
# print(f'\n{dataframe2.dtypes}')
# print(f'\n{dataframe2.columns}')
# print(dataframe2[['Estado','Ano']])

#Metódos
# print(dataframe2.describe()) # Retorna um resumo estatístico dos valores númericos
# print(dataframe2.isna()) # Retorna true para valores NaN

import numpy as np

dataframe2['Taxa Crescimento'] = np.arange(4.)[1:4]*1.34
# print(dataframe2.describe())

#Slicing Dataframes
# print(dataframe2['estado_1':'estado_3'])
# print(dataframe2[dataframe2['Taxa de Desemprego']<1.7])

dataframe3 = pd.read_csv("Aula17 - Pandas\dataset.csv")
print(dataframe3.head(7))
print(dataframe3.isna().sum())
moda = dataframe3['petal_width'].value_counts().index[0]
print(moda)
dataframe3['petal_width'].fillna(value = moda, inplace=True)
print(dataframe3.isna().sum())