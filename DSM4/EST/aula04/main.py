import pandas as pd
 
notas = [
 7, 8, 6, 9, 7,
 5, 8, 7, 10, 6,
 8, 9, 7, 5, 6,
 8, 7, 9, 8, 10
]
 
serie = pd.Series(notas)
 
print(serie.value_counts().sort_index())
print(serie.value_counts().sort_values())
print(serie.value_counts(normalize=True))
print(serie.value_counts(normalize=True) * 100)
 
frequencia = serie.value_counts().sort_index()
frequencia_acumulada = frequencia.cumsum()
 
print(frequencia_acumulada)
 
tabela = pd.DataFrame({
    "Frequencia": frequencia,
    "Frequencia_relativa": frequencia / len(serie),
    "Frequencia_acumulada": frequencia_acumulada,
})
 
print(tabela)