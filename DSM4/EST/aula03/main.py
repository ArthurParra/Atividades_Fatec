import pandas as pd
 
df = pd.read_csv("dados.csv")


nAmostra = 100
amostra = df.sample
 
print(df.shape)
print(df.head())
 
amostra = df.sample(n=100, random_state=15)
 
print(amostra.shape)
print(f"Média população: {df["idade"].mean()}")
 
print(f"Média da amostra: {amostra["idade"].mean()}")

