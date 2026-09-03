import matplotlib.pyplot as plt
import pandas as pd

notas = [
    7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9
]

#criar uma Series
serie = pd.Series(notas)

#calcular frequencia absoluta
fab = serie.value_counts()

#calcular frequencia relativa
fr = serie.value_counts(normalize=True)

#calcular frequencia acumulada
fac = fab.cumsum()

#criar tabela
tabela = pd.DataFrame({
    "F_absoluta": fab,
    "F_relativa": fr,
    "F_acumulada": fac
})

#criar um grafico de barras
fab.plot(kind='bar')

plt.title("Frequencia das notas")
plt.xlabel("Notas")
plt.ylabel("Frequencia")
plt.show()

#criar grafico de pizza
fab.plot(kind='pie', autopct='%1.1f%%')

plt.title("Frequencia das notas")
plt.show()