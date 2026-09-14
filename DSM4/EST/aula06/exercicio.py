import pandas as pd

dados = [10, 12, 15, 18, 20]

serie = pd.Series(dados)

print(f"Média aritmetica: {serie.mean()}")

print(f"Amplitude: {serie.mmax() - serie.min()}")

print(f"Variancia populacional: {serie.var(ddof=0)}")

print(f"Desvio padrao: {serie.std(ddof=0)}")