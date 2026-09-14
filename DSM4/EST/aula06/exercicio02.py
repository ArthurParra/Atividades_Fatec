import pandas as pd

Ga = [100, 100,100,100,100]
Gb = [80, 90, 100, 110, 120]

serie_a = pd.Series(Ga)
serie_b = pd.Series(Gb)


print("Grupo A")
print(f"Média: {serie_a.mean()}, Amplitude: {serie_a.max() - serie_a.min()}")
print(f"Varaincia amostral: {serie_a.var()}, variancia populacionaol: {serie_a.var(ddof=0)}")

print(8*"*")

print("Grupo B")
print(f"Média: {serie_b.mean()}, Amplitude: {serie_b.max() - serie_b.min()}")
print(f"Varaincia amostral: {serie_b.var()}, variancia populacionaol: {serie_b.var(ddof=0)}")