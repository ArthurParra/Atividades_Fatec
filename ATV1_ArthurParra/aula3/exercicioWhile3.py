import os
os.system('cls')

# sistema de tabuada
print('-------------------- Sistema de Tabuada ----------------------')
num = int(input('Digite o numero que deseja ver a tabuada (de 1 a 10): '))

i = 1
while i <= 10:
    print(f'{num} x {i} = {num * i}')
    i += 1
    
print('Programa finalizado')