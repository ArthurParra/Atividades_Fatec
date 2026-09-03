import pandas as pd
import random
import numpy as np

alunos = pd.DataFrame({
    "nome": [
        'Ana', 'Bruno', 'Carlos', 'Daniela',
        'Eduardo', 'Fernanda', 'Gabriel', 'Helena',
        'Igor', 'Julia', 'Lucas', 'Mariana'
    ],
    'nota': [8,7,9,6,10,8,7,9,5,8,6,10]
})

#verificando tamanho da população:
print(alunos.shape[0])

#calculando a media da população:
print(alunos['nota'].mean())
#retire uma amostra de 5 alunos:
amostra = alunos.sample(n=5, random_state=42)

#comparar as duas medias:
media_amostra = amostra['nota'].mean()
print(media_amostra)

# df = pd.DataFrame(alunos)

# amostra = df.sample(n=5, random_state=42)

# media_populacao = df['nota'].mean()
