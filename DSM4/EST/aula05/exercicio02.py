import pandas as pd

salarios = pd.Series([2500, 3000, 2800, 3200, 2700, 3500, 2900, 3100, 3300, 3000])

print(f"média: {salarios.mean()}")
print(f"mediana: {salarios.median()}")

tamanho = len(salarios)
tamanho_moda =len (salarios.mode())

if(tamanho_moda == tamanho):
    print("Amodal")
else:
    print(salarios.mode())


print(f"Minimo: {salarios.min()}, Maximo: {salarios.max()}")




