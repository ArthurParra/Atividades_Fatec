import pandas as pd
 
tabela = pd.read_csv('dados.csv')
 
serie = tabela['idade']
 
# print(serie.value_counts().sort_index)
print(serie.value_counts(normalize=True))