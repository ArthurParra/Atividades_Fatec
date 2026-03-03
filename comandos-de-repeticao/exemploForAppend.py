import os
os.system('cls')
#exemplo For Append para adicionar os valores a lista

numeros = []

for i in range(1,5):
    n = int(input(f"Digite o {i}º número da lista: "))
    numeros.append(n)

print("Numeros digitados: ")
for i in numeros:
    print(i)
