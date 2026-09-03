import pandas as pd
import matplotlib.pyplot as plt
 
notas = [5, 6, 7, 8, 9, 10]
 
serie = pd.Series(notas)
frequencias = serie.value_counts().sort_index()
 
frequencias.plot(kind='bar')
 
plt.xlabel("Nota")
plt.ylabel('Frequencias')
plt.title('Distribuição das Notas')
 
plt.show()
 