import numpy as np
import pandas as pd

np.random.seed(15)

dados = {
    "notas": np.random.normal(70, 10, 10000)
}

df = pd.DataFrame(dados)

amostra = df.sample(n=100, random_state=42)

media_populacao = df["notas"].mean()
media_amostra = amostra["notas"].mean()

print(f'Média da populacao: {media_populacao}')
print(f'Média da amostra: {media_amostra}')

