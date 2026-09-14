import pandas as pd

servidor_a = pd.Series([100, 101, 102,103,104])
servidor_b = pd.Series([70, 130, 90, 110, 100])

print(f"Média dos servidores: \n A: {servidor_a.mean()}, B: {servidor_b.mean()}")

amp_a = servidor_a.max() - servidor_a.min()
amp_b = servidor_b.max() - servidor_b.min()
print(f"Amplitude => A: {amp_a}, B: {amp_b}")

desv_a = servidor_a.std(ddof=0)
desv_b = servidor_b.std(ddof=0)

print(f"Desvio padrão => A: {desv_a}, B: {desv_b}")