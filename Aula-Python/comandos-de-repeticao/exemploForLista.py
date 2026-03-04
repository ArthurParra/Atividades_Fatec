import os
os.system('cls')

#exemplo For utilizando lista de valotes pré-definidos
frutas = ['uva', 'banana', 'maçã', 'pitaya']

for lista in frutas:
    print(lista)

buscar = 'pitaya'
frutas = ['uva', 'banana', 'maçã', 'pitaya']
for lista in frutas:
    if lista == buscar:
        print(f"Fruta encontrada: {buscar}")
        break
    else:
        print(f"Fruta não encontrada: {buscar}")
