# Conjunto de dados para análise
# tempos = pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])
# Instruções para resolver a Tarefa em Python:
# Calcular a Média Aritmética simples;
# Calcular a Mediana dos tempos registrados;
# Calcular a Moda (ou modas) deste conjunto;
# Calcular os valores Mínimo e Máximo observados;
# Refletir: Qual dessas medidas melhor representa o comportamento central dos dados?
 
import pandas as pd
tempos = pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])
 
media = tempos.mean()
print('Média:', media)
 
mediana = tempos.median()
print('Mediana:', mediana)
 
moda = tempos.mode()
print("Moda:", moda.tolist())
 
minimo = tempos.min()
maximo = tempos.max()
print("Mínimo:", minimo)
print("Máximo:", maximo)