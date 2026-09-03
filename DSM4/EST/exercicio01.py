import pandas as pd

dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana"],
    "Idade": [18, 20, 19, 29]
}

df = pd.DataFrame(dados)

df.info()

print(df.describe())

#print(df.head()) - Primeiras linhas

print(df) #DataFrame completo

print(len(df)) #Lê o tamanho

print(df.shape) #Linhas e colunas