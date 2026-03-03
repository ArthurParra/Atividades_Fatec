import os
os.system('cls')

print('$$$ Programa de Empréstimos $$$ \n Responda (0-não 1-sim)')

neg= int(input("Possui nome negativo? "))
if neg == 1:
    print('Você nao pode realizar o emprestimo')
else:
    cartass= int(input('Você possui carteira assinada?'))
    if cartass==0:
        print("Não pode realizar emprestimos")
    else:
        casa = int(input('Possui casa propria?'))
        if casa == 0:
            print("Nao pode realizar emprestimos")
        else:
            print("conceder o emprestimo")