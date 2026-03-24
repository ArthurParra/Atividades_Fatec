import os
os.system('cls')

tabuada = int(input('Tabuada de: '))
inicio = int(input('De: '))
fim = int(input('Até: '))

while inicio <= fim:
    print(f'{tabuada} x {inicio} = {tabuada * inicio}')
    inicio += 1