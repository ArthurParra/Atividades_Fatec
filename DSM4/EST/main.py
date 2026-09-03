#Nosso primeiro Dataframe

import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Aluno": ["Rogério", "Matheus", "Camila", "Geovana"],
    "Nota": [8,5,9,6]
}

df = pd.DataFrame(dados)

plt.bar(df["Aluno"], df["Nota"])

plt.show()

